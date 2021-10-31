import urllib.request
import re
import os
import youtube_dl

filePath = os.getcwd()+'\\Musics'
if not os.path.exists(filePath):
    os.mkdir(filePath)
filePath += '\\'

f = open("music.txt", "r")
for i in f:
    data = i.split()
    url = ''
    for j in data:
        if j != data[-1]:
            url += j + '+'
        else:
            url += j

    html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    videoURL = 'https://www.youtube.com/watch?v='+video_ids[0]

    options={
        'writethumbnail': True,
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filePath+'%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([videoURL])

f.close()
