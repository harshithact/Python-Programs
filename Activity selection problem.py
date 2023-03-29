def activity_selection(start, finish):
    
    n = len(start)
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]
    
    for i in range(1, n):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    return selected
