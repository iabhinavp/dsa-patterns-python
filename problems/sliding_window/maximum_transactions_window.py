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





def max_window_sum(values: list[int], k: int) -> int:

    if k < 0 or k > len(values) or k == 0:
        raise ValueError


    total_sum_values = 0

    for index in range(k):
        total_sum_values += values[index]

    largest_sum = total_sum_values

    for entering_index in range(k, len(values)):

        removing_index = entering_index - k 

        total_sum_values -= values[removing_index]
        total_sum_values += values[entering_index]

        largest_sum = max(largest_sum, total_sum_values)


    return largest_sum












