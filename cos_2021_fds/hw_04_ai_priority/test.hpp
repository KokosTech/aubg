/* ============================
        Silvia Srebreva
        / 200 263 539 /
              &&
       Kaloyan Doychinov
        / 200 275 606 /
       COS 2021 A - FDS

         Known bugs:
            ----
============================ */

#pragma once

#include <cassert>
#include <iostream>
#include <string>

#include "priority_queue.hpp"

#define NO_TESTS 22

class TestPriorityQueue {
private:
    PriorityQueue<int> pq;
    int passed = 0;
    int total = 0;

    void verifyAndPrint(std::string const &testName, int result, int expected) {
        total++;
        if (result == expected) {
            printf("[%d|%d] ✅passed %s\n", total, NO_TESTS, testName.c_str());
            passed++;
        } else {
            printf("[%d|%d] ❌failed %s -> expected: %d; output: %d\n", total, NO_TESTS, testName.c_str(), expected, result);
        }
    }

    bool compareArrays(const std::vector<int> &a, const std::vector<int> &b) {
        if (a.size() != b.size()) return false;
        for (size_t i = 0; i < a.size(); ++i) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }

    void test_insertion() {
        pq.Add(10);
        verifyAndPrint("test insertion of 10 w/getMin", pq.getMin(), 10);
        verifyAndPrint("test insertion of 10 w/getMax", pq.getMax(), 10);
    }

    void test_get_min() {
        pq.Add(5);
        pq.Add(20);
        verifyAndPrint("test getMin after inserting 5, 20", pq.getMin(), 5);
    }

    void test_get_max() {
        pq.Add(30);
        verifyAndPrint("test getMac after inserting 30", pq.getMax(), 30);
    }

    void test_decrease_key() {
        this->pq.DecreaseKey(10, 6);
        verifyAndPrint("test getMin after decreaseKey", pq.getMin(), 4);
    }

    void test_increase_key() {
        this->pq.IncreaseKey(4, 3);
        verifyAndPrint("test getMin after increaseKey", pq.getMin(), 5);
    }

    void test_delete_min() {
        verifyAndPrint("test deleteMin value", pq.DeleteMin(), 5);
        verifyAndPrint("test getMin after deleteMin", pq.getMin(), 7);
    }

    void test_delete() {
        pq.Delete(30);
        verifyAndPrint("test delete on 30 w/getMax", pq.getMax(), 20);
    }

    void test_delete_non_existent() {
        // here we should have 7 and 20 left
        pq.Delete(4);
        pq.Delete(8);
        verifyAndPrint("test delete on 4 & 8 (not present in PQ) w/getMin", pq.getMin(), 7);
        verifyAndPrint("test delete on 4 & 8 (not present in PQ) w/getMax", pq.getMax(), 20);
        vector<int> heap_to_test = pq.getArray();
        verifyAndPrint("test delete on 4 & 8 (not present in PQ) w/array comparison", compareArrays(heap_to_test, vector<int>{7, 20}), true);
    }

    void test_increase_key_non_existent() {
        pq.IncreaseKey(100, 5); // should do nothing
        verifyAndPrint("test increaseKey on 100 (not present in PQ) w/getMax", pq.getMax(), 20);
    }

    void test_decrease_key_non_existent() {
        pq.DecreaseKey(200, 5); // should do nothing
        verifyAndPrint("test decreaseKey on 200 (not present in PQ) w/getMin", pq.getMin(), 7);
    }

    void delete_all() {
        pq.DeleteMin(); // deletes 7
        pq.DeleteMin(); // deletes 20
        verifyAndPrint("test isEmpty after deleting all elements", pq.isEmpty(), true);
    }

    void get_min_when_empty() {
        try {
            pq.getMin();
            verifyAndPrint("test getMin on empty PQ", 0, 1);
        } catch (const std::runtime_error &e) {
            verifyAndPrint("test getMin on empty PQ", 1, 1);
        }
    }

    void get_max_when_empty() {
        try {
            pq.getMax();
            verifyAndPrint("test getMax on empty PQ", 0, 1);
        } catch (const std::runtime_error &e) {
            verifyAndPrint("test getMax on empty PQ", 1, 1);
        }
    }

    void delete_min_when_empty() {
        try {
            pq.DeleteMin();
            verifyAndPrint("test deleteMin on empty PQ", 0, 1);
        } catch (const std::runtime_error &e) {
            verifyAndPrint("test deleteMin on empty PQ", 1, 1);
        }
    }

    void test_increase_key_below_zero() {
        pq.Add(10);
        pq.IncreaseKey(10, -5); // should do nothing
        verifyAndPrint("test increaseKey with negative amount w/getMax", pq.getMax(), 10);
    }

    void test_decrease_key_below_zero() {
        pq.DecreaseKey(10, -3); // should do nothing
        verifyAndPrint("test decreaseKey with negative amount w/getMin", pq.getMin(), 10);
    }

    void test_multiple_operations() {
        pq.Add(4);
        pq.Add(15);
        pq.Add(1);
        pq.DecreaseKey(15, 20);
        pq.IncreaseKey(-5, 9);
        pq.Delete(4); // this deletes the first encounter of 4
        vector<int> heap_to_test = pq.getArray();
        verifyAndPrint("test multiple operations w/array comparison", compareArrays(heap_to_test, vector<int>{1, 10, 4}), true);
    }

    void test_duplicate_elements() {
        while (!pq.isEmpty()) {
            pq.DeleteMin();
        }
        pq.Add(10);
        pq.Add(10);
        pq.Add(5);
        pq.DecreaseKey(10, 3); // should decrease the first 10 to 7
        vector<int> heap_to_test = pq.getArray();
        verifyAndPrint("test duplicate elements w/array comparison", compareArrays(heap_to_test, vector<int>{5, 7, 10}), true);
    }

public:
    void run_tests() {
        test_insertion();
        test_get_min();
        test_get_max();
        test_decrease_key();
        test_increase_key();
        test_delete_min();
        test_delete();
        test_delete_non_existent();
        test_increase_key_non_existent();
        test_decrease_key_non_existent();
        delete_all();
        get_min_when_empty();
        get_max_when_empty();
        delete_min_when_empty();
        test_increase_key_below_zero();
        test_decrease_key_below_zero();
        test_multiple_operations();
        test_duplicate_elements();

        cout << "========================\n";
        cout << "passed " << passed << " out of " << total << " tests." << endl;
        cout << "========================\n";
    }
};
