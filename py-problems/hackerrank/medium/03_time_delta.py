from datetime import timedelta, datetime, timezone

def parse_time(t_str):
   splited_time = t_str.split()
   
   date, m, y = int(splited_time[1]), datetime.strptime(splited_time[2], "%b").month, int(splited_time[3])
   times = splited_time[4].split(":")
   hr, min, sec = int(times[0]), int(times[1]), int(times[2])

   # Handle timezone offset, curcial code
   tz_str = splited_time[-1]
   tz_sign = -1 if tz_str[0] == '-' else 1 # saviour..............
   # if we remove the above code, then it mixed up with positive and negative
   tz_hr = int(tz_str[1:3])
   tz_min = int(tz_str[3:])
   tz_offset = timedelta(hours=tz_sign*tz_hr, minutes=tz_sign*tz_min)
   print(tz_offset)
   timezone_offset = timezone(tz_offset)
   
   return datetime(year=y, month=m, day=date, hour=hr, minute=min, second=sec, tzinfo=timezone_offset)

def time_delta(t1_str, t2_str):
    
    t1 = parse_time(t1_str)
    t2 = parse_time(t2_str)
    
    return str(int(abs((t1 - t2).total_seconds())))

if __name__ == '__main__':
   t = int(input())
   l = []
   for _ in range(t):
      t1 = input()
      t2 = input()

      delta = time_delta(t1, t2)
      l.append(delta)
      print(delta)
   print(l,"\n")