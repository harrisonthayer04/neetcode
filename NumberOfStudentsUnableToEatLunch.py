from collections import Counter

# Case 1 output is 0
# students = [1,1,0,0], sandwiches = [0,1,0,1]
# step 1: students = [1,0,0,1], sandwiches = [0,1,0,1]
# step 2: students = [0,0,1,1], sandwiches = [0,1,0,1]
# step 3: students = [0,1,1], sandwiches = [1,0,1]
# step 4: students = [1,1,0], sandwiches = [1,0,1]
# step 5: students = [1,0], sandwiches = [0,1]
# step 6: students = [0,1], sandwiches = [0,1]
# step 6: students = [1], sandwiches = [1]
# step 6: students = [], sandwiches = []


# Case 2 output is 3
# students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Step 1: students = [1,1,0,0,1], sandwiches = [0,0,0,1,1]
# Step 2: students = [1,0,0,1,1], sandwiches = [0,0,0,1,1]
# Step 3: students = [0,0,1,1,1], sandwiches = [0,0,0,1,1]
# Step 4: students = [0,1,1,1], sandwiches = [0,0,1,1]
# Step 5: students = [1,1,1], sandwiches = [0,1,1] <- Here is the issue

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        counter = Counter(students)
        
        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                result -= 1
                counter[sandwich] -= 1
            else:
                return result

        return result