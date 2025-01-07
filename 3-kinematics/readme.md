# Project 3: Kinematics for Manipulators

A manipulator is a mechanical system that is controlled by a set of joints. The joints are connected to each other by rigid links. The end-effector (EE) is the last link of the manipulator and it is the part of the manipulator that interacts with the environment. The kinematics of a manipulator is the study of the relationship between the joint angles and the position and orientation of the EE.

## Files details

### 01-intro-gen3lite.ipynb

A brief introduction to the Kinova Gen3 lite manipulator and how to control it.

### Kinova_3DoF_Joint_Control

Notebook to compute the inverse kinematics of the 3-DoF Kinova Gen3 lite.

### DirectKinematics

Notebook to compute the position of the EE of the Kinova Gen3 lite from the joint positions

## Installation

```bash
# install conan
mamba install conan==1.59

# run conan config to set up for build kortex_ros package
conan config set general.revisions_enabled=1
conan profile new default --detect > /dev/null
conan profile update settings.compiler.libcxx=libstdc++11 default
```
