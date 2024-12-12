import moviepy.editor as mp
import speech_recognition as sr
from pytube import YouTube

def VideoToText(directory,link,filename):
    path = directory + "/" + filename
    
    yt = YouTube(link)
    yt = yt.get('mp4', '720p')
    yt.download(directory + "/" + filename)
