def longest_failed_streak(statuses: list[str]) -> int:
    current_streak = 0
    longest_streak = 0

    for status in statuses:
        if status == "failed":
            current_streak += 1

            if current_streak > longest_streak:
                longest_streak = current_streak
        else:
            current_streak = 0

    return longest_streak


print(
    longest_failed_streak(
        ["accepted", "failed", "failed", "accepted", "failed"]
    )
)  # 2

print(longest_failed_streak([]))  # 0

print(longest_failed_streak(["failed", "failed", "failed"]))  # 3

print(longest_failed_streak(["accepted", "accepted"]))  # 0
