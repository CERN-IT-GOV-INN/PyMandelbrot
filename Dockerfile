# This Dockerfile encapsulates the computational environment that is necessary
# to successfully run the PyManderbrot package example.
#
# You can build and distribute this Docker image as follows:
#
# $ cd example-repo
# $ docker build -t tiborsimko/pymandelbrot:1.0.0 .
# $ docker push tiborsimko/pymandelbrot:1.0.0
#
# It can be used as an inspiration for your own analyses that use the
# PyManderbrot package.

# Use Debian 11.3 base image
FROM debian:11.3

# Install system dependencies
RUN apt-get -y update && \
    apt-get -y install \
        cm-super \
        dvipng \
        python-is-python3 \
        python3 \
        python3-pip \
        texlive \
        texlive-latex-extra && \
    apt-get -y clean

# Install Python requirements
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt

# Add PyMandelbrot package sources to `/code` and work there
WORKDIR /code
COPY . /code

# Install PyManderbrot package
RUN pip install --no-cache-dir .
