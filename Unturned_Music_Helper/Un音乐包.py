# -*- coding: utf-8 -*-
# @Time : 2022/9/21 18:38
# @Author : sanchez
# @File : main
# @Software : Pycharm Community Edition
import os
import uuid


def helper():
    print('欢迎使用Unturned音乐包脚本\n*Unmusic文件夹存入音乐源文件*\n*Unproject文件夹存入Unity导出的文件*')


def check():
    if os.path.exists('Unmusic'):
        if os.path.exists('Unproject'):
            print('项目结构完整')
            return True
        else:
            print('项目结构不完整，自动重构')
            os.mkdir('Unproject')
            return False
    else:
        if os.path.exists('Unproject'):
            print('项目结构不完整，自动重构')
            os.mkdir('Unmusic')
            return False
        else:
            print('项目结构不完整，自动重构')
            os.mkdir('Unmusic')
            os.mkdir('Unproject')
            return False


def start():
    project_f_list = os.listdir('Unproject')
    music_list = os.listdir('Unmusic')
    for i in project_f_list:
        temp = os.path.splitext(i)
        if temp[1] == '.masterbundle':
            fd = os.open('Unproject/MasterBundle.dat', os.O_RDWR | os.O_CREAT)
            os.write(fd, str.encode(
                'Asset_Bundle_Name {}.masterbundle'.format(temp[0]) + '\n' + 'Asset_Prefix Assets/{}'.format(
                    temp[0]) + '\n' + 'Asset_Bundle_Version 3'))
            os.close(fd)
            if not os.path.exists('Unproject/{}'.format(temp[0])):
                os.mkdir('Unproject/{}'.format(temp[0]))
            for n in music_list:
                music = os.path.splitext(n)
                if not os.path.exists('Unproject/{}/{}'.format(temp[0], music[0])):
                    os.mkdir('Unproject/{}/{}'.format(temp[0], music[0]))
                    fd = os.open('Unproject/{}/{}/English.dat'.format(temp[0], music[0]), os.O_RDWR | os.O_CREAT)
                    os.write(fd, str.encode('Name {}'.format(music[0])))
                    os.close(fd)
                    fp = os.open('Unproject/{}/{}/{}.asset'.format(temp[0], music[0], music[0]), os.O_RDWR | os.O_CREAT)
                    s = str.encode('"Metadata"' + '\n' + '{' + '\n' + '    "GUID" "{}"'.format(
                        uuid.uuid4().hex) + '\n' + '    "Type" "SDG.Unturned.StereoSongAsset, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null"' + '\n' + '}' + '\n' + '"Asset"' + '\n' + '{' + '\n' + '    "ID" "0"' + '\n' + '    "Title"' + '\n' + '    {' + '\n' + '        "Namespace" "SDG"' + '\n' + '        "Token" "Stereo_Songs.Unlike_Pluto0.Title"' + '\n' + '    }' + '\n' + '    "Song"' + '\n' + '    {' + '\n' + '        "MasterBundle" "{}.masterbundle"'.format(
                        temp[0]) + '\n' + '        "AssetPath" "{}"'.format(n) + '\n' + '    }' + '\n' + '}')
                    os.write(fp, s)
                    os.close(fp)
            with open('Unproject/music_list.txt', 'w', encoding='utf-8') as f:
                count = 1
                for k in music_list:
                    f.write(str(count) + '.' + k + '\n')
                    count += 1


if __name__ == '__main__':
    print('检查项目结构')
    checked = check()
    helper()
    if checked:
        input('回车以继续...')
        start()
        input('运行完毕，回车以退出...')
    else:
        print('***请按照项目结构存放文件再启动脚本***')
        input('回车以退出...')
