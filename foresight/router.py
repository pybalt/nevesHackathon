from fastapi.routing import APIRouter

from fastapi.responses import JSONResponse

from foresight.schemas import PostPreviewSchema
from rpcnode.api import rpc_node_client
from foresight.helpers import transform_trace_call_to_preview

router = APIRouter()


@router.post("/preview/raw")
def preview(data: PostPreviewSchema):
    try:
        params = {
            "transaction": data.transaction.model_dump(),
            "reference": data.reference,
        }
        network = data.network
        rpc_node_response = rpc_node_client.debug_trace_call(params, network)
        response = transform_trace_call_to_preview(network, rpc_node_response)
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
