#ARG BASE_CONTAINER=jupyter/minimal-notebook
#FROM $BASE_CONTAINER
# LABEL author="sagar limbu"
ARG APP_DIR=/app

FROM python:3.10-slim-buster as build

ARG APP_DIR

RUN apt-get -y update \
	&& apt-get install -y \
	curl \
	build-essential \
	libffi-dev \
	&& rm -rf /var/lib/apt/lists/*

## jupyter notebook
#FROM jupyter/minimal-notebook

WORKDIR ${APP_DIR}
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt && \
	jupyter nbextension enable --py widgetsnbextension --sys-prefix

## generate config file for jupyter notebook
## Store password credentials
RUN jupyter notebook --generate-config

RUN sleep 9
# RUN echo "c.NotebookApp.password = 'password'" >> /root/.jupyter/jupyter_notebook_config.py 
RUN echo "c.NotebookApp.password = password" >> /root/.jupyter/jupyter_notebook_config.py 


# /root/.jupyter/jupyter_notebook_config.py 
# /root/.jupyter/jupyter_notebook_config.py


CMD ["jupyter", "notebook","--ip=0.0.0.0","--port=8888", "--no-browser", "--allow-root"]
#"--NotebookApp.token = u''", "--NotebookApp.password = u''"]
