#pragma once

#include<memory>
#include<optional>

/***
    Node class
    - A standard node class with a data element
        and a pointer to the next Node.
    - For use in a singly-linked list, for example.
*/
template<typename T>
class Node {
public:
    Node() {}
    Node(T t) {
        data = t;
        next = nullptr;
    }
    bool operator==(const T & t) {
        return data == t;
    }
    T data;
    std::shared_ptr<Node<T>> next;
};

/***
    IContainer Class
    - An abstract class with basic container functions.
    - Add should add t to the container such that the size of the
        container's contents grows by one.
    - Remove, should remove the "first" or "next" item from
        the container and return an optional to it.
        If the container is empty, a nullopt should be
        returned.
    - Peek, should return an optional of the next element in the
        container without removing it from the container.
 */
template<typename T>
class IContainer {
public:
    virtual void Add(T t) = 0;
    virtual std::optional<T> Remove() = 0;
    virtual std::optional<T> Peek() = 0;
};