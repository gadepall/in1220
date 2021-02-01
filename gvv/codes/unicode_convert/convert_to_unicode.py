#Code by Chakkirala Anish
#Revised by G V V Sharma
#January 30, 2021


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Function for  extracting relevant data from the text


def get_sloka_from_stothram(stothram_txt):
  slokams = []
  for sloka in stothram_txt.split('॥'):
    if not sloka.replace(' ', '').isnumeric() and not sloka == '\n' and not sloka == '':
      slokams.append( sloka.replace('|', '').replace('\n', '') )
  return slokams

#def get_sloka_from_stothram(stothram_txt):
#  slokams = []
#  for sloka in stothram_txt.split('||'):
#    if not sloka.replace(' ', '').isnumeric() and not sloka == '\n' and not sloka == '':
#      slokams.append( sloka.replace('|', '').replace('\n', '') )
#  return slokams


#Obtaining patterns from the text
def gen_patterns(slokams):
  global pattern_list
  for sloka in slokams:
    temp = {}
    for words in sloka.split():
      for char in words:
        if char in temp.keys():
          temp[char] = temp[char] + 1
        else:
          temp[char] = 1 
    pattern_list.append(temp)


# to read the mahishasura mardini sloka file
stothram_file = open('hindi/aigiri.txt', 'r')
stothram_txt = stothram_file.read()
stothram_file.close()

# to read the hanuman chalisa file
chalisa_file = open('hindi/hanuman_chalisa.txt', 'r')
chalisa_txt = chalisa_file.read()
chalisa_file.close()

pattern_list = []

aigiri = get_sloka_from_stothram(stothram_txt)
chalisa = get_sloka_from_stothram(chalisa_txt)


gen_patterns(aigiri)
gen_patterns(chalisa)


df = pd.DataFrame(pattern_list).fillna(0)

print(df)
#print(aigiri)
#print(chalisa)
