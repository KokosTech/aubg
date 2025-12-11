#include <iostream>
#include <fstream>
#include <vector>
#include <map>

template<typename T>
class Graph {
private:
    // here the usecase of a map is really important as the keys are always unique
    // and **ORDERED** which is important to implement the BST as shown in class
    std::map<T, std::vector<T> > nodes;

public:
    void add_edge(T u, T v) {
        nodes[u].push_back(v);
    }

    int node_closeness(T start) {
        std::queue<T> queue;
        std::map<T, bool> explored;
        std::map<T, int> distance;

        // !! C++20 Feature !!
        if (!nodes.contains(start))
            return -1;

        queue.push(start);
        explored[start] = true;
        distance[start] = 0;

        while (!queue.empty()) {
            T cursor = queue.front();
            queue.pop();

            for (auto edge: nodes[cursor]) {
                if (!explored[edge]) {
                    distance[edge] = distance[cursor] + 1;
                    explored[edge] = true;
                    queue.push(edge);
                }
            }
        }

        int total_distance = 0;
        for (auto i: distance) {
            total_distance += i.second;
        }

        return total_distance;
    }

    void graph_closeness() {
        std::map<T, double> closeness;
        int n = static_cast<int>(nodes.size());

        for (auto i: nodes) {
            closeness[i.first] = static_cast<double>(n - 1) / node_closeness(i.first);
        }

        std::unordered_map<T, double> sorted_closeness = sort_map(closeness);

        for (auto i: sorted_closeness) {
            std::cout << "Node " << i.first << " has closeness " << i.second << std::endl;
        }
    }

    // inspired by https://stackoverflow.com/a/19528891 but in a different implementation
    // unordered_map since we want it sorted by the value, not the key (could use a list, but it compromises on the key constraint)
    std::unordered_map<T, double> sort_map(std::map<T, double> &m) {
        std::unordered_map<T, double> sorted_map;
        std::vector<std::pair<T, double> > vec(m.begin(), m.end());
        std::sort(vec.begin(), vec.end(), [](const auto &a, const auto &b) {
            return a.second < b.second;
        });
        for (const auto &pair: vec) {
            sorted_map.insert(pair);
        }

        return sorted_map;
    }
};

//
// #define spr std::shared_ptr
//
// template<typename T>
// struct GraphNode {
//     T data;
//     std::vector<spr<GraphNode> > edges;
//     bool visited = false;
//
//     GraphNode() = default;
//
//     GraphNode(T data) {
//         this.data = data;
//     }
// };
//
// template<typename T>
// class Graph {
// public:
//     spr<GraphNode<T> > start = nullptr;
//
//     void load_file(std::ifstream inputFile) {
//         while (true) {
//             std::string filename;
//             std::cout << "FILENAME: ";
//             std::cin >> filename;
//
//             if (!filename.empty()) {
//                 inputFile.open(filename, std::ios::in);
//                 try {
//                     if (!inputFile.is_open())
//                         throw std::invalid_argument("File not found!");
//                     break;
//                 } catch (const std::invalid_argument &e) {
//                     std::cout << e.what() << std::endl;
//                 }
//             }
//             std::cout << std::endl;
//         }
//
//         // process file
//
//         /* example input file:
//         A: B
//         B: A C D
//         C: B
//         D: B
//         */
//
//         // process file start
//
//         std::string line;
//         while (std::getline(inputFile, line)) {
//             size_t colonPos = line.find(':');
//             if (colonPos == std::string::npos) continue; // invalid line
//             std::string nodeValue = line.substr(0, colonPos);
//             std::string edgesPart = line.substr(colonPos + 1);
//
//             if (!find(nodeValue)) {
//                 spr<GraphNode<T>> new_node = std::make_shared<GraphNode<T> >(nodeValue);
//             }
//
//             std::istringstream edgesStream(edgesPart);
//             std::string edgeValue;
//             while (edgesStream >> edgeValue) {
//                 if (nodes.find(edgeValue) == nodes.end()) {
//                     nodes[edgeValue] = std::make_shared<GraphNode<T> >(edgeValue);
//                 }
//                 connect_nodes(nodes[nodeValue], nodes[edgeValue]);
//             }
//         }
//
//
//         inputFile.close();
//     }
//
//     void add_node(T value) {
//         spr<GraphNode<T> > new_node = std::make_shared<GraphNode<T> >(value);
//     }
//
//     // aka add edge
//     void connect_nodes(spr<GraphNode<T> > src, spr<GraphNode<T> > dest) {
//         if (!src && !dest) return;
//         src->edges.push_back(dest);
//     }
//
//     // test bfs function (before implementing closeness)
//     void find_node(T value) {
//     }
//
//     // actual algorithm
//     void graph_closeness() {
//     }
//
//     Graph() = default;
//
//     Graph(GraphNode<T> gn) {
//         this->start = gn;
//     }
// };
//
