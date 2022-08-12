
# AIHUB label(.json)을 yolo label(.txt)로 변경
# test env : python 3.7

# dataset
# ├──images
# │    ├──train   ← put train images here
# │    └──val     ← put validation images here
# ├──json
# │    ├──train   ← put train labels(.json) here
# │    └──val     ← put validation labels(.json) here
# ├──labels
# │    ├──train
# │    └──val
# └──json2yolo.py  ← put this file here

# copy : cp json2yolo.py ~/Desktop/~~~~
# move : mv *.txt ~/carvis/datasets/ds1/labels/train/
# move : mv *.jpg ~/carvis/datasets/ds1/images/train/
# move : mv *.txt ~/carvis/datasets/ds1/labels/val/
# move : mv *.jpg ~/carvis/datasets/ds1/images/val/

import json
from glob import glob
from os import path

def label(i):
    # labels
    # 0 = sign / 1 = green / 2 = left / 3 = yellow / 4 = red / 5 = GA / 6 = RA / 7 = rest

    if i['class'] == 'traffic_sign': return 0
    if i['attribute'][0]['red'] == 'on':
        if i['attribute'][0]['left_arrow'] == 'on' : return 6
        return 4
    if i['attribute'][0]['yellow'] == 'on': return 3
    if i['attribute'][0]['green'] == 'on': 
        if i['attribute'][0]['left_arrow'] == 'on' : return 5
        return 1
    return 7

def convert(size, box):
    #box: coco형식 xmin , ymin , w , h
    w = (box[2] - box[0])/size[0]
    h = (box[3] - box[1])/size[1]
    x = (box[0]+ box[2])/2/size[0]
    y = (box[1]+ box[3])/2/size[1]
    w = round(w,6)
    h = round(h,6)
    x = round(x,6)
    y = round(y,6)
    if w <0 or h < 0:
        return False
    return (x,y,w,h)

def main():
    labels = []
    folder = path.dirname(path.realpath('__file__'))
    for tv in ['train', 'val']:
        n = 0
        label_list = glob('json\\'+tv+'\\*.json')
        for l in label_list:
            with open(l) as f:
                data=json.load(f)
            size = data['image']['imsize']
            file_number = data['image']['filename'][:-4]
            for i in data['annotation']:
                b=i['box']
                bb=convert(size, b)
                if bb==False:
                    continue
                file = path.join(folder, 'labels', tv, )
                label_file=open(file + '\\' + file_number + '.txt','a')
                label_number=label(i)
                line=f'{label_number} {bb[0]} {bb[1]} {bb[2]} {bb[3]}\n'
                label_file.write(line)
                label_file.close()
            n = n + 1
            print(tv, ':', n,'/',len(label_list))

if __name__ == "__main__":
    main()
