FROM python:3.8-slim

COPY . /gradunwarp

RUN cd /gradunwarp \
  && python setup.py install

ENV PATH /gradunwarp/docker:$PATH

ENTRYPOINT ["/bin/bash", "/gradunwarp/docker/run.sh"]
