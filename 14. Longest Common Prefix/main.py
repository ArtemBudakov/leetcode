from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".
        """
        first_word: str = strs[0]
        prefix: str = ""
        for word in strs[1:]:
            if prefix == "":
                for label_word, label_first_word in zip(word, first_word):
                    if label_first_word == label_word:
                        prefix += label_word
            else:
                new_prefix: str = ""
                for label_word, prefix_label in zip(word, prefix):
                    if prefix_label == label_word:
                        new_prefix += prefix_label
                prefix = new_prefix

        return prefix


if __name__ == '__main__':
    s1 = Solution()
    print(s1.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(s1.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
