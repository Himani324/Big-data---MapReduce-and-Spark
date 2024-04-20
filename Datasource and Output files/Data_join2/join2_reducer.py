
import sys
prev_word = ' '
ABC_dict = {}
kvs = []
line_cnt = 0

for line in sys.stdin:
  line = line.strip()
  key_value = line.split('\t')

  if key_value[1] == 'ABC':
    if (key_value[0] in ABC_dict) == False:
      ABC_dict.update({key_value[0]: 0})
  else:
    kvs.append(key_value)

for key_value in kvs:
  if key_value[0] in ABC_dict:
    ABC_dict[key_value[0]] += int(key_value[1])

for (key,value) in ABC_dict.items():
  print('%s %s'%(key,value))
