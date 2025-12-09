/* ============================
       Kaloyan Doychinov
        / 200 275 606 /
       COS 2021 A - FDS
       / In-Class Ex /
============================ */

#include <iostream>
#include <fstream>
#include <string>
#include <valarray>
#include <cmath>

// imagine it's a 1000 element hash table
#define HT_SIZE 1000

size_t hash_1(std::string str) {
    size_t hash = 0;
    size_t len = str.length();

    for (size_t i = 0; i < len; ++i)
        hash += str[i];

    return hash;
}

size_t hash_2(std::string str) {
    size_t hash = 0xCBF29CE48422232UL;
    size_t len = str.length();

    for (size_t i = 0; i < len; ++i) {
        hash ^= str[i];
        hash *= 0x100000001B3UL;
    }

    return hash;
}

size_t hash_3(std::string str) {
    size_t hash = 5381;
    size_t len = str.length();

    for (size_t i = 0; i < len; ++i) {
        hash = (hash << 5) + hash;
        hash += str[i];
    }

    return hash;
}

double calc_std(size_t *ht, size_t word_count) {
    double mean = word_count / static_cast<double>(HT_SIZE);
    double sum = 0;

    for (int i = 0; i < HT_SIZE; ++i) {
        sum += pow((ht[i] - mean), 2);
    }

    return sqrt(sum / static_cast<double>(HT_SIZE));
}

int main(int argc, char **argv) {
    if (argc < 2) {
        std::cerr << "File please :/\n";
        return -1;
    }

    std::string filename = argv[1];
    std::ifstream inputFile(filename, std::ios::in);

    if (!inputFile.is_open()) {
        std::cerr << "Valid file please :/\n";
        return -2;
    }

    size_t ht1[HT_SIZE], ht2[HT_SIZE], ht3[HT_SIZE];

    std::fill_n(ht1, HT_SIZE, 0);
    std::fill_n(ht2, HT_SIZE, 0);
    std::fill_n(ht3, HT_SIZE, 0);


    std::string word;
    size_t word_count = 0;
    while (inputFile >> word) {
        ++ht1[hash_1(word) % HT_SIZE];
        ++ht2[hash_2(word) % HT_SIZE];
        ++ht3[hash_3(word) % HT_SIZE];
        ++word_count;
    }

    std::cout << "STD 1 -> " << calc_std(ht1, word_count) << std::endl;
    std::cout << "STD 2 -> " << calc_std(ht2, word_count) << std::endl;
    std::cout << "STD 3 -> " << calc_std(ht3, word_count) << std::endl;

    return 0;
}
