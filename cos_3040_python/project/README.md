# TrainSimPy

Short description to be written here :3 (1-2 paragraphs)

TrainSimPy is a COS3020 Project for bare-bones simulation of a train scheduling system. It includes a hierarchy of train
types alinged with the BDZ system of transportaion and train clasifications. It handles file persistency, simple cli
operations (such as adding and removing), displaying the loaded information, and the most important functionallity -
finding a route(s) from one station to another. You can imagie this project as bileti.bdz.bg - where you can find your
most stuitable ticket. The search has sorting and filtering.

**What does bare-bones mean?** - much of the functionallity (in my head) is not implemented due to time constraints and
other group projects, exams, assignments (and general lack of time). This project covers the requirements and implements
a search algorithm, and has everything interconnected within (which is quite complex due to the sheer amount of object
and cases you need to think of)

**Beware** - there can potentially be many logical errors

**Future development** - during the summer, a proper implementation (with all CRUD operations) as well as train-specific
functions such as booking, registering, etc, would be implemented

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

AI-Generated UML Diagram of the Project*

<img width="883" height="1294" alt="image" src="https://github.com/user-attachments/assets/cedb0f2f-a46e-441a-afb1-915a01a1e3ef" />

*Usually JetBrains PyCharm should be able to generate programatically a UML diagram but it kept failing on me, I tried
using different free AI models for generating a UML diagram from the source code - Claude kind of did it

## Search Algorithm

The search algorithm is implemented in 2 parts:

- if you're looking for a direct-route, it's going to just list all the possible direct routes and sort them by your
  preference
- if you're looking for a transfer route (1-2 transfers), it's using the abovementioned direct-route algorithm within
  a "handicapped" dfs search (limited by 1 or 2 transfers, otherwise it's going to get chaotic - a friend of mine
  working in BDZ did that mistake and the search for trains was broken for a couple of days). The dfs is then sorted by
  the preference of the user - it does not look for the shortest path - just looks for any possible path

## User Guide

### Installation

```
git clone https://github.com/KokosTech/aubg
cd cos_3040_python/project
pip install -r requirements.txt
```

### Getting Started

```
python main.py
```

### Running Tests

```
python -m unittest discover tests
```

```
coverage run -m unittest discover tests
coverage report -m
```

## Use of Generative AI

AI was used to generate all the json data for the rail network and trains (stored in the data folder). The built-in
functionality of PyCharm was used for assistance with suggesting in-line code improvements (just like in class and
during the exams).

**_Used AI tools:_**

- JetBrains AI (built-in functionality of PyCharm)
- Claude – for generating the json data for the rail network and trains
- Claude – for generating the "UML" diagram
- Claude – questions for some logic designs (to clear my ideas up and to check for inconsistency)

## Sources

- [Python Docs](https://docs.python.org/3.10/) – 3.10 as it's the one I'm using on my daily-driver
- [Coverage Docs](https://coverage.readthedocs.io/)
- StackOverflow
- Reddit
