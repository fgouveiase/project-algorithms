def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int) or target_time == 0:
        return None
    count_student = 0
    for period in permanence_period:
        start, end_time = period
        if not isinstance(start, int) or not isinstance(end_time, int):
            return None
        if start <= target_time <= end_time:
            count_student += 1
    return count_student
