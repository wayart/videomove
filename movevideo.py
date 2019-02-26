# -*- coding: utf-8 -*-

import shutil, os, subprocess, re

def get_shuxing(filename):
    shuxing = {}
    result = subprocess.Popen([
        "ffprobe", "-i", filename, "-v", "quiet", "-show_streams",
        "-select_streams", "v:0"
    ],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)

    x = result.stdout.read().decode()
    # print(x)
    # sx01 = re.search(r"duration=(\d*)", x)
    # shuxing['changdu'] = int(sx01.group(1))
    # sx02 = re.search(r"TAG:creation_time=(.*?)T", x)
    # shuxing['cjrq'] = sx02.group(1)
    # sx03 = re.search(r"width=(\d*)\s+height=(\d*)", x,)
    # shuxing['kuan'] = int(sx03.group(1))
    # shuxing['gao']=int(sx03.group(2))
    sx04 = re.search(r"codec_tag_string=(.*?)\s+codec_tag", x,)
    if sx04==None:
        shuxing['bianma']=None
    else:
        shuxing['bianma'] = sx04.group(1)
    return shuxing

def get_dir(path, bianma,fileType):
    '''
    :param path: 路径
	:param bianma: 视频的编码方式使用ffprobe读取
    :param fileType: 需要移动的视频文件类型（.mkv或.avi等，前面需要加.）
    :return:null
    '''

    allfilelist = os.listdir(path)

    for file in allfilelist:
        print(file, '\n')
        filepath = os.path.join(path, file)
        if filepath.endswith(fileType):
            if get_shuxing(filepath)['bianma'] == bianma:
                print('找到文件：' + filepath)
                shutil.move(filepath, distPath)
        else:
            print('不是指定格式文件或文件夹，继续查找...')


if __name__ == '__main__':
    print('''
    直接打开视频文件目录将地址栏路径复制一下，粘贴，回车
    输入要找的视频后缀要加. 比如.mp4  .avi等，回车
    输入要找的视频编码入hvc1(h265的编码)，avc1(h264的编码)等，回车
    然后打开要拷贝到的目录将地址栏复制一下，粘贴，回车
    运行需要ffmpeg中的ffprobe支持，
    想确认一下视频编码可以用ffprobe查看下codec_tag_string选项
    ''')
    path = input('请输入视频文件所在文件夹>>>>>')
    houzhui = input('请输入视频后缀名需要带点，比如.mp4等>>>>>')
    bianmaa = input('请输入视频编码，比如avc1等>>>>>')
    #复制到distPath目录，目录需先创建
    distPath = input('请输入目标文件夹>>>>>')

    get_dir(path,bianmaa,houzhui)
    input('敲回车退出')