def count_pattern(text, pattern):
    return sum(
        text.startswith(pattern, i)
        for i in range(len(text) - len(pattern) + 1)
    )