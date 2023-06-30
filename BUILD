python_requirements(
    name="root",
    overrides={
            "sqlalchemy": {"dependencies": [":root#psycopg2"]},
        },
)

docker_image(
    name="monitor",
    source="monitor.Dockerfile",
    repository="example/monitor",
)

docker_image(
    name="server",
    source="server.Dockerfile",
    repository="example/server",
)
