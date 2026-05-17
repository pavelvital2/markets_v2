"""Shared parser V2 constants."""

SCHEMA_VERSION = "market-parser-v2.contract.v0"
SUPPORTED_SCHEMA_VERSIONS = (SCHEMA_VERSION,)
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

QUERY_MART_FIELDS = (
    "marketplace",
    "source_system",
    "run_id",
    "query",
    "normalized_query",
    "canonical_query",
    "query_group",
    "source_query",
    "rank",
    "score",
    "hybrid_score",
    "wordstat_volume",
    "count",
    "selected_reason",
    "data_quality_status",
    "schema_version",
)

PRODUCT_MART_FIELDS = (
    "marketplace",
    "source_system",
    "run_id",
    "query",
    "query_group",
    "page",
    "position_on_page",
    "absolute_position",
    "external_product_id",
    "product_name",
    "brand",
    "external_seller_id",
    "seller_name",
    "final_price",
    "price",
    "old_price",
    "sale_price",
    "rating",
    "reviews_count",
    "feedbacks",
    "promo_markers",
    "raw_file",
    "raw_page_path",
    "data_quality_status",
    "schema_version",
)

SELLER_MART_FIELDS = (
    "marketplace",
    "source_system",
    "run_id",
    "external_seller_id",
    "seller_name",
    "seller_rating",
    "seller_reviews",
    "feedbacks_count",
    "product_count",
    "query_count",
    "queries_ref",
    "query_groups_ref",
    "external_product_ids_ref",
    "source_product_run_ids",
    "data_quality_status",
    "schema_version",
)

SELLER_QUERY_PRODUCT_BRIDGE_FIELDS = (
    "marketplace",
    "source_system",
    "run_id",
    "query",
    "query_group",
    "external_product_id",
    "external_seller_id",
    "seller_name",
    "product_run_id",
    "schema_version",
    "data_quality_status",
)

MART_FIELDS = {
    "queries": QUERY_MART_FIELDS,
    "products": PRODUCT_MART_FIELDS,
    "sellers": SELLER_MART_FIELDS,
    "seller_query_product_bridge": SELLER_QUERY_PRODUCT_BRIDGE_FIELDS,
}

MANIFEST_REQUIRED_FIELDS = (
    "marketplace",
    "source_system",
    "run_id",
    "schema_version",
    "export_created_at_utc",
    "component_statuses",
    "file_list",
    "row_counts",
    "checksums",
    "data_quality_summary",
    "usable_for_reports",
    "warnings",
    "errors",
)

FORBIDDEN_EXPORT_NAME_PARTS = (
    "cookie",
    "cookies",
    "secret",
    "secrets",
    "token",
    "api_key",
    "apikey",
    ".har",
    "/har/",
    "profile",
    "browser_profile",
    "chromium",
    ".log",
    "raw_html",
    "raw-json",
    "raw_json",
    "html_snapshot",
    "response_body",
)

FORBIDDEN_EXPORT_CONTENT_MARKERS = (
    "set-cookie",
    "authorization: bearer",
    "api_key=",
    "api-key=",
    "apikey=",
    "access_token=",
    "refresh_token=",
    "cookie=",
)
