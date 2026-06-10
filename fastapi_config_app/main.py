from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from init_dependencies import init_dependencies
from routes.config_routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    deps = init_dependencies()
    app.state.dependencies = deps
    yield


app = FastAPI(
    title="Laboratory FastAPI App",
    version="1.0.0",
    description="Учебное приложение на FastAPI",
    lifespan=lifespan,
)

app.include_router(router)


@app.get("/")
async def root():
    return RedirectResponse("/docs")
