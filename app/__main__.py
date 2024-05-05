import uvicorn

from app.settings import settings


def main() -> None:
    uvicorn.run(
        "app.api.application:get_app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )


if __name__ == "__main__":
    main()
