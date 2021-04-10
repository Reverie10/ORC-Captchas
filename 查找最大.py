# -*- coding: utf-8 -*-

import os

#存放省名的文件夹
path1 = r'/Users/wuyue/Downloads/road_judge1'
#存放地址txt结尾
path2 = r'/Users/wuyue/Downloads/road_judge1/out.txt'
pro_list = os.listdir(path1)
with open(path2,'w') as f0:
    for pro in pro_list:
        if pro == '.DS_Store':
            continue
        if pro == 'out.txt':
            continue
        r_max = 0
        n_max = 0
        rln_max = 0
        print(pro)
        #r表最大
        if  not os.path.exists(path1 + '/' + pro + '/' +  'road' + '/' +  'R' + pro + '.txt'):
            os.renames(path1 + '/' + pro + '/' +  'road' + '/' + 'R' + pro + '.mid',path1 + '/' + pro + '/' +  'road' + '/' +  'R' + pro + '.txt')
        with open(path1 + '/' + pro + '/' +  'road' + '/' +  'R' + pro + '.txt') as f1:
            for link in f1:
                link = link.strip('\n').strip('\r').split(',')
                link_num = int(link[1].strip('"'))
                if link_num > r_max:
                    r_max = link_num

        #n表最大
        if not os.path.exists(path1 + '/' + pro + '/' +  'road' + '/' +  'N' + pro + '.txt'):
            os.rename(path1 + '/' + pro + '/' + 'road' + '/' +  'N' + pro + '.mid', path1 + '/' + pro + '/' +  'road' + '/' +  'N' + pro + '.txt')
        with open(path1 + '/' + pro + '/' +  'road' + '/' +  'N' + pro + '.txt') as f2:
            for link in f2:
                node = link.strip('\n').strip('\r').split(',')
                link_num = int(node[1].strip('"'))
                if link_num > n_max:
                    n_max = link_num
        #rln表最大
        if not os.path.exists(path1 + '/' + pro + '/' +  'road' + '/' + 'R_LName' + pro + '.txt'):
            os.rename(path1 + '/' + pro + '/' +  'road' + '/' + 'R_LName' + pro + '.mid', path1 + '/' + pro + '/' +  'road' + '/' + 'R_LName' + pro + '.txt')
        with open( path1 + '/' + pro + '/' +  'road' + '/' + 'R_LName' + pro + '.txt') as f3:
            for link in f3:
                link = link.strip('\n').strip('\r').split(',')
                link_num = int(link[2].strip('"'))
                if link_num > rln_max:
                    rln_max = link_num
        f0.write(pro + ':' + 'R表:' + str(r_max) + ':N表:' + str(n_max) + ':RLN表:' + str(rln_max) + '\n')

