# image - sudosk/mosotf:latest

# continuumio/miniconda3:4.8.2
FROM continuumio/miniconda3@sha256:456e3196bf3ffb13fee7c9216db4b18b5e6f4d37090b31df3e0309926e98cfe2

LABEL authors="sangramsahu15@gmail.com" \
      description="Docker image containing dependencies for krassowski/multi-omics-state-of-the-field"

COPY environment.yml /

RUN apt-get update && \
  conda env update -f /environment.yml -n root && \
  conda clean -a
