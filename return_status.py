def report_status(scheduled_time, estimated_time):
    ''' (number, number)-> str
    return the flight status (on time, early, delayed)
    for a flught that was schedued to arrive at schaduled_time,
    but is now estimatd to arrive at expectd_tim. 
    
    pr-condition: 0.0 <= scheduled_time < 24.0 and 
    0.0 <= estimated_time < 24.0
    
    >>> report_status (14.3, 14.3)
    'on time'
    >>> report_status (12.5, 11.5)
    'early'
    >>> report_status (9.0, 9.5)
    'delayed'
    '''
    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'
    
    
    
    
    
