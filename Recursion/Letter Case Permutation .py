


def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.

    result = []

    def lp_helper(s, i, slate):
        if i >= len(s):
            result.append(slate)
        else:
            if s[i].isdigit():
                lp_helper(s,i+1,slate + s[i])
            else:
                lp_helper(s, i + 1, slate + s[i].lower())
                lp_helper(s, i + 1, slate + s[i].upper())

    lp_helper(s,0,'')

    return result

s = 'a1b2'
print(letter_case_permutations(s))

#s(n) = i/p + intermediate + o/p
#ip -n, intermediate - storing in slate along one branch from root to leaf - 1+2+3+ + n = O(n^2)
# o/p - O(2^n*n) - no of leaf nodes - 2^n, each leaf has length n.
#S(n) - O(2^n*n)

#T(n) - O(2^n-1* n) - *n as new string will be generated as we concatenate - internal node, leaf node
# - O(2^n*1)
#T(n) - O(2^n*n)


