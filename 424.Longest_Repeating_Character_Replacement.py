class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     freq = [0] * 26
     left = 0
     max_freq = 0
     max_window = 0

     for right in range(len(s)):
        # Update frequency of current character
        idx = ord(s[right]) - ord('A')
        freq[idx] += 1

        # Update max frequency in the window
        max_freq = max(max_freq, freq[idx])

        # Current window size
        window_length = right - left + 1

        # If replacements needed exceed k, shrink window
        if window_length - max_freq > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        # Update max window size
        window_length = right - left + 1
        max_window = max(max_window, window_length)

     return max_window