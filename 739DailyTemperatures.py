class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # solution using stack
        stack = [1]
        # initialized the res for all 0 
        res = [0]*len(temperatures)
        for index , temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                # pop the stack
                currentindex = stack.pop()
                res[currentindex] =  index - currentindex
            # add index into the stack 
            stack.append(index)
        return res