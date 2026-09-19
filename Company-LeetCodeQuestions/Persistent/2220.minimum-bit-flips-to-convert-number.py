class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        def convert_bits(num):
            bits = ""
            while num != 0:
                quotient = int(num/2)
                remainder = int(num %2 !=0)
                bits += str(remainder)
                num = quotient
            return bits    
        
        bits_start = convert_bits(start)
        bits_goal = convert_bits(goal)

        len_bit_start = len(bits_start)
        len_bit_goal = len(bits_goal)
        if len_bit_start > len_bit_goal:
            bits_goal += "0"*(len_bit_start - len_bit_goal)
        else:
            bits_start += "0"*(len_bit_goal - len_bit_start)    

        
        print(bits_start, bits_goal)    
        min_change = 0
        for i in range(len(bits_start)):
            if bits_start[i] != bits_goal[i]:
                min_change += 1
        
        return min_change

sol = Solution()
start = 3
goal = 4
print(sol.minBitFlips(start,goal))
