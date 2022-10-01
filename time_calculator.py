from datetime import datetime,timedelta

def add_time(start, duration,dayofwk = None):
  dayofweek = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
  }
  duration_hour_org = int(duration.partition(":")[0])
  duration_minutes_org = int(duration.partition(":")[2])
  start_time = datetime.strptime(start, '%I:%M %p')
  
  #Calculate next day
  time_24hr = datetime.strftime(start_time,'%H:%M')
  hour_24hr = int(time_24hr.partition(":")[0])
  min_24hr = int(time_24hr.partition(":")[2])

  add_hr = 0
  cal_nextday = 0
  
  if (min_24hr + duration_minutes_org) > 60:
    add_hr += (min_24hr + duration_minutes_org)//60
    duration_hour = duration_hour_org + add_hr
    duration_minutes = (min_24hr + duration_minutes_org) - (add_hr*60)
  else:
    duration_hour = duration_hour_org
    duration_minutes = duration_minutes_org
    
  if (hour_24hr +  duration_hour) > 24:
    cal_nextday += (hour_24hr + duration_hour)//24
  
  #Calculate display day of week
  if str(dayofwk).capitalize() in dayofweek:
    next_day = ""
    cal_dow = None

    if cal_nextday == 0:
      str_nextday = ", " + str(dayofwk.capitalize())
    else:
      if (dayofweek[str(dayofwk).capitalize()] + cal_nextday) > 7:
        cal_dow = (dayofweek[str(dayofwk).capitalize()] + cal_nextday)%7
      else:
        cal_dow =  dayofweek[str(dayofwk).capitalize()] + cal_nextday
    
      next_day = [k for k, v in dayofweek.items() if v ==  cal_dow][0]
      
      if cal_nextday == 1:
        str_nextday = ", " + next_day + " (next day)"
      else:
        str_nextday = ", " + next_day + " (" + str(cal_nextday) +" days later)"
    
  #calculate new_time
  cal_time = start_time + timedelta(minutes=duration_minutes_org, hours=duration_hour_org)
  
  #Show output
  if dayofwk == None:
    if cal_nextday == 1:
      new_time = cal_time.time().strftime('%-I:%M %p') + " (next day)"
    elif cal_nextday > 1:
      new_time = cal_time.time().strftime('%-I:%M %p') + " (" + str(cal_nextday) + " days later)"
    else:
      new_time = cal_time.time().strftime('%-I:%M %p')
  else:
    new_time = str(cal_time.time().strftime('%-I:%M %p')) + str_nextday

  return new_time