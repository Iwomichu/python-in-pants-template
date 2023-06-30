FROM python:3.9
COPY placeholder/app.pex /bin
ENTRYPOINT ["/bin/app.pex", "info"]
