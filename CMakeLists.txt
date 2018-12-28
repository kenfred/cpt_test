cmake_minimum_required(VERSION 3.7)
project(CptTest)

add_library(cpt_test ${CMAKE_CURRENT_SOURCE_DIR}/Foo.cpp)
target_include_directories(cpt_test PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
