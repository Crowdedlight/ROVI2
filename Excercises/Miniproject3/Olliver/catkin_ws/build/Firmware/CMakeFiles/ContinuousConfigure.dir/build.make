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

# Utility rule file for ContinuousConfigure.

# Include the progress variables for this target.
include Firmware/CMakeFiles/ContinuousConfigure.dir/progress.make

Firmware/CMakeFiles/ContinuousConfigure:
	cd /home/olliver/localbuild/catkin_ws/build/Firmware && /usr/bin/ctest -D ContinuousConfigure

ContinuousConfigure: Firmware/CMakeFiles/ContinuousConfigure
ContinuousConfigure: Firmware/CMakeFiles/ContinuousConfigure.dir/build.make

.PHONY : ContinuousConfigure

# Rule to build all files generated by this target.
Firmware/CMakeFiles/ContinuousConfigure.dir/build: ContinuousConfigure

.PHONY : Firmware/CMakeFiles/ContinuousConfigure.dir/build

Firmware/CMakeFiles/ContinuousConfigure.dir/clean:
	cd /home/olliver/localbuild/catkin_ws/build/Firmware && $(CMAKE_COMMAND) -P CMakeFiles/ContinuousConfigure.dir/cmake_clean.cmake
.PHONY : Firmware/CMakeFiles/ContinuousConfigure.dir/clean

Firmware/CMakeFiles/ContinuousConfigure.dir/depend:
	cd /home/olliver/localbuild/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/olliver/localbuild/catkin_ws/src /home/olliver/localbuild/catkin_ws/src/Firmware /home/olliver/localbuild/catkin_ws/build /home/olliver/localbuild/catkin_ws/build/Firmware /home/olliver/localbuild/catkin_ws/build/Firmware/CMakeFiles/ContinuousConfigure.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Firmware/CMakeFiles/ContinuousConfigure.dir/depend

