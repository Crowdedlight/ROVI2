# Install script for directory: /home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/olliver/localbuild/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure/msg" TYPE FILE FILES
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/BoolParameter.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/Config.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/Group.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/IntParameter.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/SensorLevels.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/ConfigDescription.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/DoubleParameter.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/GroupState.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/ParamDescription.msg"
    "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg/StrParameter.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure/srv" TYPE FILE FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/srv/Reconfigure.srv")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure/cmake" TYPE FILE FILES "/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/catkin_generated/installspace/dynamic_reconfigure-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/devel/include/dynamic_reconfigure")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/devel/share/roseus/ros/dynamic_reconfigure")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/devel/share/common-lisp/ros/dynamic_reconfigure")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/devel/share/gennodejs/ros/dynamic_reconfigure")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/olliver/localbuild/catkin_ws/devel/lib/python2.7/dist-packages/dynamic_reconfigure")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/devel/lib/python2.7/dist-packages/dynamic_reconfigure" REGEX "/\\_\\_init\\_\\_\\.py$" EXCLUDE REGEX "/\\_\\_init\\_\\_\\.pyc$" EXCLUDE)
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/devel/lib/python2.7/dist-packages/dynamic_reconfigure" FILES_MATCHING REGEX "/home/olliver/localbuild/catkin_ws/devel/lib/python2.7/dist-packages/dynamic_reconfigure/.+/__init__.pyc?$")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/dynamic_reconfigure" TYPE FILE FILES "/home/olliver/localbuild/catkin_ws/devel/include/dynamic_reconfigure/TestConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/olliver/localbuild/catkin_ws/devel/lib/python2.7/dist-packages/dynamic_reconfigure/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/dynamic_reconfigure" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/devel/lib/python2.7/dist-packages/dynamic_reconfigure/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/catkin_generated/installspace/dynamic_reconfigure.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure/cmake" TYPE FILE FILES
    "/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/catkin_generated/installspace/dynamic_reconfigure-msg-extras.cmake"
    "/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/catkin_generated/installspace/dynamic_reconfigure-extras.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure/cmake" TYPE FILE FILES
    "/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/catkin_generated/installspace/dynamic_reconfigureConfig.cmake"
    "/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/catkin_generated/installspace/dynamic_reconfigureConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure" TYPE FILE FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/dynamic_reconfigure" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/include/dynamic_reconfigure/" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdynamic_reconfigure_config_init_mutex.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdynamic_reconfigure_config_init_mutex.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdynamic_reconfigure_config_init_mutex.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/olliver/localbuild/catkin_ws/devel/lib/libdynamic_reconfigure_config_init_mutex.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdynamic_reconfigure_config_init_mutex.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdynamic_reconfigure_config_init_mutex.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libdynamic_reconfigure_config_init_mutex.so")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/cmake" USE_SOURCE_PERMISSIONS)
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/msg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/dynamic_reconfigure" TYPE PROGRAM FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/scripts/dynparam")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/dynamic_reconfigure" TYPE PROGRAM FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/scripts/reconfigure_gui")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/srv")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_reconfigure" TYPE DIRECTORY FILES "/home/olliver/localbuild/catkin_ws/src/dynamic_reconfigure/templates")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/olliver/localbuild/catkin_ws/build/dynamic_reconfigure/test/cmake_install.cmake")

endif()

