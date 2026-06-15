struct Node {
    int val;
    int min_at_node; // Stores the minimum value up to this point
    Node* next;

    Node(int val_, int min_, Node* next_) {
        this->val = val_;
        this->min_at_node = min_;
        this->next = next_;
    }
};

class MinStack {
private:
    Node* head;
public:
    MinStack() {
        this->head = nullptr;
    }
    
    void push(int val) {
        // Calculate the new minimum based on the current head's minimum
        int current_min = (this->head == nullptr) ? val : std::min(this->head->min_at_node, val);
        this->head = new Node(val, current_min, this->head);
    }
    
    void pop() {
        if (this->head != nullptr) {
            Node* temp = this->head;
            this->head = this->head->next;
            delete temp;
        }
    }
    
    int top() {
        return this->head->val;
    }
    
    int getMin() {
        return this->head->min_at_node;
    }
    
    ~MinStack() {
        while (this->head != nullptr) {
            Node* temp = this->head;
            this->head = this->head->next;
            delete temp;
        }
    }
};