python_sources()

pex_binary(
    name="server",
    script="uvicorn",
    dependencies=["apps/backend/server.py"],
    args=["apps.backend.server:app", "--host", "0.0.0.0", "--port", "8000"],
)

docker_image(
    name="app",
    source="server.Dockerfile",
    repository="example/backend",
)
