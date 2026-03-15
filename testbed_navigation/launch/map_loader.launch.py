from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{
            'yaml_filename': '/home/kingkhan/assignment_ws/src/l1-KashifAlam407/testbed_bringup/maps/testbed_world.yaml'
        }]
    )

    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_map',
        output='screen',
        parameters=[{
            'autostart': True,
            'node_names': ['map_server']
        }]
    )

    return LaunchDescription([
        map_server,
        lifecycle_manager
    ])
