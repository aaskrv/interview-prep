"""
- DAY 28 -
- First Unique -

You have a queue of integers, you need to retrieve the first unique integer in the queue. 

Implement the FirstUnique class: 
• FirstUnique( int [ ] nums ) Initializes the object with the numbers in the queue. 
• int showFirstUnique( ) returns the value of the first unique integer of the queue, and returns -1 if there is no such integer. 
• void add( int value) insert value to the queue.

Ex:
["FirstUnique","showFirstUnique","add","showFirstUnique"] 
[[[809]],[],[809],[]] 

Output: 
[nu11,809,null,-1] 

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]); 
firstUnique.showFirstUnique(); // return 809 
firstUnique.add(809); // the queue is now [809,809] 
firstUnique.showFirstUnique(); // return —1 
"""

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = []
        self.dict = {}
        for i in nums:
            self.add(i)
        

    def showFirstUnique(self) -> int:
        while len(self.unique) > 0 and self.dict[self.unique[0]] > 1:
            self.unique.pop(0)
        
        if len(self.unique) == 0:
            return -1
        else:
            return self.unique[0]
        

    def add(self, value: int) -> None:
        if value not in self.dict:
            self.dict[value] = 1
            self.unique.append(value)
        else:
            self.dict[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)