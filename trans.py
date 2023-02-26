ffmpeg_path = "D:/ffmpeg/ffmpeg.exe"

import os
for file in os.listdir("./input"):
    name = file.split('.')[0]
    os.system(f"{ffmpeg_path} -i \"./input/{file}\" \"./meme/{name}.webp\"")
print("已完成")