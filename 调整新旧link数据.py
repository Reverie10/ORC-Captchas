
import random


#更改调整数据
path1 = '/Users/wuyue/Downloads/road_judge1/shandong1/road/Rshandong1_1.txt'
path2 = '/Users/wuyue/Downloads/mid-mif合并/Rshandong1.txt'
path3 = '/Users/wuyue/Downloads/mid-mif合并/Rshandong1_2.txt'
with open(path1,'w') as f1:
    with open(path2) as f2:
        for f in f2:
            link_list = f.strip('\n').split(',')
            daoludengji = link_list[2]
            xiansu = link_list[24]
            a = random.randint(2,14)
            if a == 10:
                link_list[2] = '22222222222222'
                link_list[24] = '1111111111111'
            f1.write(','.join(link_list) + '\n')
new_dict = {}
with open(path1) as f3:
    for link in f3:
        link_list = link.split('\n').split(',')
        new_dict[link_list[1]] = link.strip('\n')
with open(path3,'w') as f5:
    with open(path2) as f4:
        for link in f4:
            link_list = link.strip('\n').split(',')
            if link_list[1] in new_dict:
                f5.write(new_dict[link_list[1]] + '\n')
            else:
                f5.write(link)
