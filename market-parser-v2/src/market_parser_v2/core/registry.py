"""Provider registry for offline skeleton operations."""

from __future__ import annotations

from market_parser_v2.core.constants import MARKETPLACE_ALL, SUPPORTED_PROVIDER_IDS
from market_parser_v2.providers.base import Provider
from market_parser_v2.providers.ozon import OzonProvider
from market_parser_v2.providers.wb import WbProvider


_PROVIDERS: dict[str, Provider] = {
    "wb": WbProvider(),
    "ozon": OzonProvider(),
}


def get_provider(provider_id: str) -> Provider:
    try:
        return _PROVIDERS[provider_id]
    except KeyError as exc:
        raise ValueError(f"unknown provider: {provider_id}") from exc


def list_provider_ids() -> tuple[str, ...]:
    return SUPPORTED_PROVIDER_IDS


def resolve_marketplace(marketplace: str) -> tuple[str, ...]:
    if marketplace == MARKETPLACE_ALL:
        return SUPPORTED_PROVIDER_IDS
    if marketplace in SUPPORTED_PROVIDER_IDS:
        return (marketplace,)
    raise ValueError(f"unknown marketplace selector: {marketplace}")
