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
    int dc = d.has_value() ? d.value() : 0;

    std::cout << ac << bc << cc << dc << std::endl;

    Stack<int> stack;
    stack.Add(3);
    stack.Add(6);
    stack.Add(5);

    std::optional<int> as = stack.Remove();
    std::optional<int> bs = stack.Remove();
    std::optional<int> cs = stack.Remove();
    std::optional<int> ds = stack.Remove();

    int asc = as.has_value() ? as.value() : 0;
    int bsc = bs.has_value() ? bs.value() : 0;
    int csc = cs.has_value() ? cs.value() : 0;
    int dsc = ds.has_value() ? ds.value() : 0;

    std::cout << asc << bsc << csc << dsc;

    return 0;
}