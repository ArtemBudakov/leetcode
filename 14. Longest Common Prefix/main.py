from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".
        """

        if not strs:
            return ''

        prefix: str = strs[0]
        for word in strs:
            if prefix == "":
                return prefix

            if len(word) < len(prefix):
                prefix = prefix[:len(word)]

            for index, label in enumerate(word):
                if (index + 1) > len(prefix):
                    break
                if prefix[index] != label:
                    prefix = prefix[:index]
                    break
        return prefix


if __name__ == '__main__':
    s1 = Solution()
    print(s1.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(s1.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
