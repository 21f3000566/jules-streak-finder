def longest_positive_streak(nums: list[int]) -> int:
    """
    Return the length of the longest run of consecutive values strictly greater than 0.
    """
    longest_streak = 0
    current_streak = 0
    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 0
    longest_streak = max(longest_streak, current_streak)
    return longest_streak
