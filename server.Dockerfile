FROM python:3.9
COPY placeholder/server.pex /bin
ENTRYPOINT ["/bin/server.pex"]
