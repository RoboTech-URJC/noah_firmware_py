# Copyright (c) 2022 Star Robotics.
#
# Licensed under a Propietary License, (the "License");
# you may not use this file except in compliance with the License.
#
# All rights are reserved.
# License: Commercial

"""noah_firmware_py launcher."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    """generate_launch_description."""
    # Configure environment
    stdout_linebuf_envvar = SetEnvironmentVariable(
        'RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED',
        '1')
    stdout_colorized_envvar = SetEnvironmentVariable(
        'RCUTILS_COLORIZED_OUTPUT',
        '1')

    # Node Configurations
    config_file = LaunchConfiguration('noah_firmware_config')
    declare_config_file_cmd = DeclareLaunchArgument(
      'noah_firmware_config',
      default_value=os.path.join(
        get_package_share_directory('noah_firmware_py_launch'),
        'config',
        'config.yaml'),
      description='Full path to the noah_firmware_py_launch config')

    # noah_firmware node
    noah_firmware_node = Node(
        package='noah_firmware_py',
        executable='noah_firmware_py',
        name='noah_firmware_py',
        output='screen',
        parameters=[config_file]
    )

    ld = LaunchDescription()
    # Set environment variables
    ld.add_action(stdout_linebuf_envvar)
    ld.add_action(stdout_colorized_envvar)
    ld.add_action(declare_config_file_cmd)
    # Add nodes
    ld.add_action(noah_firmware_node)

    return ld
