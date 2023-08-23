FROM python:3.8-slim

COPY . /gradunwarp

RUN cd /gradunwarp \
  && pip install -r requirements.txt \
  && pip install .

ENV PATH /gradunwarp/docker:$PATH

ENTRYPOINT ["/usr/local/bin/gradient_unwarp.py"]
