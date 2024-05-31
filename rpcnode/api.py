import requests
import json

from foresight.schemas import TransactionSchema
from .constants import DEBUG_CONFIG


class RPCNode:
    """RPC Node Client"""

    URL = "{This was deleted from the original code}"

    def __init__(self, url=None):
        self.url = url or self.URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def post(self, endpoint, params=None):
        response = self.session.post(f"{self.url}{endpoint}", data=params)
        response.raise_for_status()
        if "error" in response.json():
            raise Exception(response.json()["error"])
        return response

    def debug_trace_call(self, params, network):
        transaction = params.get("transaction")
        transaction = TransactionSchema(**transaction).model_dump(by_alias=True)
        block_reference = params.get("reference")
        payload = {
            "method": "debug_traceCall",
            "params": [transaction, block_reference, DEBUG_CONFIG],
            "id": 1,
            "jsonrpc": "2.0",
        }
        response = self.post(f"{network}_trace-geth/", params=json.dumps(payload))
        return response.json()


rpc_node_client = RPCNode()
