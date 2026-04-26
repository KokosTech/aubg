# TrainSimPy

Short description to be written here :3 (1-2 paragraphs)

## File Structure

    project:
        - data - used to store files for input and persistency for the railway network and trains
        - models - used for all classes and data classes in the program
            - rail - package which includes all classes for the rail network, such as:
                - track.py - TODO ...
                - train_station.py - TODO ...
                - rail_network.py - TODO ...
            - trains - package including all train types
                - helper - package including any 'has-a' classes for the trains
                    - carriage.py - TODO ...
                    - carriage_types.py - TODO ...
                    - stop.py - TODO ...
                - base.py - TODO ...
                - passenger.py - TODO ...
                - intercity.py - TODO ...
                - intercity_express.py - TODO ...
            - services - package containing the logic of the project - the actual simulation
                - train_sim.py - TODO ...
                - validate_train_schedule.py - TODO ...

        - utils - package including core project scripts, such as:
            - config.py - parses configuration file
            - menu.py - handles the the user input as well as the CLI interface
            - time_to_string.py - helper function used across the project to convert tuple (int, int) or just a single int to a formatted time string
        - tests - package including all tests for this project
        
        main.py - starter of the whole project
        .coveragerc - prevents test files to be included in the coverage report 
        .gitignore - prevents cache and secret files from being committed by accident
        config.ini - usually should not be included in a project source code (aka git) as it may include sensitive information, in this case it's just easier for setup
        requirements.txt - includes all dependencies (packages) to be installed before running the program

## Class Structure


```
    ===============================================
    BaseTrain - abstract class for all trains
        - PassengerTrain - concrete implementation of BaseTrain
            - IntercityTrain - implementation over PassengerTrain - upgraded service of PassengerTrain
                - IntercityExpressTrain - implementation over IntercityTrain - upgraded service of IntercityTrain
    Carriage - has-a relationship with BaseTrain
    Stop - has-a relationship with BaseTrain - represents stations with arrival and departure times
    ===============================================
    RailNetwork - class for the rail network - used to represent the rail network (graph)
    TrainStation - has-a relationship with RailNetwork - used to represent the train stations (nodes)
    Track - has-a relationship with RailNetwork - used to represent the tracks between train stations (edges)
    ===============================================
    TrainSim - class for the train simulation
    Journey - has-a relationship with TrainSim
    ===============================================
    Time - dataclass for handling time
    ===============================================
```

## Special Functions & Algorithms

### Search Algorithm

### Other Things - to be thought of what's actually important

## User Guide

### Installation

how to clone repo, go to project folder, and install required packages

### Getting Started

how to setup config (optional), how to input data files (optional)

### Video

[copy paste from requirements]

o First you should run your project and explain in short what your project is doing (e.g. if there is a menu with different options you should show if any of the options are chosen what would be the result etc).

o After you have shown that your project works, you should open the code and go through the classes/methods and show and explain how each of the requirements was implemented in your project.

o Then you should run the unit tests to show that they pass.

o Finally run the coverage and show the coverage report.

## Use of Generative AI

To be written
