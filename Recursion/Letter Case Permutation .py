


# For an alphanumeric string, letters have two case choices and digits have one.
# With a letters there are 2^a outputs, each of length n.
def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """

    result = []

    # i is the next character to decide; slate is an immutable prefix owned by this branch.
    def lp_helper(s, i, slate):
        if i >= len(s):
            # Store the completed string. Output uses O(n * 2^a) space; live prefixes can add O(n^2) auxiliary space.
            result.append(slate)
        else:
            # Digits pass through unchanged; branching on them would create duplicate outputs.
            if s[i].isdigit():
                lp_helper(s,i+1,slate + s[i])
            else:
                # Explore both cases independently; concatenation creates a new prefix, so no undo is required.
                lp_helper(s, i + 1, slate + s[i].lower())
                lp_helper(s, i + 1, slate + s[i].upper())

    lp_helper(s,0,'')

    return result

s = 'a1b2'
print(letter_case_permutations(s))




