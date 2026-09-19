# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Group the state and operations used by the minimum bit flips to convert number implementation.
class Solution:
    # Compute or update the min bit flips result for the supplied input.
    def minBitFlips(self, start: int, goal: int) -> int:

        # Compute or update the convert bits result for the supplied input.
        def convert_bits(num):
            bits = ""
            # Keep processing while `num != 0` remains true.
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
        # Choose this path when `len_bit_start > len_bit_goal` is true.
        if len_bit_start > len_bit_goal:
            bits_goal += "0"*(len_bit_start - len_bit_goal)
        else:
            bits_start += "0"*(len_bit_goal - len_bit_start)    

        
        print(bits_start, bits_goal)    
        min_change = 0
        # Process each value from `range(len(bits_start))`.
        for i in range(len(bits_start)):
            # Choose this path when `bits_start[i] != bits_goal[i]` is true.
            if bits_start[i] != bits_goal[i]:
                min_change += 1
        
        return min_change

sol = Solution()
start = 3
goal = 4
print(sol.minBitFlips(start,goal))
