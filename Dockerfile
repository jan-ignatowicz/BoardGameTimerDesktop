# set base image (host OS)
FROM ubuntu:20.04

MAINTAINER jan.ignatowicz2@gmail.com

ENV DEBIAN_FRONTEND=noninteractive

# This fix: libGL error: No matching fbConfigs or visuals found
ENV LIBGL_ALWAYS_INDIRECT=1

# set the working directory in the container
WORKDIR /home/app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN apt-get update && \
    apt-get install -y python3-pyqt5 python3-pip && \
    pip3 install -r requirements.txt

# copy the content of the app code files to the working directory
COPY src ./src
COPY src/main/board_game_timer_app.py ./board_game_timer_app.py

# command to run on container start
CMD [ "python3", "/home/app/board_game_timer_app.py" ]
