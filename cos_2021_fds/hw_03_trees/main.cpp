#include <iostream>

#include "splay.hpp"

int main() {
    Splay<int> tree;
    tree.insert(10);
    tree.insert(20);
    tree.insert(30);
    tree.insert(40);
    tree.insert(50);
    tree.print();
    std::cout << "Find 30 at depth: " << tree.find(30) << std::endl;
    tree.print();
    std::cout << "Find 10 at depth: " << tree.find(10) << std::endl;
    tree.print();
    return 0;
}