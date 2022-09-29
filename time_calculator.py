def add_time(start, duration, weekday=None):

    # set up variables
    start_hour, start_min = (int(x) for x in 
                             start.replace(':', ' ').split(' ')[:2])
    start_period = 0 if start.split(' ')[1] == 'AM' else 1
    duration_hour, duration_min = (int(x) for x in duration.split(':'))
   
    # calculate new time
    end_hour = start_hour + duration_hour
    end_min = start_min + duration_min
    periods = 0
    if end_min >=60:
        end_hour += 1
        end_min %= 60
    if end_hour >=12:
        periods = end_hour // 12
        end_hour = end_hour % 12 if end_hour % 12 != 0 else 12
    end_period = start_period if periods % 2 == 0 else 1 - start_period
    
    new_time = (str(end_hour) + ':' + str(end_min).zfill(2) + ' ' + 
                ['AM', 'PM'][end_period])

    # calculate days passed to include as suffix to new time
    days = periods // 2 if start_period == 0 else (periods + 1) // 2
    if days > 1:
        suffix = f'({days} days later)'
    elif days == 1:
        suffix = '(next day)'
    else:
        suffix = None
        
    # calculate new weekday if weekday provided and return new time
    if weekday:
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 
                       'friday', 'saturday', 'sunday']
        start_day = days_of_week.index(weekday.lower())
        end_day = (start_day + days) % 7
        new_time_and_weekday = new_time + ', ' + days_of_week[end_day].capitalize()
        return new_time_and_weekday if not suffix else new_time_and_weekday + ' ' + suffix

    # return new time (no weekday)
    return new_time if not suffix else new_time + ' ' + suffix