#!/usr/bin/python3.2

file = open('/sys/class/thermal/thermal_zone0/temp', 'r')

raw_temp = file.readline()
cel_string = raw_temp[0] + raw_temp[1] + '.' + raw_temp[2]
cel_float = float(cel_string)
far_float = (cel_float*1.8000) + 32.00
far_raw_s = str(far_float)
far_arr = far_raw_s.split('.')
print(cel_string + "'C")
print(far_arr[0] + "." + far_arr[1][0] + "'F")
