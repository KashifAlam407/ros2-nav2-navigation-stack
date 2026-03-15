from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    params_file = "/home/kingkhan/assignment_ws/src/l1-KashifAlam407/testbed_navigation/config/nav2_params.yaml"

    planner = Node(
        package="nav2_planner",
        executable="planner_server",
        name="planner_server",
        output="screen",
        parameters=[params_file]
    )

    controller = Node(
        package="nav2_controller",
        executable="controller_server",
        name="controller_server",
        output="screen",
        parameters=[params_file]
    )

    bt_navigator = Node(
        package="nav2_bt_navigator",
        executable="bt_navigator",
        name="bt_navigator",
        output="screen",
        parameters=[params_file]
    )

    behavior = Node(
        package="nav2_behaviors",
        executable="behavior_server",
        name="behavior_server",
        output="screen",
        parameters=[params_file]
    )

    lifecycle = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_navigation",
        output="screen",
        parameters=[{
            "use_sim_time": True,
            "autostart": True,
            "node_names": [
                "planner_server",
                "controller_server",
                "bt_navigator",
                "behavior_server"
            ]
        }]
    )

    return LaunchDescription([
        planner,
        controller,
        bt_navigator,
        behavior,
        lifecycle
    ])
