class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        scurrent_temp=[]
        
        result=[0] * len(temperatures)
        for i in range(len(temperatures)):
            current_temp=temperatures[i]
            for j in range(i+1, len(temperatures)):
                if current_temp<temperatures[j]:
                    result[i]= j - i
                    break
                

        return result