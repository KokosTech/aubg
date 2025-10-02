/* ============================
       Kaloyan Doychinov
       COS 2021 A - FDS
============================ */

#include <iostream>
#include <optional>
#include "implementations.hpp"

int main() {
       Queue<int> queue;
       queue.Add(3);
       queue.Add(6);
       queue.Add(5);

       std::optional<int> a = queue.Remove();
       std::optional<int> b = queue.Remove();
       std::optional<int> c = queue.Remove();
       std::optional<int> d = queue.Remove();

       int ac = a.has_value() ? a.value() : 0;
       int bc = b.has_value() ? b.value() : 0;
       int cc = c.has_value() ? c.value() : 0;
       int dc = c.has_value() ? c.value() : 0;

       std::cout << ac << bc << cc << dc;

       return 0;
}