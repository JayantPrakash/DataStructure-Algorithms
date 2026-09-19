# slate holds chosen characters; array holds undecided characters. Each step excludes or includes array[0].
def subset_hp(slate, array):
    # When nothing remains to decide, print one subset, including the empty subset.
    if len(array) == 0:
        print(slate)
    else:
        subset_hp(slate, array[1:])
        # Immutable strings keep branches independent without pop/undo, but slicing and concatenation allocate copies.
        subset_hp(slate + array[0], array[1:])


# Printing all 2^n subsets costs O(n * 2^n) total character work.
# Retained string prefixes/suffixes along a recursion chain can require O(n^2) auxiliary space.
def all_subsets(array):
    subset_hp('', array)


array = '123'

all_subsets(array)

