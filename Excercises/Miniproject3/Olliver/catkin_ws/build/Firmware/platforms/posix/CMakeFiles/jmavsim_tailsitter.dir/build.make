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

# Utility rule file for jmavsim_tailsitter.

# Include the progress variables for this target.
include Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/progress.make

Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter:
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/tmp && /home/olliver/localbuild/catkin_ws/src/Firmware/Tools/sitl_run.sh /home/olliver/localbuild/catkin_ws/devel/lib/px4/px4 posix-configs/SITL/init/ekf2 none jmavsim tailsitter /home/olliver/localbuild/catkin_ws/src/Firmware /home/olliver/localbuild/catkin_ws/build/Firmware

jmavsim_tailsitter: Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter
jmavsim_tailsitter: Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/build.make

.PHONY : jmavsim_tailsitter

# Rule to build all files generated by this target.
Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/build: jmavsim_tailsitter

.PHONY : Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/build

Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/clean:
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/platforms/posix && $(CMAKE_COMMAND) -P CMakeFiles/jmavsim_tailsitter.dir/cmake_clean.cmake
.PHONY : Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/clean

Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/depend:
	cd /home/olliver/localbuild/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/olliver/localbuild/catkin_ws/src /home/olliver/localbuild/catkin_ws/src/Firmware/platforms/posix /home/olliver/localbuild/catkin_ws/build /home/olliver/localbuild/catkin_ws/build/Firmware/platforms/posix /home/olliver/localbuild/catkin_ws/build/Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Firmware/platforms/posix/CMakeFiles/jmavsim_tailsitter.dir/depend

