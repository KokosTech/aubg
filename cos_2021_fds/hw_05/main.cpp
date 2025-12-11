/* ============================
       Kaloyan Doychinov
        / 200 275 606 /
              &&
        Silvia Srebreva
        / 200 263 539 /
       COS 2021 A - FDS

        General Notes:
- Firstly we taught we should do it like a real graph - aka nodes pointing to other nodes,
  but for the solution of this project (and the algorithm provided in the lecture+wiki),
  it's much simpler using an adjacency list

- Choosing the built-in C++ container type - these were pretty useful
  https://stackoverflow.com/questions/22088607/what-is-the-difference-between-set-vs-map-in-c
  https://stackoverflow.com/questions/2196995/is-there-any-advantage-of-using-map-over-unordered-map-in-case-of-trivial-keys

- Checking results by hand - check /hand_solution_check directory

         Known bugs:
 !!!! C++20 IS REQUIRED !!!!
- just run: g++ main.cpp -std=c++20 -Wall -Wextra -Werror -Wpedantic
- doesn't properly work with non-connected graphs
  (centrality goes beyond 1 - dunno if that's correct)
============================ */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include "graph.hpp"

std::ifstream open_file() {
    std::ifstream input_file;

    while (true) {
        std::string filename;
        std::cout << "FILENAME: ";
        std::cin >> filename;

        if (!filename.empty()) {
            input_file.open(filename, std::ios::in);
            try {
                if (!input_file.is_open())
                    throw std::invalid_argument("File not found!");
                break;
            } catch (const std::invalid_argument &e) {
                std::cout << e.what() << std::endl;
            }
        }
        std::cout << std::endl;
    }

    return input_file;
}

template<typename T>
void read_graph_and_close(Graph<T> &graph, std::ifstream &input_file) {
    if (!input_file.is_open()) return;

    // U: V V V V....

    std::string line;
    while (std::getline(input_file, line)) {
        char node_value = line.at(0);

        std::string edgesPart = line.substr(2);
        std::stringstream edgesStream(edgesPart);
        std::string edgeValue;
        while (edgesStream >> edgeValue) {
            graph.add_edge(node_value, edgeValue.at(0));
        }
    }
    input_file.close();
}

int main() {
    Graph<char> graph;
    std::ifstream input_file = open_file();
    read_graph_and_close(graph, input_file);
    graph.graph_closeness();
    return 0;
}
