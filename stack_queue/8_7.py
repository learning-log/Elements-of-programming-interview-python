#implement circular queue

class Qeue():
    def __init__(self):
        self.capacity = 10
        self.head = 0
        self.tail = 0
        self.num_elements = 0
        self.store = [0]*self.capacity
    def enque(self,val):
        if self.num_elements<self.capacity:
            self.store[self.tail] = val
            self.tail= (self.tail + 1)%self.capacity
            self.num_elements+=1
        else:
            print("Error: Capacity full")
    def deque(self):
        if self.num_elements>0:
            num = self.store[self.head]
            self.num_elements-=1
            self.head = (self.head+1)%self.capacity
            return num
        else:
            print("error: empty")
            return -1 
    def empty(self):
        return self.num_elements==0

q = Qeue()

q.enque(1)
q.enque(4)

q.enque(1)
q.enque(4)

q.enque(1)
q.enque(4)

print(q.store)
print(q.empty())
print(q.deque())
q.enque(1)
q.enque(4)
q.enque(1)
q.enque(4)
q.enque(1)
q.enque(4)

