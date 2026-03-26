start = input()
end = input()

starttime = int(start[0:2])*3600 + int(start[3:5])*60+int(start[6:8])
endtime = int(end[0:2])*3600 + int(end[3:5])*60+int(end[6:8])

realtime = endtime - starttime
if realtime < 0:
    realtime += 86400 
real_hour = realtime // 3600
real_minute = (realtime - real_hour*3600) // 60
real_second = (realtime - real_hour*3600 - real_minute*60)

print(f'{real_hour:02}:{real_minute:02}:{real_second:02}')