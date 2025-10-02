/* ============================
       Kaloyan Doychinov
        / 200 275 606 /
       COS 2021 A - FDS

         Known bugs:
- for the program - I haven't
found any (probably there are)
- for me - this time, I had to
use an IDE, couldn't bare not
seeing the methods & attributes
============================ */

#include <fstream>
#include <iostream>
#include <memory>
#include <optional>

#include "implementations.hpp"

static const std::string INPUT_FILE = "code.txt";

int main() {
    Queue<std::string> character_queue;
    Queue<std::string> sentence_queue;

    Stack<std::shared_ptr<Queue<std::string> > > decode_stack;
    std::shared_ptr<Queue<std::string> > word_queue = nullptr;

    // Input Data

    std::ifstream inputFile(INPUT_FILE, std::ios::in);
    try {
        if (!inputFile.is_open())
            throw std::invalid_argument("File not found!");
    } catch (const std::invalid_argument &e) {
        std::cout << e.what() << std::endl;
        return -1;
    }

    char ch;
    while (inputFile >> std::noskipws >> ch) {
        // stackoverflow helped on the char to str conversion - https://stackoverflow.com/questions/17201590/how-can-i-create-a-string-from-a-single-character
        character_queue.Add(std::string{ch});
    }

    inputFile.close();

    // Actual Logic

    std::optional<std::string> cur = character_queue.Remove();
    while (cur && cur.has_value() && cur.value() != "") {
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

            if (decode_stack.Peek() != std::nullopt) {
                std::optional<std::shared_ptr<Queue<std::string> > > tobe = decode_stack.Remove();
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
