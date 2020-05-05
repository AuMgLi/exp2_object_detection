import os
import random

train_val_percent = 1.
train_percent = 0.9

xml_file_path = './data/Annotations'
txt_save_path = './data/ImageSets'
if not os.path.exists(txt_save_path):
    os.makedirs(txt_save_path)

total_xml = os.listdir(xml_file_path)
n_samples = len(total_xml)
range_list = range(n_samples)
n_train_val = int(n_samples * train_val_percent)
n_train = int(n_train_val * train_percent)
train_val = random.sample(range_list, n_train_val)
train = random.sample(train_val, n_train)

f_train_val = open(os.path.join(txt_save_path, 'train_val.txt'), 'w')
f_train = open(os.path.join(txt_save_path, 'train.txt'), 'w')
f_test = open(os.path.join(txt_save_path, 'test.txt'), 'w')
f_val = open(os.path.join(txt_save_path, 'val.txt'), 'w')

for i in range_list:
    name = total_xml[i][:-4] + '\n'
    if i in train_val:
        f_train_val.write(name)
        if i in train:
            f_train.write(name)
        else:
            f_val.write(name)
    else:
        f_test.write(name)

f_train_val.close()
f_train.close()
f_val.close()
f_test.close()
