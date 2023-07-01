python_sources()

pex_binary(
    name="app",
    entry_point="main.py",
)

pex_binary(
    name="server",
    script="uvicorn",
    dependencies=["placeholder/server.py"],
    args=["placeholder.server:app"],
)

pex_binary(
    name="kafka_monitor",
    script="fastkafka",
    dependencies=["placeholder/monitor.py"],
    args=["run", "placeholder.monitor:kafka_app"],
    execution_mode="venv",
)
