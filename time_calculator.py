# everything done without the use of datetime module

def add_time(start, duration, starting_day = ''):
  # split the start parameter into variables
  start = start.split(':')
  hour = start[0]
  minute = start[1].split()
  ampm = minute[1]
  minute = minute[0]

  # split the duration parameter and added to previous variables
  duration = duration.split(':')
  hour = int(hour) + int(duration[0])
  minute = int(minute) + int(duration[1])

  count = 0
  days = 0

  # if minute is above 59 then floor division is used to
  # divide by 60 to find additional hours rounded down
  if minute > 59:
    extra_hours = minute // 60
    hour = hour + extra_hours
    minute = minute - 60 # find actual minute by removing 60

  # if minute is less than two digits then minute is 
  # converted to a string and a zero is added to the start
  if minute < 10:
    minute = '0' + str(minute)

  # if hour is above 11 then floor division is used to
  # divide by 24 to find the count of days
  if hour > 11:
    days = hour // 24
    if days > 1:
      days = days + 1
    count = hour // 12 # grab count for AM/PM switch
    hour = hour % 12 # find actual hour with modulus 12
    if hour == 0: # convert 0 to 12 for proper time
      hour = 12

  # change AM/PM based on count from above
  if ampm == 'AM':
    if count % 2 != 0:
      ampm = 'PM'
  else:
    if count % 2 != 0:
      ampm = 'AM'
      if count == 1 or count == 3: #additional day added when PM becomes AM on odd counts
        days = days + 1

  # if elif to convert string day to a number
  if starting_day != '':
    starting_day = starting_day.lower() # lower method used to keep starting_day uniform
    if starting_day == 'tuesday':
      starting_pos = 1
    elif starting_day == 'wednesday':
      starting_pos = 2
    elif starting_day == 'thursday':
      starting_pos = 3
    elif starting_day == 'friday':
      starting_pos = 4
    elif starting_day == 'saturday':
      starting_pos = 5
    elif starting_day == 'sunday':
      starting_pos = 6
    else:
      starting_pos = 0

    # while loop to add days and update day of week
    while_count = days
    while while_count > 0:
      if starting_pos == 6: # keep loop 0-6 for days of week
        starting_pos = 0
      else:
        starting_pos = starting_pos + 1
      while_count = while_count - 1

    # convert number back to day of week with proper output
    if starting_pos == 1:
      starting_day = ', Tuesday'
    elif starting_pos == 2:
      starting_day = ', Wednesday'
    elif starting_pos == 3:
      starting_day = ', Thursday'
    elif starting_pos == 4:
      starting_day = ', Friday'
    elif starting_pos == 5:
      starting_day = ', Saturday'
    elif starting_pos == 6:
      starting_day = ', Sunday'
    else:
      starting_day = ', Monday'

  # return string determined by number of days
  if days == 1:
    new_time = str(hour) + ':' + str(minute) + ' ' + ampm + starting_day + ' (next day)'
  elif days > 1:
    new_time = str(hour) + ':' + str(minute) + ' ' + ampm + starting_day + ' (' + str(int(days)) + ' days later)'
  else:
    new_time = str(hour) + ':' + str(minute) + ' ' + ampm + starting_day

  return new_time