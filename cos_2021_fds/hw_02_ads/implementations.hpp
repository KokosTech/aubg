#pragma once

#include <memory>
#include <optional>

#include "interfaces.hpp"

// FIFO (First in, First out)
template <typename T>
class Queue : public IContainer<T> {
   private:
    std::shared_ptr<Node<T>> start;
    std::shared_ptr<Node<T>> end;

   public:
    Queue() : start(nullptr), end(nullptr) {}

    void Add(T t) {
        std::shared_ptr<Node<T>> new_node = std::make_shared<Node<T>>(t);
        new_node->next = nullptr;

        if (!this->start && !this->end) {
            this->start = new_node;
            this->end = this->start;
        } else {
            this->end->next = new_node;
            this->end = this->end->next;
        }
    }

    std::optional<T> Remove() {
        if(!this->start) return std::nullopt;

        T copy_removed = this->start->data;
        this->start = this->start->next;
        return copy_removed;
    }

    std::optional<T> Peek() {
        if (!this->start) return std::nullopt;
        return this->start->data;
    }
};

// LIFO (Last in, First out)
template <typename T>
class Stack : public IContainer<T> {
private:
    std::shared_ptr<Node<T>> top;
public:
    Stack() : top(nullptr) {}

    void Add(T t) {
        std::shared_ptr<Node<T>> new_node = std::make_shared<Node<T>>(t);
        new_node->next = this->top;
        this->top = new_node;
    }

    std::optional<T> Remove() {
        if (!this->top) return std::nullopt;

        T copy_removed = this->top->data;
        this->top = this->top->next;
        return copy_removed;
    }

    std::optional<T> Peek() {
        if (!this->top) return std::nullopt;
        return this->top->data;
    }
};