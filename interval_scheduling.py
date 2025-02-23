intervals = [(1,2),(2,3),(3,4),(4,5)]
def interval_scheduling(intervals):
    intervals.sort(key=lambda x :x[1])
    selected_intervals=0
    last_end_time = float('-inf')
    for start,end in intervals:
        if start >= last_end_time:
            selected_intervals += 1
            last_end_time =end
            return selected_intervals
print(interval_scheduling(intervals))