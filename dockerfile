FROM jenkins/jenkins:lts-jdk11
USER root
RUN mkdir /my_app
WORKDIR /my_app
COPY * /my_app
RUN apt-get update
RUN apt-get install -y python3
# Install app dependencies
#RUN pip install --upgrade pip
