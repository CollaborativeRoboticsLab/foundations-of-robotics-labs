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

- [**Project 0 - Primers**](<./0-primers/readme.md>) - Primers on Python, the terminal, and ROS
- [**Project 1 - Sense -> Think -> Act**](<./1-sense-think-act/README.md>) - Feedback & Robotic algorithm fundamentals
- [**Project 2 - Perception, Filters, and Navigation**](<./2-navigation/readme.md>) - Localization, Navigation & Mapping
- [**Project 3 - Kinematics**](<./3-kinematics/README.md>) - Kinematics for a Robot Manipulator
- [**Project 4 - Mobile Manipulators**](<./4-mobile-manipulators/>) - Mobile Robotics & Manipulator Control
- [**Project 5 - Inference**](<./5-inference/readme.md>) - Perception and Navigation

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

The code is provided as [Jupyter notebooks](https://jupyter.org). In a terminal at the top level of this git repository, run the following.

```bash
source .venv/bin/activate

# start a jupyter notebook server
jupyter lab --ip=0.0.0.0 --port=8888
# open a web browser to the address provided in the terminal
# for example: http://localhost:8888/lab?token=...

# or run a voila server for the UI only version
voila . --port=8866
```

## Contributing

Contributions are welcome. Please read the [contributing guidelines](<./CONTRIBUTING.md>) for more information.

### Found an Issue?

[![Fork](https://img.shields.io/badge/Fork-Repository-purple)](https://github.com/AIResearchLab/foundations-of-robotics-labs/fork)
[![Open Issue](https://img.shields.io/badge/Open-Issue-purple)](https://github.com/AIResearchLab/foundations-of-robotics-labs/issues/new)

Fork the repository, make a pull request or open an issue. Contributions are welcome.

## Experimental Software Disclaimer

The contents of this source is provided in an experimental state and does not guarantee safe or correct operation.

The contents of this source is subject to change, without prior notice. Any available APIs are to be considered unstable and are not guaranteed to be complete and / or functional.
