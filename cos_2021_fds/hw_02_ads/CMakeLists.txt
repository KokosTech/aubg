cmake_minimum_required(VERSION 3.29)
project(hw_02_ads)

set(CMAKE_CXX_STANDARD 17)

include_directories(.)

add_executable(
    hw_02_ads
    implementations.hpp
    interfaces.hpp
    kaloyan_doychinov_hw2.cpp)
