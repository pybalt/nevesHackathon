from web3 import Web3
from utils.logger import logger


def get_raw_traces(data):
    """Consist on the raw data, but deleting logs in each call if they exist. This is a recursive process"""
    if isinstance(data, dict):
        if "logs" in data:
            del data["logs"]
        if "calls" in data:
            for call in data["calls"]:
                get_raw_traces(call)
    return data


def to_checksum_address(address):
    return Web3.to_checksum_address(address)


def flatten_calls(calls):
    flat_calls = []
    for call in calls:
        flat_calls.append(call)
        if "calls" in call:
            flat_calls.extend(flatten_calls(call["calls"]))
    return flat_calls


def get_internals_from_tx_traces_geth(calls):
    internal_txs = []

    raw_traces = flatten_calls(calls)

    for tx in raw_traces:
        try:
            if tx.get("type") == "DELEGATECALL":
                continue

            value = 0

            if tx.get("value") is not None:
                value_hex = tx.get("value")
                if value_hex.startswith("0x"):
                    value_hex = value_hex[2:]
                value = int(value_hex, 16)
            elif tx.get("value") is None and tx.get("type") == "STATICCALL":
                pass
            else:
                return [{"Error": f"Unhandled scenario in geth traces: {raw_traces}"}]

            if value > 0:
                internal_txs.append(
                    {
                        "From": to_checksum_address(tx.get("from")),
                        "To": to_checksum_address(tx.get("to")),
                        "Value": value,
                        "Type": tx.get("type").lower(),
                    }
                )
        except Exception as e:
            logger.error(f"Getting traces from geth error: {str(e)}")
            return [{"Error": f"Getting traces from geth error: {str(e)}"}]

    return internal_txs


def extract_logs(call):
    tx_logs = []

    if "logs" in call:
        tx_logs.extend(call["logs"])
    if "calls" in call:
        for subcall in call["calls"]:
            sub_tx_logs = extract_logs(subcall)
            tx_logs.extend(sub_tx_logs)
    for log in tx_logs:
        log["address"] = to_checksum_address(log["address"])
        if "index" in log:
            log["logIndex"] = hex(log["index"])
            del log["index"]
    return tx_logs


def transform_trace_call_to_preview(network, data: dict) -> dict:
    """Transforms the response from the RPC node to a preview response"""
    decodedInput = {}
    eventLogs = []
    data = data["result"]
    tx_recepit = {
        "transactionHash": None,
        "transactionIndex": None,
        "blockHash": None,
        "blockNumber": None,
        "from": data.get("from"),
        "to": data.get("to"),
        "cumulativeGasUsed": None,
        "gasUsed": data["gasUsed"],
        "effectiveGasPrice": None,
        "status": None,
    }
    internalTxs = get_internals_from_tx_traces_geth(data["calls"])
    rawTx = {
        "from": data.get("from"),
        "to": data.get("to"),
        "value": data.get("value"),
        "input": data.get("input"),
    }

    tx_logs = extract_logs(data)

    tx_recepit["logs"] = tx_logs
    rawTraces = get_raw_traces(data)
    return {
        "network": network,
        "txReceipt": tx_recepit,
        "decodedInput": decodedInput,
        "eventLogs": eventLogs,
        "internalTxs": internalTxs,
        "rawTx": rawTx,
        "rawTraces": rawTraces,
    }
