class Solution:

    def encode(self, strs: List[str]) -> str:
        result=[]

        for s in strs:
            result.append(str(len(s)))
            result.append('#')
            for char in s:
                result.append(char)
        final_encoded_string="".join(result)
        return final_encoded_string
            
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i <len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            start_string=j+1
            end_string=length+start_string
            result.append(s[start_string:end_string])
            i= end_string
        return result
                