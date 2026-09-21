def maximum_transaction_window(
    amounts: list[int],
    window_size: int,
) -> int:
    if not amounts:
        raise ValueError("amounts cannot be empty")

    if window_size <= 0 or window_size > len(amounts):
        raise ValueError("invalid window size")

    window_total = sum(amounts[:window_size])
    largest_total = window_total

    for entering_index in range(window_size, len(amounts)):
        leaving_index = entering_index - window_size

        window_total -= amounts[leaving_index]
        window_total += amounts[entering_index]

        largest_total = max(largest_total, window_total)

    return largest_total