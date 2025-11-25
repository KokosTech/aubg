/* ============================
          Open AI
        / Chat GPT /
       COS 2021 A - FDS

         Known bugs:
- everything down this comment
is AI generated - that buggs us
============================ */

#pragma once

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
using namespace std;

template<typename T>
class PriorityQueue {
private:
    vector<T> heap;

    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[index] < heap[parent]) {
                swap(heap[index], heap[parent]);
                index = parent;
            } else {
                break;
            }
        }
    }

    void heapifyDown(int index) {
        int size = heap.size();
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int smallest = index;

            if (left < size && heap[left] < heap[smallest])
                smallest = left;
            if (right < size && heap[right] < heap[smallest])
                smallest = right;

            if (smallest != index) {
                swap(heap[index], heap[smallest]);
                index = smallest;
            } else {
                break;
            }
        }
    }

    int findIndex(const T &value) {
        for (int i = 0; i < heap.size(); i++) {
            if (heap[i] == value)
                return i;
        }
        return -1;
    }

public:
    void Add(T t) {
        heap.push_back(t);
        heapifyUp(heap.size() - 1);
    }

    void Delete(T t) {
        int index = findIndex(t);
        if (index == -1) return;
        heap[index] = heap.back();
        heap.pop_back();
        if (index < heap.size()) {
            heapifyUp(index);
            heapifyDown(index);
        }
    }

    T DeleteMin() {
        if (heap.empty())
            throw runtime_error("Heap is empty");
        T minVal = heap.front();
        heap[0] = heap.back();
        heap.pop_back();
        if (!heap.empty())
            heapifyDown(0);
        return minVal;
    }

    void IncreaseKey(T t, T amount) {
        if (amount < 0) return;
        int index = findIndex(t);
        if (index == -1) return;
        heap[index] += amount;
        heapifyDown(index);
    }

    void DecreaseKey(T t, T amount) {
        if (amount < 0) return;
        int index = findIndex(t);
        if (index == -1) return;
        heap[index] -= amount;
        heapifyUp(index);
    }

    void print() {
        for (T val: heap)
            cout << val << " ";
        cout << endl;
    }

    vector<T> getArray() const {
        return heap;
    }

    bool isEmpty() const {
        return heap.empty();
    }

    T getMin() const {
        if (heap.empty())
            throw runtime_error("Heap is empty");
        return heap.front();
    }

    T getMax() const {
        if (heap.empty())
            throw runtime_error("Heap is empty");
        return *max_element(heap.begin(), heap.end());
    }
};
