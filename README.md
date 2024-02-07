# Foundations of Robotics Lab Notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](<https://mybinder.org/v2/gh/AIResearchLab/foundations-of-robotics-labs/HEAD>)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github/AIResearchLab/foundations-of-robotics-labs>)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-dev-blue)](https://open.vscode.dev/AIResearchLab/foundations-of-robotics-labs)

These Python Jupyter notebooks are designed for academic teaching laboratories in robotics, using Gazebo for simulation up to physical deployment on robotic platforms. The students are not expected to install or deploy the required ROS workspace on their personal computer, but rather use lab resources at the university. The laboratories were designed at École de technologie supérieure, in Montréal, Canada, and adapted for the University of Canberra. Robotic platforms are available for the students to test their algorithms along with shared laptop stations.

## Prerequisites

The notebooks are designed to be used with a ROS workspace that contains the following packages:

- [Sphero RVR ROS](<https://github.com/AIResearchLab/sphero_rvr_ros>) - ROS packages for the Sphero RVR
- [Kinova Gen3 lite ROS](<https://github.com/Kinovarobotics/ros_kortex>) - ROS packages for the Kinova Gen3 lite

## Projects

- [**Project 0 - Primers**](<./0-primers/>) - Primers on Python, the terminal, and ROS
- [**Project 1 - Sense -> Think -> Act**](<./Project1/>) - Feedback & Robotic algorithm fundamentals
- [**Project 2 - Perception, Filters, and Navigation**](<./Project2/>) - Localization, Navigation & Mapping
- [**Project 3 - Kinematics**](<./3-kinematics/>) - Kinematics for a Robot Manipulator
- [**Project 4**](<./Project4/>) - Mobile Robotics & Manipulator Control
- [**Project 5**](<./Project5/>) - Perception and Navigation

## Installation

### ROS

The software requires ROS to be installed to use the `rospy` libraries. Follow the instructions for ROS `Noetic` on the [official website](https://ros.org).

### Virtual Environment

Setting up a python virtual environment for can be useful in some development situations. Run the following command in a terminal at the top level of this git repository.

```python
# create virtual environment
python3 -m venv .venv

# linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Running the code

In a terminal at the top level of this git repository, run the following.

```bash
source .venv/bin/activate

# start a jupyter notebook server
jupyter lab --ip=0.0.0.0 --port=8888

# or run a voila server for the UI only version
voila . --port=8866
```

## Experimental Software Disclaimer

The contents of this source is provided in an experimental state and does not guarantee safe or correct operation.

The contents of this source is subject to change, without prior notice. Any available APIs are to be considered unstable and are not guaranteed to be complete and / or functional.
