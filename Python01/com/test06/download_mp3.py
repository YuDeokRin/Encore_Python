# -*-coding:utf-8 -*-

#pip install pytube3

from pytube import YouTube
from glob import glob
from os import path,mkdir,rename


#
target_url = input('url :')
download_path = 'mp3'

if not path.exists(download_path):
    mkdir(download_path)
    print('mkdir :', download_path)
else:
    print('exists')
 
   
    
#   
target = YouTube(target_url)

try:
    target.streams.filter(only_audio=True).first().download(download_path)
    print('download success')
except:
    print('download fail')



#
rename(glob(download_path+ '/*.mp4')[0], download_path+'/'+target.title.replace('/', '_')+'mp3')
print('mp4 to mp3')