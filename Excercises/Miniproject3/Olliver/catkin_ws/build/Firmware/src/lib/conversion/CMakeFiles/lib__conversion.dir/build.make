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
include Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/depend.make

# Include the progress variables for this target.
include Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/progress.make

# Include the compile flags for this target's objects.
include Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/flags.make

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o: Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/flags.make
Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o: /home/olliver/localbuild/catkin_ws/src/Firmware/src/lib/conversion/rotation.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/olliver/localbuild/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/lib__conversion.dir/rotation.cpp.o -c /home/olliver/localbuild/catkin_ws/src/Firmware/src/lib/conversion/rotation.cpp

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/lib__conversion.dir/rotation.cpp.i"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/olliver/localbuild/catkin_ws/src/Firmware/src/lib/conversion/rotation.cpp > CMakeFiles/lib__conversion.dir/rotation.cpp.i

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/lib__conversion.dir/rotation.cpp.s"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/olliver/localbuild/catkin_ws/src/Firmware/src/lib/conversion/rotation.cpp -o CMakeFiles/lib__conversion.dir/rotation.cpp.s

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.requires:

.PHONY : Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.requires

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.provides: Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.requires
	$(MAKE) -f Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/build.make Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.provides.build
.PHONY : Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.provides

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.provides.build: Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o


# Object files for target lib__conversion
lib__conversion_OBJECTS = \
"CMakeFiles/lib__conversion.dir/rotation.cpp.o"

# External object files for target lib__conversion
lib__conversion_EXTERNAL_OBJECTS =

/home/olliver/localbuild/catkin_ws/devel/lib/liblib__conversion.a: Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o
/home/olliver/localbuild/catkin_ws/devel/lib/liblib__conversion.a: Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/build.make
/home/olliver/localbuild/catkin_ws/devel/lib/liblib__conversion.a: Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/olliver/localbuild/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library /home/olliver/localbuild/catkin_ws/devel/lib/liblib__conversion.a"
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion && $(CMAKE_COMMAND) -P CMakeFiles/lib__conversion.dir/cmake_clean_target.cmake
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lib__conversion.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/build: /home/olliver/localbuild/catkin_ws/devel/lib/liblib__conversion.a

.PHONY : Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/build

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/requires: Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/rotation.cpp.o.requires

.PHONY : Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/requires

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/clean:
	cd /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion && $(CMAKE_COMMAND) -P CMakeFiles/lib__conversion.dir/cmake_clean.cmake
.PHONY : Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/clean

Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/depend:
	cd /home/olliver/localbuild/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/olliver/localbuild/catkin_ws/src /home/olliver/localbuild/catkin_ws/src/Firmware/src/lib/conversion /home/olliver/localbuild/catkin_ws/build /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion /home/olliver/localbuild/catkin_ws/build/Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Firmware/src/lib/conversion/CMakeFiles/lib__conversion.dir/depend

