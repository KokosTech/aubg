#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "The program expects a single argument <n>, to print all prime numbers until <n> (not incl.)" << std::endl;
        return -1;
    }

    long long unsafe_n = std::stoll(argv[1]); // firstly I was using `atoi`, but found out there's a CPP variant `stoi` -> `stoll` for long long
    if (unsafe_n < 1) {
        std::cerr << "The argument <n> mustn't be a non-positive number" << std::endl;
        return -1;
    }

    // magical number - max int size (if the compiler uses 4-bytes)
    if (unsafe_n > 2147483647) {
        std::cerr << "Please refrain from using numbers beyond the normal int" << std::endl;
        return -1;
    }

    int n = static_cast<int>(unsafe_n);
    std::vector<int> table(n); // was using `bool table[n];` but with large numbers (>100k) it was giving me a segfault -> vector is SLOWER!!!
    
    // technically, I could create a table without 0 and 1 (but 2x4bytes ain't gonna make a whole difference)
    std::fill_n(table.begin(), n, true);
    table[0] = false;
    table[1] = false;

    // ====== TIMING START ======
    int64_t sum = 0;
    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 2; i <= sqrt(n); ++i) {
        if (!table[i]) continue;

        for (int j = 2; i * j < n; ++j) {
            table[i * j] = false;
        }
	}

    // ====== TIMING END ======
    auto end = std::chrono::high_resolution_clock::now();

	for(int i = 2; i < n; ++i) {
		if(table[i]) std::cout << i << " ";
	}

    std::cout << std::endl;

    // ====== TIMING PRINT ======

    int64_t duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
    std::cout << "Duration " << duration << " ns" << std::endl;

    return 0;
}
