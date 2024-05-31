from fastapi.routing import APIRouter

from fastapi.responses import JSONResponse

from foresight.schemas import PostPreviewSchema
from rpcnode.api import rpc_node_client

router = APIRouter()


@router.post("/raw/data")
def raw_preview(data: PostPreviewSchema):
    params = {
        "transaction": data.transaction.model_dump(),
        "reference": data.reference,
    }
    network = data.network
    try:
        rpc_node_response = rpc_node_client.debug_trace_call(params, network)
        return JSONResponse(content=rpc_node_response, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
