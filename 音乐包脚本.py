# -*- coding: utf-8 -*-
# @Time : 2022/9/21 18:39
# @Author : sanchez
# @File : main
# @Software : Pycharm Community Edition
import os
import uuid

if os.path.exists('music') and os.path.exists('project'):
    print('项目结构完整')
    pass
else:
    print('项目结构不完整')
    input('回车以结束......')
    quit()

project_f_list = os.listdir('project')
for i in project_f_list:
    temp = os.path.splitext(i)
    if temp[1] == '.masterbundle':
        fd = os.open('project/MasterBundle.dat', os.O_RDWR | os.O_CREAT)
        os.write(fd, str.encode('Asset_Bundle_Name {}.masterbundle'.format(temp[0]) + '\n' + 'Asset_Prefix Assets/{}'.format(
            temp[0]) + '\n' + 'Asset_Bundle_Version 3'))
        os.close(fd)
        if not os.path.exists('project/{}'.format(temp[0])):
            os.mkdir('project/{}'.format(temp[0]))
        music_list = os.listdir('music')
        for n in music_list:
            music = os.path.splitext(n)
            if not os.path.exists('project/{}/{}'.format(temp[0], music[0])):
                os.mkdir('project/{}/{}'.format(temp[0], music[0]))
                fd = os.open('project/{}/{}/English.dat'.format(temp[0], music[0]), os.O_RDWR | os.O_CREAT)
                os.write(fd, str.encode('Name {}'.format(music[0])))
                os.close(fd)
                fp = os.open('project/{}/{}/{}.asset'.format(temp[0], music[0], music[0]), os.O_RDWR | os.O_CREAT)
                s = str.encode('"Metadata"' + '\n' + '{' + '\n' + '    "GUID" "{}"'.format(uuid.uuid4().hex) + '\n' + '    "Type" "SDG.Unturned.StereoSongAsset, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null"' + '\n' +'}' + '\n' + '"Asset"' + '\n' + '{' + '\n' + '    "ID" "0"' + '\n' + '    "Title"' + '\n' + '    {' + '\n' + '        "Namespace" "SDG"' + '\n' + '        "Token" "Stereo_Songs.Unlike_Pluto0.Title"' + '\n' + '    }' + '\n' + '    "Song"' + '\n' + '    {' + '\n' + '        "MasterBundle" "{}.masterbundle"'.format(temp[0]) + '\n' + '        "AssetPath" "{}"'.format(n) + '\n' + '    }' + '\n' + '}')
                os.write(fp, s)
                os.close(fp)
        with open('project/music_list.txt', 'w' , encoding='utf-8') as f:
            count = 1
            for i in music_list:
                f.write(str(count) + '.' + i + '\n')
                count += 1


input('回车以结束......')