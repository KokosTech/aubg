cmake_minimum_required(VERSION 3.29)
project(hw_03_trees)

set(CMAKE_CXX_STANDARD 17)

include_directories(.)

add_executable(hw_03_trees
    avl.hpp
    bst.hpp
    main.cpp
    node.hpp
    splay.hpp
    splay_nono.hpp)
