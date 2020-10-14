import tinytag
import sys
import os

basepath = sys.argv[1]

def mkdir(path):
 
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            filedir = entry.path
            try:
                tag = tinytag.TinyTag.get(filedir)
            except tinytag.tinytag.TinyTagException:
                pass
            track_num = tag.track 
            track_name = tag.title
            track_album = tag.album         # album as string
            track_albumartist = tag.albumartist   # album artist as string
            track_artist = tag.artist
            track_samplerate = tag.samplerate 
            track_year = tag.year 
            file_ext = os.path.splitext(entry.name)[-1][1:]
            print(entry.name,track_num,track_name,track_artist,track_album,track_year,track_samplerate)
            track_num = track_num.zfill(2)
            track_samplerate = track_samplerate / 1000
            track_samplerate = int(track_samplerate)
            track_samplerate = str(track_samplerate)
            new_file_name = track_num + " - " + track_name + "." + file_ext
            album_dirname = track_artist + " - " + track_album + " ("+ track_year +") [" + file_ext.upper() + "," + track_samplerate + "kHz]"
            mkdir(os.path.join(basepath,album_dirname))
            os.rename(filedir,os.path.join(basepath,album_dirname,new_file_name))
            print("rename " + track_name + " success!")


