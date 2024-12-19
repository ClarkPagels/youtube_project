#code from https://www.geeksforgeeks.org/extract-speech-text-from-video-in-python/
import moviepy.editor as mp
import speech_recognition as sr
text = ""
def converter(video_path):
    #make video file
    video = mp.VideoFileClip(video_path)

    #make audio file
    audio_file = video.audio
    audio_file.write_audiofile("audio.wav")

    # turn audio to text
    r = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        data = r.record(source)

    f = open("textfile.txt", "x")
    text = r.recognize_google(data)
    f.write(text)
    f.close()
