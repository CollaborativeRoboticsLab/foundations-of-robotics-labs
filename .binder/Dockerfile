# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Based on
# FROM jupyter/scipy-notebook:ubuntu-22.04
FROM ros:humble-ros-base-jammy

ARG NB_USER="founder"
ARG NB_UID="1000"
ARG NB_GID="100"

# install missing packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    bzip2 \
    ca-certificates \
    locales \
    netbase \
    sudo \
    tini \
    # wget \
    iputils-ping \
    net-tools \
    # curl \
    # git \
    nano-tiny \
    tzdata \
    unzip \
    openssh-client \
    python3-pip \
    ros-humble-turtlesim && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# set up environment variables
ENV NB_USER="${NB_USER}" \
    NB_UID=${NB_UID} \
    NB_GID=${NB_GID}
ENV HOME="/home/${NB_USER}"

# create the notebook user
RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers && \
    sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers && \
    useradd --no-log-init --create-home --shell /bin/bash --uid "${NB_UID}" --no-user-group "${NB_USER}" && \
    chmod g+w /etc/passwd

# install source requirements file
COPY ./requirements-lock.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# # get ROS package sources for the course
# RUN mkdir -p /home/${NB_USER}/colcon_ws/src && \
#     cd /home/${NB_USER}/colcon_ws/src && \
#     git clone https://github.com/CollaborativeRoboticsLab/sphero_rvr_desktop

# # update ROS dependencies
# RUN apt-get update && \
#     rosdep install --from-paths /home/${NB_USER}/colcon_ws/src/sphero_rvr_desktop --ignore-src -r -y && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*

# Make sure the contents of our repo are in ${HOME}
RUN mkdir -p ${HOME}/work
COPY . ${HOME}/work

# change ownership of the workspace
RUN chown -R ${NB_UID}:${NB_GID} ${HOME}

# switch back to the user
USER ${NB_UID}

RUN echo "source /opt/ros/humble/setup.bash" >> ${HOME}/.bashrc
RUN rosdep update

# export ROS environment variables in bashrc
RUN echo "export RMW_IMPLEMENTATION=rmw_fastrtps_cpp" >> ${HOME}/.bashrc
RUN echo "export ROS_LOCALHOST_ONLY=0" >> ${HOME}/.bashrc
RUN echo "export DISCOVERY_SERVER_PORT=11811" >> ${HOME}/.bashrc

# expose the notebook port and start the notebook server
EXPOSE 8888
WORKDIR ${HOME}
ENTRYPOINT ["tini", "--", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--IdentityProvider.token=''", "--ServerApp.password=''"]
