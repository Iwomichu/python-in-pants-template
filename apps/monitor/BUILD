python_sources()

pex_binary(
    name="kafka_monitor",
    script="fastkafka",
    dependencies=["apps/monitor/main.py"],
    args=["run", "apps.monitor.main:kafka_app"],
    execution_mode="venv",
)

docker_image(
    name="app",
    source="monitor.Dockerfile",
    repository="example/monitor",
)

