# ROS2 Nav2 Navigation Stack (Gazebo Simulation)

This repository demonstrates a **manual implementation of the ROS2 Navigation Stack (Nav2)** for a simulated mobile robot.

The robot runs in **Gazebo**, navigation is visualized in **RViz**, and the navigation stack is configured manually without using the default `nav2_bringup`.

The project includes robot description, simulation environment, bringup configuration, and a custom navigation package.

-----------------------------------------------------------------------

### Video Demonstration

[![ros2_trajectory_control](https://img.youtube.com/vi/y7erTK9Ahqo/0.jpg)](https://www.youtube.com/watch?v=y7erTK9Ahqo)

▶ Click the image above to watch the full demo video on YouTube.

-----------------------------------------------------------------------

# Repository Structure

```
ros2-nav2-navigation-stack
│
├── testbed_description
├── testbed_gazebo
├── testbed_bringup
├── testbed_navigation
```

---

# Folder Description

## testbed_description

Contains the **robot model and visualization configuration**.

Files inside this package define the robot structure and how it appears in simulation and RViz.

Includes:
- URDF files describing robot links and joints
- Mesh files for robot visualization
- RViz configuration files
- Launch files for loading the robot model

This package defines the **physical structure of the robot**.

---

## testbed_gazebo

Contains files required to run the robot inside **Gazebo simulation**.

Includes:
- Gazebo world files
- Simulation launch files
- Additional models used in the environment

This package is responsible for **simulating the robot and environment**.

---

## testbed_bringup

Responsible for **starting the robot simulation environment**.

This package launches:
- Gazebo simulation
- Robot model
- RViz visualization
- Robot controllers

Main launch file:

```
testbed_full_bringup.launch.py
```

Running this launch file starts the complete simulation environment.

---

## testbed_navigation

Implements the **ROS2 Navigation Stack (Nav2)** manually.

Instead of using `nav2_bringup`, navigation components are launched individually.

Includes configuration and launch files for:

- Map Server
- AMCL Localization
- Planner Server
- Controller Server
- Behavior Tree Navigator
- Behavior Server
- Costmaps

Navigation pipeline:

```
RViz Goal
   ↓
Planner
   ↓
Controller
   ↓
cmd_vel
   ↓
Robot Motion
```

---

# Build Workspace

```
cd ~/assignment_ws
colcon build
source install/setup.bash
```

---

# Run the Simulation

```
ros2 launch testbed_bringup testbed_full_bringup.launch.py
```

---

# Start Navigation

Load map:

```
ros2 launch testbed_navigation map_loader.launch.py
```

Start localization:

```
ros2 launch testbed_navigation localization.launch.py
```

Start navigation:

```
ros2 launch testbed_navigation navigation.launch.py
```

In RViz:

1. Click **2D Pose Estimate** to initialize the robot pose
2. Click **2D Goal Pose** to send a navigation goal

The robot will compute a path and navigate to the goal.

---

# Demo

YouTube Demo Video:  
(Add your video link here)

---

# Technologies Used

- ROS2 Humble
- Navigation2 (Nav2)
- Gazebo
- RViz
- AMCL Localization
- Path Planning and Control
