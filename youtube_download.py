from pytube import YouTube
#download video to a save path from link
#code from https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/
def youtube(SAVE_PATH, link, filename):
# where to save

# link of the video to be downloaded




    try:
    # object creation using YouTube
        yt = YouTube(link)
    except:
    #to handle exception
        print("Connection Error")

# Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4')
#mp4_list
    #mp4_list = list(mp4_streams)

# get the video with the highest resolution
    d_video = mp4_streams[-1]

    try:
    # downloading the video
        d_video.download(output_path=SAVE_PATH, filename=filename)
        print('Video downloaded successfully!')
    except IndexError:
        print("Error: No streams found or index out of range")
    except Exception as e:
        print(f"An error occurred: {e}")

