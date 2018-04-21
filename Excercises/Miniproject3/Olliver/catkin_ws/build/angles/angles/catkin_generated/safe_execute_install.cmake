execute_process(COMMAND "/home/olliver/localbuild/catkin_ws/build/angles/angles/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/olliver/localbuild/catkin_ws/build/angles/angles/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
