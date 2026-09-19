from typing import List
class Codec:
    # Store string lengths separately and concatenate the payload on this Codec instance.
    # This version returns None: decoding works only by reusing the same instance's stored state.
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Lengths preserve boundaries even when strings are empty or contain delimiter-like characters.
        self.map_len = []
        for str in strs:
            self.map_len.append(len(str))

        self.encoded_string = "".join(strs)    

    # The argument s is unused here; decode reads self.encoded_string and self.map_len from encode.
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []

        i = 0
        len_seen = 0
        # len_seen is the start of the next string; slicing by its recorded length reconstructs the boundary.
        for curr_len in self.map_len:
            curr_str = self.encoded_string[len_seen:len_seen + curr_len] 
            strs.append(curr_str)
            len_seen += curr_len

        return strs           



# Your Codec object will be instantiated and called as such:
codec = Codec()
dummy_input = ["Hello","World", "jayant ", "Prakash"]
dummy_input = [""]

print(codec.decode(codec.encode(dummy_input)))