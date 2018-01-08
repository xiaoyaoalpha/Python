#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from datetime import timezone
import time

# Get local time
# 2017-09-25 10:58:18.666643
now = datetime.now()

# Get target time
# 2015-12-25 17:16:54
target_time = datetime(2015, 12, 25, 17, 16, 54)

# Convert datetime type to time stamp
# 1506308521.664049
timeStamp = now.timestamp()

# Convert time stamp to datetime object
# 2017-09-25 11:03:32.910864
target_time2 = datetime.fromtimestamp(timeStamp)

# Convert time stamp to datetime object in UTC time
# 2017-09-25 03:04:50.380004
target_time3 = datetime.utcfromtimestamp(timeStamp)

# Convert string object to datetime object
# 2017-09-25 15:04:50
str_time1 =  "2017-9-25 15:4:50"
date_time1 = datetime.strptime(str_time1, "%Y-%m-%d %H:%M:%S")

# Convert datetime object to string object
# Mon Sep 25 13:22:30
date_time2 = date_time1
str_time2 = date_time2.strftime("%a %b %d %H:%M:%S")

# Add and reduce date and time (not for year or month)
# 2017-10-05 17:04:50
date_time3 = date_time1 + timedelta(days=10,hours=2)
# 11370 days, 13:29:59.198400
age1 = datetime.now() - datetime.strptime("1986-08-09 00:00:00", "%Y-%m-%d %H:%M:%S")

# Convert local time to utc time
# Create time zone east_8
tz_utc_east_8 = timezone(timedelta(hours=8))
# 2017-09-25 13:41:27.004078+08:00
bj_dt = now.replace(tzinfo=tz_utc_east_8)

# Change time zone
# 2017-09-25 05:43:45.657048+00:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# 2017-09-25 13:43:45.657048+08:00
bj_dt = utc_dt.astimezone(tz_utc_east_8)

# Count datedelta
born_dt = datetime.strptime("1986-08-09 00:00:00", "%Y-%m-%d %H:%M:%S")
age_year = now.year - born_dt.year
age_month = now.month - born_dt.month
age_day = now.day - born_dt.day
age_hour = now.hour - born_dt.hour
print("Age is %d years %d months %d days % hours" %(age_year,age_month,age_day,age_hour))

##################################################################################

# Get time stamp
# 1506306721.4066062
now = time.time()

# Convert time stamp to local time which in Tuple type
# time.struct_time(tm_year=2017, tm_mon=9, tm_mday=25, tm_hour=10, tm_min=34, tm_sec=31, tm_wday=0, tm_yday=268, tm_isdst=0)
localtime = time.localtime(now)

# Convert time stamp to gm time which in Tuple type (utc0)
# time.struct_time(tm_year=2017, tm_mon=9, tm_mday=25, tm_hour=2, tm_min=36, tm_sec=58, tm_wday=0, tm_yday=268, tm_isdst=0)
gmtime = time.gmtime(now)

# Convert time object to strings
# "2017/09/25 10:38:39"
Stime = time.strftime("%Y/%m/%d %H:%M:%S", localtime)

# time.struct_time(tm_year=2017, tm_mon=9, tm_mday=25, tm_hour=10, tm_min=39, tm_sec=54, tm_wday=0, tm_yday=268, tm_isdst=-1)
# Convert strings object to time
Ttime = time.strptime(Stime, "%Y/%m/%d %H:%M:%S")
