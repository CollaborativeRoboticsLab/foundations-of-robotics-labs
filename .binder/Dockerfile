# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Based on
# FROM jupyter/datascience-notebook:ubuntu-20.04
FROM ghcr.io/mpo-web-consulting/ros-notebook:datascience-noetic

# install missing packages
USER root
RUN apt-get update && \
    apt-get install -y \
    iputils-ping && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# get ROS package sources for the course
RUN mkdir -p /home/${NB_USER}/catkin_ws/src && \
    cd /home/${NB_USER}/catkin_ws/src && \
    git clone https://github.com/Kinovarobotics/ros_kortex && \
    git clone https://github.com/AIResearchLab/sphero_rvr_ros && \
    git clone https://github.com/AIResearchLab/sphero_rvr_desktop

# update ROS dependencies
RUN apt-get update && \
    rosdep install --from-paths /home/${NB_USER}/catkin_ws/src/ros_kortex --ignore-src -r -y && \
    rosdep install --from-paths /home/${NB_USER}/catkin_ws/src/sphero_rvr_ros --ignore-src -r -y && \
    # rosdep install --from-paths /home/${NB_USER}/catkin_ws/src/sphero_rvr_desktop --ignore-src -r -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Make sure the contents of our repo are in ${HOME}
RUN mkdir -p ${HOME}/work
COPY . ${HOME}/work

# install pip dependencies
# RUN pip install --no-cache-dir -r ${HOME}/work/requirements-lock.txt && \
RUN pip install --no-cache-dir -r ${HOME}/work/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# change ownership of the workspace
RUN chown -R ${NB_UID}:${NB_GID} ${HOME}

# switch back to the user
USER ${NB_UID}
