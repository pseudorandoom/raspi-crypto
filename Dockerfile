FROM python:2.7

RUN pip install pycrypto

ENTRYPOINT ["/usr/bin/env", "python"]
