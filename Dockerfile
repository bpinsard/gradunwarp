FROM python:3.8-slim

COPY . /gradunwarp

RUN cd /gradunwarp \
  && pip install -r requirements.txt \
  && pip install .

ENTRYPOINT ["/usr/local/bin/gradient_unwarp.py"]
