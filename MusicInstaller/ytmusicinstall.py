import youtube_dl
from youtube_search import YoutubeSearch
import csv
import os


def dlfromyt(songname, artists):
    folder = 'E:\\AIProjectFrontEnd\\music'
    results = YoutubeSearch(songname+' '+artists +
                            ' song', max_results=1).to_dict()
    song = results[0]

    yt_url = 'https://youtube.com'+song['url_suffix']
    title = song['title']

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(folder, f'{songname}.mp3'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([yt_url])
        except:
            pass


def readfile():

    with open('spotify.csv', encoding="utf8") as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            if count == 0:
                count = 1
                pass
            elif count > 25000:
                if (len(row[12].split()) > 1):
                    # print(row[12].split())
                    dlfromyt(row[12], row[1])
            count += 1


def main():
    readfile()


main()
