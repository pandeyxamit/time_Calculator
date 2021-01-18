def add_time(start, duration, day=None):
    weekdays = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
    curr_day = day
    hours = int(start.split()[0].split(":")[0])
    minutes = int(start.split()[0].split(":")[1])
    period = start.split()[1]
    dur_hours = int(duration.split(":")[0])
    dur_minutes = int(duration.split(":")[1])
    num_days = 0
    day_num = 0
    same_day = 0
    minutes = minutes + dur_minutes
    if period == "PM":
        hours += 12
    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + dur_hours + 1
    else:
        hours = hours + dur_hours
    
    if minutes < 10:
        minutes = "0{}".format(minutes)
    
    num_days = hours // 24

    if hours >= 12 and hours < 24:
        period = "PM"
        if hours > 12:
            hours = hours - 12
    else:
        hours = hours % 24
        period = "AM"
        if hours == 0:
            hours = 12
        else:
            if hours > 12:
                hours = hours - 12

            
        
    if not curr_day:
        if num_days == 0:
            new_time = "{}:{} {}".format(hours, minutes, period)
        elif num_days == 1:
            new_time = "{}:{} {} (next day)".format(hours, minutes, period)
        else:
            new_time = "{}:{} {} ({} days later)".format(hours, minutes, period, num_days)
    else:
        for key in weekdays.keys():
            if weekdays[key].lower() == curr_day.lower():
                day_num = key
                same_day = key
        
        day_num = (day_num + num_days) % 7
        
        if day_num > 0:
            curr_day = weekdays[day_num]
        else:
            curr_day = weekdays[7]
        if num_days == 0:
            new_time = "{}:{} {}, {}".format(hours, minutes, period, curr_day)
        elif num_days == 1:
            new_time = "{}:{} {}, {} (next day)".format(hours, minutes, period, curr_day)
        else:
            new_time = "{}:{} {}, {} ({} days later)".format(hours, minutes, period, curr_day, num_days)

    return new_time