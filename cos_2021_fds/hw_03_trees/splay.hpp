#include<utility>
#include"node.hpp"

template<typename T>
class Splay  {
private:
    std::shared_ptr<Node<T>> root;


    /* The splay method: remember the splay method is responsible for
        "splaying" the current node to the root of the tree.
        The node passed into the method is the node that was either:
            - just inserted
            - or found, using the find method.
        This is the node that must be "splayed" to the root of the tree.

        NOTE: Your implementation should be recursive.

        Please refer to the _insert and _find methods to see where this
        method is called. 
    */
    void left_rotation() {

    }

    void right_rotation() {

    }

    void zig_zig() {

    }

    void zig_zag() {

    }

    void _splay(std::shared_ptr<Node<T>> cur) {
        // PHASE 1: Implemet the splay method for the tree.
        //  Refer to the book for the two types of rotations.
        //  This is a challenging exercise. I suggest you first draw out
        //  the nodes to understand how splaying works.

        if(cur->)
    }

    void _insert(std::shared_ptr<Node<T>> cur, std::shared_ptr<Node<T>> newnode) {
        if(*newnode < *cur) {
            if(cur->left == nullptr) {
                cur->left = newnode;
                newnode->parent = cur;
                _splay(newnode);
            }
            else _insert(cur->left, newnode);
        } else if(*newnode > *cur) {
            if(cur->right == nullptr) {
                cur->right = newnode;
                newnode->parent = cur;
                _splay(newnode);
            }
            else _insert(cur->right, newnode);
        } else { return; }
    }

    int _find(T t, std::shared_ptr<Node<T>> cur, int depth) {
        if(!cur) return depth;
        else if(*cur==t) {
            _splay(cur);
            return depth;
        }
        else if(*cur > t) return _find(t, cur->left, depth+1);
        else return _find(t, cur->right, depth+1);
    }

    void _print(std::shared_ptr<Node<T>> cur, std::string indent) {
        if(!cur) return;
        if(cur->right) _print(cur->right, indent+"*");
        std::cout << indent << cur->data << std::endl;
        if(cur->left) _print(cur->left, indent+"*");
        
    } 

public:
    Splay()
        : root(nullptr)
    {}

    void insert(T t) {
        std::shared_ptr<Node<T>> node = std::make_shared<Node<T>>(t);
        if(root==nullptr) {
            root = node;
        } else {
            _insert(root, node);
        }
    }

    int find(T t) {
        return _find(t, root, 0);
    }

    void print() {
        _print(root, "");
    }
};