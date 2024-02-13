# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Based on
# FROM jupyter/datascience-notebook:ubuntu-20.04
FROM ghcr.io/mpo-web-consulting/ros-notebook:datascience-noetic

# get ROS package sources for the course
USER root
RUN mkdir -p /home/${NB_USER}/catkin_ws/src && \
    cd /home/${NB_USER}/catkin_ws/src && \
    git clone https://github.com/Kinovarobotics/ros_kortex && \
    git clone https://github.com/AIResearchLab/sphero_rvr_ros

# update ROS dependencies
RUN apt-get update && \
    rosdep install --from-paths /home/${NB_USER}/catkin_ws/src --ignore-src -r -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Make sure the contents of our repo are in ${HOME}
RUN mkdir -p ${HOME}/work
COPY . ${HOME}/work

# install pip dependencies
RUN pip install --no-cache-dir -r ${HOME}/work/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}
