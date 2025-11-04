/* ============================
       Kaloyan Doychinov
        / 200 275 606 /
       COS 2021 A - FDS

         Known bugs:
- there were a lot in the
beginning but I think I've
fixed them all (hopefully)
============================ */

#include <iostream>
#include <random>
#include <vector>
#include <algorithm>

#include "avl.hpp"
#include "bst.hpp"
#include "splay.hpp"

#define TEST_RUNS 100000.00

int main() {
    AvlTree<int> avl_tree;
    BST<int> bst_tree;
    Splay<int> splay_tree;

    // https://en.cppreference.com/w/cpp/numeric/random/random_device.html
    std::random_device dev;
    //chose this one because it caught my eye (and was in the examples given)
    std::mt19937 rng(dev()); // "the longest non-repeating sequence"
    std::uniform_int_distribution<std::mt19937::result_type> dist6(0, 1000);

    // test 1

    for (int i = 0; i <= 1000; ++i) {
        avl_tree.insert(i);
        bst_tree.insert(i);
        splay_tree.insert(i);
    }

    unsigned long long avl_sum_depth = 0;
    unsigned long long bst_sum_depth = 0;
    unsigned long long splay_sum_depth = 0;

    for (int i = 0; i < (int) TEST_RUNS; ++i) {
        int rnd_num_to_find = static_cast<int>(dist6(rng));

        avl_sum_depth += avl_tree.find(rnd_num_to_find);
        bst_sum_depth += bst_tree.find(rnd_num_to_find);
        splay_sum_depth += splay_tree.find(rnd_num_to_find);
    }

    // numbers were unreadable, so some formatting is great to have
    // firstly, it wasn't working but - https://stackoverflow.com/questions/20352438/printf-output-not-affected-by-global-locale
    std::locale::global(std::locale("en_US.UTF-8"));
    std::cout.imbue(std::locale());

    std::cout << "========== TEST 1 ==========" << std::endl;
    std::cout << "AVL AVG DEPTH -> " << avl_sum_depth / TEST_RUNS << std::endl;
    std::cout << "BST AVG DEPTH -> " << bst_sum_depth / TEST_RUNS << std::endl;
    std::cout << "SPLAY AVG DEPTH -> " << splay_sum_depth / TEST_RUNS << std::endl;
    std::cout << "============================" << std::endl;

    // test 2

    AvlTree<int> new_avl_tree;
    BST<int> new_bst_tree;
    Splay<int> new_splay_tree;

    // i wasted way too much time for this random order
    // firstly implemented my own function, then a set,
    // and now im back to vector + shuffle (didn't know it existed)
    std::vector<int> numbers;
    for (int i = 0; i <= 1000; ++i)
        numbers.push_back(i);
    std::shuffle(numbers.begin(), numbers.end(), rng);

    for (int num: numbers) {
        new_avl_tree.insert(num);
        new_bst_tree.insert(num);
        new_splay_tree.insert(num);
    }

    avl_sum_depth = 0;
    bst_sum_depth = 0;
    splay_sum_depth = 0;

    for (int i = 0; i < (int) TEST_RUNS; ++i) {
        int rnd_num_to_find = static_cast<int>(dist6(rng));

        avl_sum_depth += new_avl_tree.find(rnd_num_to_find);
        bst_sum_depth += new_bst_tree.find(rnd_num_to_find);
        splay_sum_depth += new_splay_tree.find(rnd_num_to_find);
    }

    // fun fact - BST now improves times 50 - why - because it's normal insertion and it's not just a linked list
    // avl suffers a bit but it's still the best
    // splay - is the worst one here - but it's still close to AVL (by 20% slower)
    //      - reason - it's optimized for frequent access, and not access to all nodes
    std::cout << "========== TEST 2 ==========" << std::endl;
    std::cout << "AVL AVG DEPTH -> " << avl_sum_depth / TEST_RUNS << std::endl;
    std::cout << "BST AVG DEPTH -> " << bst_sum_depth / TEST_RUNS << std::endl;
    std::cout << "SPLAY AVG DEPTH -> " << splay_sum_depth / TEST_RUNS << std::endl;
    std::cout << "============================" << std::endl;

    return 0;
}
