# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/olliver/localbuild/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/olliver/localbuild/catkin_ws/build

# Utility rule file for git_gps_devices.

# Include the progress variables for this target.
include Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/progress.make

Firmware/src/drivers/gps/CMakeFiles/git_gps_devices: Firmware/src/drivers/gps/git_init_devices.stamp


Firmware/src/drivers/gps/git_init_devices.stamp: /home/olliver/localbuild/catkin_ws/src/Firmware/.gitmodules
Firmware/src/drivers/gps/git_init_devices.stamp: /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/gps/devices/.git
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/olliver/localbuild/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "git submodule devices"
	cd /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/gps && bash /home/olliver/localbuild/catkin_ws/src/Firmware/Tools/check_submodules.sh devices
	cd /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/gps && cmake -E touch /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/gps/git_init_devices.stamp

git_gps_devices: Firmware/src/drivers/gps/CMakeFiles/git_gps_devices
git_gps_devices: Firmware/src/drivers/gps/git_init_devices.stamp
git_gps_devices: Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/build.make

.PHONY : git_gps_devices

# Rule to build all files generated by this target.
Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/build: git_gps_devices

.PHONY : Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/build

Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/clean:
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/gps && $(CMAKE_COMMAND) -P CMakeFiles/git_gps_devices.dir/cmake_clean.cmake
.PHONY : Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/clean

Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/depend:
	cd /home/olliver/localbuild/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/olliver/localbuild/catkin_ws/src /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/gps /home/olliver/localbuild/catkin_ws/build /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/gps /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Firmware/src/drivers/gps/CMakeFiles/git_gps_devices.dir/depend

