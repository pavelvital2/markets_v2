from __future__ import annotations

from fastapi import FastAPI

from market_analytics.api.routes import router as analytics_router
from market_analytics.web.routes import router as web_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="market-analytics",
        version="0.1.0",
        description="Skeleton analytics service for parser export bundle imports.",
    )
    app.include_router(analytics_router)
    app.include_router(web_router)

    @app.get("/healthz", include_in_schema=False)
    def healthz() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
