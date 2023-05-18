import datetime
def add_time(start, duration, starting_day = ''):
  format = '%I:%M %p'
  start = datetime.datetime.strptime(start, format)

  if starting_day != '':
    if starting_day.lower() == 'tuesday':
      start = start.replace(day=2)
    elif starting_day.lower() == 'wednesday':
      start = start.replace(day=3)
    elif starting_day.lower() == 'thursday':
      start = start.replace(day=4)
    elif starting_day.lower() == 'friday':
      start = start.replace(day=5)
    elif starting_day.lower() == 'saturday':
      start = start.replace(day=6)
    elif starting_day.lower() == 'sunday':
      start = start.replace(day=7)

  duration = duration.split(':')
  time_change = datetime.timedelta(hours = int(duration[0]), minutes = int(duration[1]))
  new_time = start + time_change

  if starting_day != '':
        starting_day = new_time.strftime(', %A')

  if new_time.strftime('%j') > start.strftime('%j'):
    if int(new_time.strftime('%j')) - int(start.strftime('%j')) == 1:
      new_time = new_time.strftime('%-I:%M %p' + starting_day + ' (next day)')
    else:
      days = int(new_time.strftime('%j')) - int(start.strftime('%j'))
      new_time = new_time.strftime('%-I:%M %p') + starting_day + ' (' + str(days) + ' days later)'
  else:
    new_time = new_time.strftime('%-I:%M %p') + starting_day

  return new_time