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

# Include any dependencies generated for this target.
include Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/depend.make

# Include the progress variables for this target.
include Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/progress.make

# Include the compile flags for this target's objects.
include Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/flags.make

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o: Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/flags.make
Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o: /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/distance_sensor/srf02_i2c/srf02_i2c.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/olliver/localbuild/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o -c /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/distance_sensor/srf02_i2c/srf02_i2c.cpp

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.i"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/distance_sensor/srf02_i2c/srf02_i2c.cpp > CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.i

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.s"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/distance_sensor/srf02_i2c/srf02_i2c.cpp -o CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.s

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.requires:

.PHONY : Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.requires

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.provides: Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.requires
	$(MAKE) -f Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/build.make Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.provides.build
.PHONY : Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.provides

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.provides.build: Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o


# Object files for target drivers__srf02_i2c
drivers__srf02_i2c_OBJECTS = \
"CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o"

# External object files for target drivers__srf02_i2c
drivers__srf02_i2c_EXTERNAL_OBJECTS =

/home/olliver/localbuild/catkin_ws/devel/lib/libdrivers__srf02_i2c.a: Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o
/home/olliver/localbuild/catkin_ws/devel/lib/libdrivers__srf02_i2c.a: Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/build.make
/home/olliver/localbuild/catkin_ws/devel/lib/libdrivers__srf02_i2c.a: Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/olliver/localbuild/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library /home/olliver/localbuild/catkin_ws/devel/lib/libdrivers__srf02_i2c.a"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c && $(CMAKE_COMMAND) -P CMakeFiles/drivers__srf02_i2c.dir/cmake_clean_target.cmake
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/drivers__srf02_i2c.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/build: /home/olliver/localbuild/catkin_ws/devel/lib/libdrivers__srf02_i2c.a

.PHONY : Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/build

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/requires: Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/srf02_i2c.cpp.o.requires

.PHONY : Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/requires

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/clean:
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c && $(CMAKE_COMMAND) -P CMakeFiles/drivers__srf02_i2c.dir/cmake_clean.cmake
.PHONY : Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/clean

Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/depend:
	cd /home/olliver/localbuild/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/olliver/localbuild/catkin_ws/src /home/olliver/localbuild/catkin_ws/src/Firmware/src/drivers/distance_sensor/srf02_i2c /home/olliver/localbuild/catkin_ws/build /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c /home/olliver/localbuild/catkin_ws/build/Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Firmware/src/drivers/distance_sensor/srf02_i2c/CMakeFiles/drivers__srf02_i2c.dir/depend

