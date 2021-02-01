# -*- coding: utf-8 -*-
"""frequency.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wCpcjbgVgPgR4ZyKiRhXBluRD3lyjaWb
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd drive/MyDrive/'Colab Notebooks'/slokam_pattern

import matplotlib.pyplot as plt

uni_file = open('unicode_test1.txt', 'r')
uni_txt = uni_file.read()
uni_file.close()

uni_chars = uni_txt.split()
periodicity_found = []
periodicity = {}
processed_periodic_dict = {}

def to_cal_periodicity(char, index):
    count = 0
    temp = uni_chars[index+1:]
    for j in temp:
        if j == char:
            periodicity[char].append(count)
            count = 0
        else:
            count = count + 1

def to_process_dict(periodicity_dict):
    dict_keys = periodicity_dict.keys()
    
    for key in dict_keys:
        if len(periodicity_dict[key]) == 0:
            average = 0
        else:
            average = sum(periodicity_dict[key])/len(periodicity_dict[key])
        key = key.replace('U+', '')
        key = key[:1] + 'x' + key[1:]
        processed_periodic_dict[chr(int(key, 16))] = average 

def plot_bar(periodicity_dict):
    keys = list(periodicity_dict.keys())
    values = list(periodicity_dict.values())
    keys = [ hex(ord(i)).replace('x', '') for i in keys ]

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 5, 5])
    ax.bar(keys, values)
    plt.show()

for i, char in enumerate(uni_chars):
    if char in periodicity_found:
        pass
    else:
        periodicity_found.append(char)
        periodicity[char] = []
        to_cal_periodicity(char, i)

print(periodicity)
to_process_dict(periodicity)
print(processed_periodic_dict)
plot_bar(processed_periodic_dict)

test1_result = processed_periodic_dict

uni_file = open('unicode_test2.txt', 'r')
uni_txt = uni_file.read()
uni_file.close()

uni_chars = uni_txt.split()
periodicity_found = []
periodicity = {}
processed_periodic_dict = {}

for i, char in enumerate(uni_chars):
    if char in periodicity_found:
        pass
    else:
        periodicity_found.append(char)
        periodicity[char] = []
        to_cal_periodicity(char, i)

to_process_dict(periodicity)
plot_bar(processed_periodic_dict)

test2_result = processed_periodic_dict

common_keys = []
keys1 = list(test1_result.keys())
keys2 = list(test2_result.keys())

for i in keys1:
  if i in keys2:
    common_keys.append(i)

key_value_1 = {}
key_value_2 = {}

for i in common_keys:
  key_value_1[i] = test1_result[i]
  key_value_2[i] = test2_result[i]

plot_bar(key_value_1)

plot_bar(key_value_2)

import numpy as np
x_pos = np.linspace(0, 9, 41)

barWidth = 0.05
fig = plt.subplots(figsize =(20, 20)) 


 
plt.bar(x_pos, list(key_value_1.values()), color ='r', width = barWidth, 
		edgecolor ='grey', label ='Trained') 
plt.bar(x_pos + barWidth, list(key_value_2.values()), color ='g', width = barWidth, 
		edgecolor ='grey', label ='Latter') 
plt.show()