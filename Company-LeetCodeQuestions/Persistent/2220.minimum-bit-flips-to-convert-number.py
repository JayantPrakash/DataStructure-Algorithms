class Solution:
    # Each differing bit needs exactly one flip; count mismatches between aligned binary representations.
    # This is the same concept as counting set bits in start XOR goal, implemented here with strings.
    def minBitFlips(self, start: int, goal: int) -> int:

        # Repeated division emits bits least-significant first, so the resulting string is reversed binary.
        # Assumes nonnegative, modest-sized integers; int(num / 2) uses floating-point division.
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
        # Pad on the right because these strings store low-order bits first; absent high bits are zero.
        if len_bit_start > len_bit_goal:
            bits_goal += "0"*(len_bit_start - len_bit_goal)
        else:
            bits_start += "0"*(len_bit_goal - len_bit_start)    

        
        print(bits_start, bits_goal)    
        min_change = 0
        for i in range(len(bits_start)):
            # Each mismatch is independent: fixing one bit does not affect any other position.
            if bits_start[i] != bits_goal[i]:
                min_change += 1
        
        return min_change

sol = Solution()
start = 3
goal = 4
print(sol.minBitFlips(start,goal))
