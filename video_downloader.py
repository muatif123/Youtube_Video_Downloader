# Importing the module
from pytube import YouTube

# Ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video(seconds): ",yt.length)
print("Rating of video: ",yt.rating)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download('D:/Projects Python/Youtube Video Downloader')
print("Download completed!!")
