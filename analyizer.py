import moviepy.editor as mp
import speech_recognition as sr
from pytube import YouTube

def VideoToText(directory,link,filename):
    path = directory + "/" + filename
    
    yt = YouTube(link)
    yt = yt.get('mp4', '720p')
    yt.download(directory + "/" + filename)

    video = mp.VideoFileClip(path)
    audio = video.audio

    audio.write_audiofile('audio.wav')

    r=sr.Recognizer()

    with sr.AudioFile("audio.wav") as source:
        data = r.record(source)

    f = open("{filename}", "w+")
    text = r.recognize_google(data)
    f.write(text)
    f.close()
