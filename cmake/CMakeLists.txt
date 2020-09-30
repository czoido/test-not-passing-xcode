
cmake_minimum_required(VERSION 2.8.12)
project(executable CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

add_executable(example main.cpp)
target_link_libraries(example CONAN_PKG::libD)
