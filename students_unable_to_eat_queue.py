class queueNode(self,val):
    self.val = val
    self.next = None

class queues:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #Adds an element to the end of the queue.
    def enqueue(self,val):
        new_node = queueNode(val)
        #if empty queue, set head and tail to new node
        if self.tail == None:
            self.head = self.tail = new_node
        #if not empty, add to the end and rearranrge tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        #add to size since you added to queue
        self.size += 1
    
    #Removes and returns the element at the front of the queue.
    def dequeue(self):
        #if queue is empty then return nothing 
        if self.is_empty():
            return None
        #set removed node to the head and get rid of it, rearrange head
        removed_node = self.head
        self.head = self.head.next
        #if empty then set tail to none
        if not self.head:
            self.tail = None
        #decrease size since you removed by one, then return the removed nodes val
        self.size -= 1
        return removed_node.val

    #function for if the queue is empty, return self.size = 0
    def is_empty(self):
        return self.size == 0

    #peek function that looks at the heads val
    def peek(self):
        #check if empty
        if self.is_empty():
            return None
        return self.head.val
    
    #get size funtion, returns the size of queue
    def get_size(self):
        return self.size

class Solution(object):
    def countStudents(self, students, sandwiches):
        len_students = len(students)
        #convert students into queue
        students_queue = queues()
        #convert sandwiches into array
        food_stack = []

        #iterate through len of students 
        for i in range(len_students):
            #add each student into student_queue using enqueue function
            students_queue.enqueue(students[i])
            food_stack.append(sandwiches[len_students - 1 - i])

            #set counter
            counter = 0
            #The loop exits when all sandwiches are served (counter is reset to 0) or all students are checked
            while counter < len(food_stack):
                #check if student at front matches sandwich on top of stack
                #If the current student's preferred sandwich is available, they are served
                if students_queue.peek() == food_stack[-1]:
                    #student takes sandwich, sandwich is dequeed and poped from stack
                    #reset counter since food is taken
                    students_queue.dequeue()
                    food_stack.pop()
                    conter = 0
                #if food doesnt match, student moves to end of queue, dequeue and enqueue student
                #increment counter
                else:
                    deq_val = students_queue.dequeue()
                    students_queue.enqueue(deq_val)
                    counter += 1
            #counter holds all students who dont have the sandwich
            return counter 


""" 
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 
""" 