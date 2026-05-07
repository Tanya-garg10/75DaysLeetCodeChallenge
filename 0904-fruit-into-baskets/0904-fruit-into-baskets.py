class Solution:
    def totalFruit(self, fruits):
        left = 0
        count = {}
        max_fruits = 0
        
        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] = count.get(fruit, 0) + 1
            
            # shrink window if more than 2 types
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                
                if count[left_fruit] == 0:
                    del count[left_fruit]
                
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits