set(_AMENT_PACKAGE_NAME "usb_cam")
set(usb_cam_VERSION "0.6.1")
set(usb_cam_MAINTAINER "Evan Flynn <evanflynn.msu@gmail.com>")
set(usb_cam_BUILD_DEPENDS "cv_bridge" "rclcpp" "rclcpp_components" "std_msgs" "std_srvs" "sensor_msgs" "camera_info_manager" "builtin_interfaces" "image_transport" "image_transport_plugins" "v4l-utils" "ffmpeg")
set(usb_cam_BUILDTOOL_DEPENDS "ament_cmake_auto" "rosidl_default_generators")
set(usb_cam_BUILD_EXPORT_DEPENDS "cv_bridge" "rclcpp" "rclcpp_components" "std_msgs" "std_srvs" "sensor_msgs" "camera_info_manager" "builtin_interfaces" "image_transport" "image_transport_plugins" "v4l-utils" "ffmpeg")
set(usb_cam_BUILDTOOL_EXPORT_DEPENDS )
set(usb_cam_EXEC_DEPENDS "rosidl_default_runtime" "cv_bridge" "rclcpp" "rclcpp_components" "std_msgs" "std_srvs" "sensor_msgs" "camera_info_manager" "builtin_interfaces" "image_transport" "image_transport_plugins" "v4l-utils" "ffmpeg")
set(usb_cam_TEST_DEPENDS "ament_cmake_gtest" "ament_lint_auto" "ament_lint_common")
set(usb_cam_GROUP_DEPENDS )
set(usb_cam_MEMBER_OF_GROUPS "rosidl_interface_packages")
set(usb_cam_DEPRECATED "")
set(usb_cam_EXPORT_TAGS)
list(APPEND usb_cam_EXPORT_TAGS "<build_type>ament_cmake</build_type>")
