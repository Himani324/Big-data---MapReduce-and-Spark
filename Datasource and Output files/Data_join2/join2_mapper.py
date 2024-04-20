
import sys
for line in sys.stdin:
  line = line.strip()
  key_value = line.split(',')
  if len(key_value) > 1:
    key_in = key_value[0]
    value_in = key_value[1]
    testNum = [int(s) for s in value_in.split() if s.isdigit()]

    if len(testNum) > 0:
      print('%s\t%s' % (key_in,value_in))
    else:
      if value_in == 'ABC':
       print('%s\t%s' % (key_in,value_in))
