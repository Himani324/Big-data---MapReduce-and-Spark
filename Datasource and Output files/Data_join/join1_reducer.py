
import sys
prev_word = ' '
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dates_to_output = []
day_cnts_to_output = []
line_cnt = 0

for line in sys.stdin:
  line_cnt = line_cnt + 1
  line = line.strip()
  key_value = line.split('\t')
  curr_word = key_value[0]
  value_in = key_value[1]

  if (curr_word != prev_word) and (line_cnt > 1):
    for i in range(len(dates_to_output)):
      print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))
    dates_to_output = []
    day_cnts_to_output = []
  if value_in[0:3] in months:
    date_day = value_in.split()
    dates_to_output.append(date_day[0])
    day_cnts_to_output.append(date_day[1])
  else:
    curr_word_total_cnt = value_in
  prev_word = curr_word
for i in range(len(dates_to_output)):
  print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))
