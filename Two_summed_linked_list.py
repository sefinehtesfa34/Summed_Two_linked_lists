# Sum_of_Two_linked_lists
#create Node class 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#create LinkedList class
class LinkedList:
    def __init__(self):
        self.head1=None
        self.head2=None
        self.headSum=None
     #create first linked lisst
    def push1(self,data):
        newNode1=Node(data)
        newNode1.next=self.head1
        self.head1=newNode1
    #create second linkedlist
    def push2(self,data):
        newNode2=Node(data)
        newNode2.next=self.head2
        self.head2=newNode2
    create a linked list for the sum of the two linked lists
    def pushsum(self,sum_data):
        sumNode=Node(sum_data)
        sumNode.next=self.headSum
        self.headSum=sumNode
    #print the first , second and summed linked lists
    def printValue(self):
        tmp=self.head1
        print("First linked list================================")
        while tmp:
            print(tmp.data)
            tmp=tmp.next
        print("second linked list============================")
        tempSecond=self.head2
        while tempSecond:
            print(tempSecond.data)
            tempSecond=tempSecond.next
        sumTemp=self.headSum
        print("summed ============================ ")
        while sumTemp:
            print(sumTemp.data)
            sumTemp=sumTemp.next
    #reverse the first linked list
    def reverse1(self):
        prev = None
        current = self.head1
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head1 = prev
    #reverse the second linked list
    def reverse2(self):
        prev = None
        current = self.head2
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head2 = prev
    #reverse the summed linked list
    def reverse(self):
        prev = None
        current = self.headSum
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.headSum = prev
    #sum the two linked lists
    def sumLinkedList(self):
        temp1=self.head1
        temp2=self.head2
        carry=0
        while temp1 or temp2:
            if temp1 is not None and temp2 is not None:    
                summed=temp1.data+temp2.data+carry
                carry=0
                if summed>=10:
                    summed-=10
                    carry=1
                self.pushsum(summed)
            elif temp1:
                summed=temp1.data+carry
                if summed>=10:
                    summed-=10
                    carry=1
                self.pushsum(summed)
            else:
                summed=temp2.data+carry
                if summed>=10:
                    carry=1
                    summed=summed-10
                self.pushsum(summed)
            if temp1 and temp2:
                temp1=temp1.next
                temp2=temp2.next
            elif temp1:
                temp1=temp1.next
            else:
                temp2=temp2.next
#create linked list object
linkedList=LinkedList()
#call the push1() method
linkedList.push1(1)
linkedList.push1(9)
linkedList.push1(3)
#call the push2() method
linkedList.push2(4)
linkedList.push2(7)
linkedList.push2(0)
linkedList.push1(0)
#call the sumLinkedList() method
linkedList.sumLinkedList()
#call the reverse1() method
linkedList.reverse1() 
#call the reverse2() method
linkedList.reverse2()
#finally call the printValue() method
linkedList.printValue()
            
