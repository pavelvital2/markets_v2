"""Shared parser V2 constants."""

SCHEMA_VERSION = "market-parser-v2.contract.v0"
SUPPORTED_PROVIDER_IDS = ("wb", "ozon")
MARKETPLACE_ALL = "all"

MANDATORY_SERVICE_FIELDS = (
    "run_id",
    "component",
    "collected_at_utc",
    "source_system",
    "source_type",
    "source_ref",
    "status",
    "error_message",
    "schema_version",
)

REQUIRED_EXPORT_FILES = (
    "marts/queries.csv",
    "marts/products.csv",
    "marts/sellers.csv",
    "marts/seller_query_product_bridge.csv",
    "quality/data_quality_summary.json",
    "metadata/contract.json",
)

FORBIDDEN_EXPORT_NAME_PARTS = (
    "cookie",
    "secret",
    "token",
    "har",
    "profile",
    "raw_html",
    "raw_json",
)
