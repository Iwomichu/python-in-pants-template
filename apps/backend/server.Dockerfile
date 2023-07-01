FROM python:3.9
COPY apps.backend/server.pex /bin
ENTRYPOINT ["/bin/server.pex"]
