from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".
        """
        prefix: str = strs[0]
        for word in strs[1:]:
            new_prefix: str = ""
            for label_word, label_prefix in zip(word, prefix):
                if label_prefix == label_word:
                    new_prefix += label_prefix
                else:
                    prefix = new_prefix
                    break
            prefix = new_prefix

        return prefix


if __name__ == '__main__':
    s1 = Solution()
    print(s1.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(s1.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
