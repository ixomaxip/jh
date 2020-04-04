ARG BASE
FROM $BASE


RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0


COPY config/jupyterhub_config.py .
COPY config/cull_idle_servers.py .

COPY nativeauthenticator .
RUN pip install -e .