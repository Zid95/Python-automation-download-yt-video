from pytube import YouTube 



youtube_obj = YouTube("video link")

print("Title: ", youtube_obj.title)

print("View: ", youtube_obj.views)

quality = youtube_obj.streams.get_highest_resolution()


# save video path here
quality.download(" $save video path$ ")