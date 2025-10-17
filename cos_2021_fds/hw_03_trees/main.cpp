#include <iostream>

#include "splay.hpp"

int main() {
    Splay<int> tree;
    tree.insert(30);
    std::cout << "========30=========\n";
    tree.print();
    std::cout << "==================\n";
    tree.insert(20);
    std::cout << "========20=========\n";
    tree.print();
    std::cout << "==================\n";
    tree.insert(40);
    std::cout << "========40=========\n";
    tree.print();
    std::cout << "==================\n";
    tree.insert(10);
    std::cout << "========10=========\n";
    tree.print();
    std::cout << "==================\n";
    tree.insert(5);
    std::cout << "========5=========\n";
    tree.print();
    std::cout << "==================\n";
    tree.insert(50);
    std::cout << "========50=========\n";
    tree.print();
    std::cout << "==================\n";
    std::cout << "Find 30 at depth: " << tree.find(30) << std::endl;
    std::cout << "==================\n";
    tree.print();
    std::cout << "Find 10 at depth: " << tree.find(10) << std::endl;
    tree.print();


    // tree.insert(1);
    // tree.insert(3);
    // tree.insert(2);
    // tree.print();
    // tree.find(3);
    // tree.print();
    // tree.insert(4);
    // tree.find(1);
    // tree.print();
    // tree.insert(10);
    // tree.print();
    // tree.find(2);
    // tree.print();
    return 0;
}