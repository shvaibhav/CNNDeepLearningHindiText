#  last character- ']'
# utf
import json
import csv
import re
from itertools import *
#import StringIO
#import unicodecsv


with open('regional1.txt') as fr, open('sports.txt') as fs, \
open('bollywood.txt') as fb, open('gallery.txt') as fg, \
open('gadgets.txt') as fga, open('money.txt') as fm, \
open('jokes.txt') as fj, open('lifestyle.txt') as fl, \
open('magazines.txt') as fmag, open('abhivyakti.txt') as fabhi, \
open('international.txt') as finter, open('national.txt') as fnat, \
open('states.txt') as fstates, open('jeevan_mantra.txt') as fjeev, \
open('regional2.txt') as fr2:
  data_region = fr.read().splitlines()
  data_sports = fs.read().splitlines()
  data_bolly = fb.read().splitlines()
  data_gal = fg.read().splitlines()
  data_gadget = fga.read().splitlines()
  data_money = fm.read().splitlines()
  data_jokes = fj.read().splitlines()
  data_life = fl.read().splitlines()
  data_mag = fmag.read().splitlines()
  data_abhi = fabhi.read().splitlines()
  data_inter = finter.read().splitlines()
  data_national = fnat.read().splitlines()
  data_states = fstates.read().splitlines()
  data_jeev = fjeev.read().splitlines()
  data_region2 = fr2.read().splitlines()





input_file1 = 'news_art_headlines_append_mode.json'
input_file2 = 'news_art_text_append_mode.json'
input_file3 = 'news_classes_append_mode.json'

output_file = 'output.csv'


#############

def func(data):
  if data[0:2] == '[[':
    data = data[1:]
  data = data.replace('}{', '},{')
  data = data.replace('}[{', '},{')
  if data[-1] == '\n':
    print 'last character newline'
    data = data[0:len(data)-1]
  if data[-1] == ',':
    print 'last character comma'
    data = data[0:len(data)-1]
  if data[-1] == '\'':
    print 'last character quote'
    data = data + '}]'
  if data[-1] == '}':
    print 'last character }'
    data = data + ']'
  if data[-3] != '"':
    print 'third last character is not equal to double quotes'
    data = data[0:len(data) - 2] + '"}]'
  return data


with open(input_file1) as f1, open(input_file2) as f2, open(input_file3) as f3:
#    data1 = json.load(f1)
  data_f1 = f1.read()
  data_f2 = f2.read()
  data_f3 = f3.read()

data_f1 = func(data_f1)
data_f2 = func(data_f2)
data_f3 = func(data_f3)

data1 = json.loads(data_f1)
data2 = json.loads(data_f2)
data_class = json.loads(data_f3)

############




#with open(input_file1) as f1, open(input_file2) as f2, open(input_file3) as f3:
#    data1 = json.load(f1)
#    data2 = json.load(f2)
#    data_class = json.load(f3)


data3=list()
for ele in data1:
  temp_data=''
#  temp = re.findall('(\\\\u[a-zA-Z0-9_]{4})+\s', repr(ele.values()[0]))
  temp = repr(ele.values()[0])
  temp = temp.replace('\\n',' ')
  temp = re.findall('(\\\\u[a-zA-Z0-9]{4}\s*)?', temp)
  temp = filter(bool, temp)
  for item in temp:
    item_new = item.decode('unicode_escape').encode('utf-8')
    temp_data = temp_data + (item_new)
  temp_data = ' '.join(temp_data.split())
  data3.append(temp_data)

data4=list()
for ele in data2:
  temp_data = ''
  temp = repr(ele.values()[0])
#  temp = re.findall('\\\\u[a-zA-Z0-9_]{4}', repr(ele.values()[0]))
  temp = temp.replace('\\n',' ')
  temp = re.findall('(\\\\u[a-zA-Z0-9]{4}\s*)?', temp)
  temp = filter(bool, temp)
  for item in temp:
    item_new = item.decode('unicode_escape').encode('utf-8')
    temp_data = temp_data + (item_new)
  temp_data = ' '.join(temp_data.split())
  data4.append(temp_data)


region_list = data_region + data_region2
data_res_class = list()
for ele in data_class:
  if ele.values()[0] in region_list:
    class_id = 1
    data_res_class.append(class_id)
  else:
    class_id = 2
    data_res_class.append(class_id)

 

all_elements = list()
all_elements_temp = list()
for ele1, ele2, ele3 in izip(data3, data4, data_res_class):
  all_elements.append([ele3, ele1, ele2])
#  all_elements_temp.append(ele2)

###########

# with open('temp1.csv', "wb") as f:
# #  writer = unicodecsv.writer(f, encoding='utf-8')
# #  writer = csv.writer(f)
#   for item in all_elements_temp:
# #    writer.writerow(item)
#     new_item = item.replace('\\', '\\\\')
#     f.write(repr(new_item))
###########


# with open('temp.csv', 'wb') as f:
# #  writer = unicodecsv.writer(f, encoding='utf-8')
#   writer = csv.writer(f)
#   for item in all_elements_temp:
# #    new_item = item.replace('\n', '\r\n')
#     writer.writerow((item))


with open(output_file, "wb") as f:
  writer = csv.writer(f, delimiter=',')
  writer.writerows(all_elements)

# with open(output_file2, "wb") as f:
#   writer = csv.writer(f)
#   writer.writerows(all_elements_temp)

#dict_text = json.loads(content)

# id = 0
# with open("/home/vaibhav/Documents/Spring2015/AI2_project/DainikBhaskar/output.csv", "wb") as f:
#   writer = csv.writer(f)
#   for ele in data:
#     temp = list()
#     temp.append(id)
#     temp.append(ele.values()[0].encode('utf-8'))
#     writer.writerow(temp)
