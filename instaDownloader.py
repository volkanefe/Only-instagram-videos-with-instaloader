import instaloader, os
print("Downloading media")
profile_name="excel.egitim" # instagram account name
instaloader.Instaloader(
    download_videos=True,
    download_comments=False,
    download_geotags=False,
    download_pictures=False,
    download_video_thumbnails=False,
    save_metadata=False,
    compress_json=False,
).download_profile(profile_name, profile_pic=False, profile_pic_only=False)

for file in os.listdir(profile_name):
    if file.endswith('.txt'):
        file_path=os.path.join(profile_name,file)
        os.remove(file_path)
print("Download Completed")