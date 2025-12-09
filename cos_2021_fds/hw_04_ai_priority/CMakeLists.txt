cmake_minimum_required(VERSION 3.29)
project(hw_04_ai_priority)

set(CMAKE_CXX_STANDARD 17)

include_directories(.)

add_executable(hw_04_ai_priority
    main.cpp
    priority_queue.hpp
    test.hpp)
