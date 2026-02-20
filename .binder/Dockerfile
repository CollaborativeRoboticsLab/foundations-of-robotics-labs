# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Based on
# FROM jupyter/scipy-notebook:ubuntu-22.04
FROM ros:jazzy-ros-base

ARG NB_USER="frlab"
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
    python3-venv \
    ros-jazzy-rviz2 \
    ros-jazzy-turtlesim \
    ros-jazzy-turtlebot3 \
    ros-jazzy-turtlebot3-cartographer \
    ros-jazzy-turtlebot3-teleop \
    ros-jazzy-turtlebot3-gazebo && \
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
    if id "${NB_UID}" >/dev/null 2>&1; then \
    existing_user=$(getent passwd "${NB_UID}" | cut -d: -f1) && \
    usermod -l "${NB_USER}" -d "/home/${NB_USER}" -m "${existing_user}"; \
    else \
    useradd --no-log-init --create-home --shell /bin/bash --uid "${NB_UID}" --no-user-group "${NB_USER}"; \
    fi && \
    chmod g+w /etc/passwd

# create venv and install python deps
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

RUN python3 -m venv --system-site-packages "$VIRTUAL_ENV" \
    && pip install --upgrade pip setuptools wheel

# install source requirements file
COPY ./requirements-lock.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# export ROS environment variables in bashrc
RUN echo "export RMW_IMPLEMENTATION=rmw_fastrtps_cpp" >> ${HOME}/.bashrc
RUN echo "export ROS_LOCALHOST_ONLY=0" >> ${HOME}/.bashrc
RUN echo "export DISCOVERY_SERVER_PORT=11811" >> ${HOME}/.bashrc
RUN echo "export ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET" >> ${HOME}/.bashrc
RUN echo "export ROS_SUPER_CLIENT=True" >> ${HOME}/.bashrc
RUN echo "source /opt/ros/jazzy/setup.bash" >> ${HOME}/.bashrc
RUN rosdep update

# # get ROS package sources for the course
# RUN mkdir -p /home/${NB_USER}/colcon_ws/src && \
#     cd /home/${NB_USER}/colcon_ws/src && \
#     # git clone https://github.com/CollaborativeRoboticsLab/sphero_rvr_ros && \
#     git clone -b ros2 https://github.com/CollaborativeRoboticsLab/sphero_rvr_desktop

# # update ROS dependencies
# RUN apt-get update && \
#     rosdep install --from-paths /home/${NB_USER}/colcon_ws/src/sphero_rvr_desktop --ignore-src -r -y && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*

# # build ROS packages
# RUN /bin/bash -c "source /opt/ros/jazzy/setup.bash && cd /home/${NB_USER}/colcon_ws && colcon build"

# # add workspace setup to bashrc
# RUN echo "source /home/${NB_USER}/colcon_ws/install/setup.bash" >> ${HOME}/.bashrc

# Make sure the contents of our repo are in ${HOME}
RUN mkdir -p ${HOME}/work
COPY . ${HOME}/work

# change ownership of the workspace
RUN chown -R ${NB_UID}:${NB_GID} ${HOME}

# switch back to the user
USER ${NB_UID}

# expose the notebook port and start the notebook server
EXPOSE 8888
WORKDIR ${HOME}/work
ENTRYPOINT ["tini", "--", "/bin/bash", "-c", "cd ${HOME}/work && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --IdentityProvider.token='' --ServerApp.password=''" ]
