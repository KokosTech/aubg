#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

unsigned long long COUNTER = 0;

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

    for (int i = 2; i <= sqrt(n); ++i) {
        if (!table[i]) {
            ++COUNTER; // count +1 if we're not running the next void loop()
            continue;
        };

        for (int j = 2; i * j < n; ++j) {
            table[i * j] = false;
            ++COUNTER; // count +1 in the inner most loop
        }
	}

	for(int i = 2; i < n; ++i) {
		if(table[i]) std::cout << i << " ";
	}

    std::cout << std::endl;

    // ====== COUNTER ======
    std::cout << "COUNTER: " << COUNTER << std::endl;

	return 0;
}
