/* ============================
       Kaloyan Doychinov
        / 200 275 606 /
              &&
        Silvia Srebreva
        / 200 263 539 /
       COS 2021 A - FDS

         Known bugs:
!!!! C++20 IS REQUIRED !!!!
============================ */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include "graph.hpp"

std::ifstream open_file() {
    std::ifstream inputFile;

    while (true) {
        std::string filename;
        std::cout << "FILENAME: ";
        std::cin >> filename;

        if (!filename.empty()) {
            inputFile.open(filename, std::ios::in);
            try {
                if (!inputFile.is_open())
                    throw std::invalid_argument("File not found!");
                break;
            } catch (const std::invalid_argument &e) {
                std::cout << e.what() << std::endl;
            }
        }
        std::cout << std::endl;
    }

    return inputFile;
}

// CHANGE !!!!!
template<typename T>
void read_graph_and_close(Graph<T> &graph, std::ifstream &inputFile) {
    std::string line;
    while (std::getline(inputFile, line)) {
        size_t colonPos = line.find(':');
        if (colonPos == std::string::npos) continue; // invalid line
        char nodeValue = line.at(0);
        std::string edgesPart = line.substr(2);

        std::istringstream edgesStream(edgesPart);
        std::string edgeValue;
        while (edgesStream >> edgeValue) {
            graph.add_edge(nodeValue, edgeValue.at(0));
        }
    }
    inputFile.close();
}

int main() {
    Graph<char> graph;
    std::ifstream inputFile = open_file();
    read_graph_and_close(graph, inputFile);
    graph.graph_closeness();
    return 0;
}
