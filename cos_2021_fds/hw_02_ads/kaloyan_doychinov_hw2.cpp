/* ============================
       Kaloyan Doychinov
       COS 2021 A - FDS
============================ */

#include <fstream>
#include <iostream>
#include <memory>
#include <optional>

#include "implementations.hpp"

int main() {
    Queue<std::string> character_queue;
    Queue<std::string> sentence_queue;
    Stack<std::shared_ptr<Queue<std::string>>> decode_stack;

    std::shared_ptr<Queue<std::string>> word_queue = nullptr;

    // read a sentence from the input file
    std::ifstream inputFile("code.txt", std::ios::in);
    try {
        if (!inputFile.is_open())
            throw std::invalid_argument("File not found!");
    } catch (const std::invalid_argument& e) {
        std::cout << e.what() << std::endl;
        return -1;
    }

    char ch;
    while (inputFile >> std::noskipws >> ch) {
        std::cout << ch;
        character_queue.Add(std::string(ch, std::(c)));
    }

    std::optional<std::string> cur = character_queue.Remove();
    std::cout << "KEBUG:" << cur.value() << ":DEBUG" << std::endl;
    while (!cur && (cur.has_value() || cur.value() != "")) {
        std::cout << "DEBUG:" << cur.value() << ":DEBUG" << std::endl;
        if (cur.value() == "(") {
            std::shared_ptr<Queue<std::string>> new_word_queue =
                std::make_shared<Queue<std::string>>();
            if (word_queue->Peek() != std::nullopt) {
                decode_stack.Add(word_queue);
                word_queue = new_word_queue;
            }
        } else if (cur.value() == ")") {
            std::string word = "";
            std::optional<std::string> cur2 = word_queue->Remove();
            while (!cur2 && cur2.has_value()) {
                word.append(cur2.value());
                cur2 = word_queue->Remove();
            }
            sentence_queue.Add(word);
        } else {
            word_queue->Add(cur.value());
        }
        cur = character_queue.Remove();
    }

    std::optional<std::string> cur3 = sentence_queue.Remove();
    // std::cout << "AAAAA";
    while (!cur3 && cur3.has_value()) {
        std::cout << cur3.value() << " ";
    }

    std::cout << std::endl;

    return 0;
}