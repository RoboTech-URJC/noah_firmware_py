cmake_minimum_required(VERSION 3.5)
project(noah_firmware_py_launch)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE DEBUG)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

set(dependencies
    rclcpp
    rclpy
)

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY config DESTINATION share/${PROJECT_NAME})

ament_export_dependencies(${dependencies})

ament_package()