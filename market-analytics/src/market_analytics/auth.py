from __future__ import annotations

import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from market_analytics.config import Settings, load_settings

security = HTTPBasic()


def get_settings() -> Settings:
    return load_settings()


def require_basic_auth(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> str:
    if not settings.auth_configured:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Basic auth is not configured.",
        )

    username_ok = secrets.compare_digest(credentials.username, settings.auth_username or "")
    secret_ok = secrets.compare_digest(credentials.password, settings.auth_secret or "")
    if not (username_ok and secret_ok):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials.",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
