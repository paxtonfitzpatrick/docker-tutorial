FROM continuumio/miniconda3:4.10.3

LABEL maintainer="Paxton Fitzpatrick <Paxton.GR@dartmouth.edu>"

ENV LANG C.UTF-8

ARG DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN conda config --set auto_update_conda false \
        --set notify_outdated_conda false \
        --prepend channels conda-forge \
        --set channel_priority strict \
    && conda install -Sy \
        python==3.9.5 \
        pip==21.1.2 \
        notebook=6.1.4 \
        ipywidgets=7.5.1 \
        jupyter_contrib_nbextensions=0.5.1 \
        tini=0.18.0 \
