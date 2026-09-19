


# For each letter choose lower or upper case; digits offer only one choice.
# One shared slate uses O(n) working space; this version returns character lists, not joined strings.
def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """

    result = []
    slate = []
    def lp_helper(s, i, slate):
        if i >= len(s):
            # Copy each complete slate; storing the original list would let later pops erase saved answers.
            result.append(slate[:])
        else:
            # Digits have no case variant, so take just one recursive branch.
            if s[i].isdigit():
                slate.append(s[i])
                lp_helper(s,i+1,slate)
                # Undo the character added for this branch before exploring the next choice or returning.
                slate.pop()
            else:
                slate.append(s[i].lower())
                lp_helper(s, i + 1, slate)
                # Undo the character added for this branch before exploring the next choice or returning.
                slate.pop()
                slate.append(s[i].upper())
                lp_helper(s, i + 1, slate)
                # Undo the character added for this branch before exploring the next choice or returning.
                slate.pop()

    # Start with no decided characters; for a letters, output storage is O(n * 2^a).
    lp_helper(s,0,slate)

    return result

s = 'a1b2'
print(letter_case_permutations(s))




