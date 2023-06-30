FROM python:3.9
COPY placeholder/kafka_monitor.pex /bin
ENTRYPOINT ["/bin/kafka_monitor.pex", "--num-workers", "1", "--kafka-broker", "compose"]