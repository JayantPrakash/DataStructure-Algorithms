


def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.

    result = []
    slate = []
    def lp_helper(s, i, slate):
        if i >= len(s):
            result.append(slate[:])
        else:
            if s[i].isdigit():
                slate.append(s[i])
                lp_helper(s,i+1,slate)
                slate.pop()
            else:
                slate.append(s[i].lower())
                lp_helper(s, i + 1, slate)
                slate.pop()
                slate.append(s[i].upper())
                lp_helper(s, i + 1, slate)
                slate.pop()

    lp_helper(s,0,slate)

    return result

s = 'a1b2'
print(letter_case_permutations(s))

#s(n) = i/p + intermediate + o/p
#ip -n, intermediate - O(n) - there is only one copy of slate
# o/p - O(2^n*n) - no of leaf nodes - 2^n, each leaf has length n.
#S(n) - O(2^n*n)

#T(n) - O(2^n-1* 1) -  - internal node, leaf node - O(2^n*)n
# - *n  as for each leaf node, slate is copied and added to result
#T(n) - O(2^n*n)


