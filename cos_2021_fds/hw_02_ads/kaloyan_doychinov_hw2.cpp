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

    Stack<std::shared_ptr<Queue<std::string> > > decode_stack;
    std::shared_ptr<Queue<std::string> > word_queue = nullptr;

    std::ifstream inputFile("code.txt", std::ios::in);
    try {
        if (!inputFile.is_open())
            throw std::invalid_argument("File not found!");
    } catch (const std::invalid_argument &e) {
        std::cout << e.what() << std::endl;
        return -1;
    }

    char ch;
    while (inputFile >> std::noskipws >> ch) {
        character_queue.Add(std::string{ch});
    }


    std::optional<std::string> cur = character_queue.Remove();
    // std::cout << "KYS " << !cur << cur.has_value() << cur.value() << std::endl;
    while (cur && cur.has_value() && cur.value() != "") {
        // std::cout << "DEBUG:" << cur.value() << ":DEBUG" << std::endl;
        // std::cout << word_queue << std::endl;
        // Perfect ^
        if (cur.value() == "(") {
            auto new_word_queue =
                    std::make_shared<Queue<std::string> >();

            if (word_queue && word_queue->Peek() != std::nullopt) {
                decode_stack.Add(word_queue);
            }

            word_queue = new_word_queue;


        } else if (cur.value() == ")") {
            std::string word = "";
            std::optional<std::string> cur2 = word_queue->Remove();
            while (cur2 && cur2.has_value()) {
                word.append(cur2.value());
                cur2 = word_queue->Remove();
            }

            sentence_queue.Add(word);

            if(decode_stack.Peek() != std::nullopt) {
                std::optional<std::shared_ptr<Queue<std::string>>> tobe = decode_stack.Remove();
                word_queue = tobe.value();
            }
        } else {
            // std::cout << "KY";
            word_queue->Add(cur.value());
            // std::cout << "P";
        }
        cur = character_queue.Remove();
    }

    std::optional<std::string> cur3 = sentence_queue.Remove();
    std::cout << "======= Result =======\n";
    while (cur3 && cur3.has_value()) {
        std::cout << cur3.value() << " ";
        cur3 = sentence_queue.Remove();
    }

    std::cout << std::endl;

    return 0;
}
