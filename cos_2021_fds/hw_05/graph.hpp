#pragma once

#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
// #include <unordered_map>

template<typename T>
class Graph {
private:
    // here the usecase of a map is really important as the keys are always unique
    // and **ORDERED** which is important to implement the BFS as shown in class
    std::map<T, std::vector<T> > nodes;

public:
    void add_edge(T u, T v) {
        nodes[u].push_back(v);
    }

    int node_closeness(T start) {
        std::queue<T> queue;
        std::map<T, bool> explored;
        std::map<T, int> distance;

        // !!!! C++20 Feature !!!!
        if (!nodes.contains(start))
            return -1;

        queue.push(start);
        explored[start] = true;
        distance[start] = 0;

        while (!queue.empty()) {
            T cursor = queue.front();
            queue.pop();

            for (T edge: nodes[cursor]) {
                if (!explored[edge]) {
                    queue.push(edge);
                    explored[edge] = true;
                    distance[edge] = distance[cursor] + 1;
                }
            }
        }

        int total_distance = 0;
        for (auto [_, dist]: distance) {
            total_distance += dist;
        }

        return total_distance;
    }

    void graph_closeness() {
        std::map<T, double> closeness_map;
        int n = static_cast<int>(nodes.size());

        for (auto [node, _]: nodes) {
            double closeness = node_closeness(node);
            if (closeness == -1) continue;

            closeness_map[node] = static_cast<double>(n - 1) / closeness;
        }

        std::vector<std::pair<T, double> > sorted_closeness = sort_map(closeness_map);

        for (auto [node, closeness]: sorted_closeness) {
            std::cout << "Node " << node << " has closeness centrality of " << closeness << std::endl;
        }
    }

    // inspired by https://stackoverflow.com/a/19528891
    // first implementation used unordered_map, but the sorting was broken - no idea why
    std::vector<std::pair<T, double> > sort_map(std::map<T, double> &m) {
        // std::unordered_map<T, double> sorted_map;
        std::vector<std::pair<T, double> > vec(m.begin(), m.end());

        std::sort(vec.begin(), vec.end(), [](const auto &a, const auto &b) {
            return a.second > b.second;
        });

        // for (const auto &pair: vec) {
        //     sorted_map.insert(pair);
        // }
        // return sorted_map;

        return vec;
    }
};
