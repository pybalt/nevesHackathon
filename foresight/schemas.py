from typing import Optional
from pydantic import BaseModel, Field
from .constants import (
    DEFAULT_FROM,
    DEFAULT_TO,
    DEFAULT_DATA,
    DEFAULT_GAS,
    DEFAULT_GAS_PRICE,
    DEFAULT_REFERENCE,
    ETHEREUM_NETWORK,
)


class TransactionSchema(BaseModel):
    from_field: str = Field(
        title="From",
        description="The sender's email address",
        alias="from",
        default=DEFAULT_FROM,
    )
    to: str = Field(
        title="To", description="The recipient's email address", default=DEFAULT_TO
    )
    data: str = Field(
        title="Data", description="The data to be sent", default=DEFAULT_DATA
    )
    gas: Optional[str] = Field(
        title="Gas", description="The gas to be used", default=DEFAULT_GAS
    )
    gasPrice: Optional[str] = Field(
        title="Gas Price",
        description="The gas price to be used",
        default=DEFAULT_GAS_PRICE,
    )
    gasFeeCap: Optional[str] = Field(
        title="Gas Fee Cap", description="The gas fee cap to be used", default=None
    )
    value: Optional[str] = Field(
        title="Value", description="The value to be sent", default=None
    )

    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda s: s.replace("_", "")


class PostPreviewSchema(BaseModel):
    transaction: TransactionSchema
    reference: str = Field(
        title="Reference",
        description="The reference for the transaction",
        default=DEFAULT_REFERENCE,
    )
    network: str = Field(
        title="Network",
        description="The network to be used for the transaction",
        default=ETHEREUM_NETWORK,
    )

    class Config:
        allow_population_by_field_name = True
