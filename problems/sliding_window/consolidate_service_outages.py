def consolidate_service_outages(outages: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], int]:

    if not outages:
        return [], 0

    sorted_outages = sorted(outages)

    start, end = sorted_outages[0]

    start_outage = start
    end_outage = end

    result = []

    for start, end in sorted_outages[1:]:
        if start <= end_outage:
           end_outage = max(end_outage, end)
        else:
            result.append((start_outage, end_outage))
            start_outage, end_outage = start, end

    result.append((start_outage, end_outage))

    total_downtime = sum(
        end - start
        for start, end in result
    )

    return (result, total_downtime)
    
