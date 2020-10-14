# rename_music

Rename files according to the metadata in the file and move them to a subdirectory named after the album name.

根据文件中的元数据重命名文件,并移动到以专辑名称命名的子目录中.

Supported audio formats.

支持的音频格式：
https://github.com/devsnd/tinytag


## 安装和使用

`git clone https://github.com/TinyFlag/rename_music.git`

安装依赖,进入仓库文件夹后：

`pip install -r requeriments.txt`

打开命令行,进入仓库文件夹后输入

`python rename_music.py `

然后将需要处理的音乐所在文件夹拖入窗口,或输入路径,运行后即可完成整理.

## Installation and usage

`git clone https://github.com/TinyFlag/rename_music.git`

`pip install -r requeriments.txt`

`python rename_music.py {path2musicfile}`

## Naming conventions

file name:

``` track_num - track_name ```

directory name:

``` track_artist - track_album (track_year) [ file_ext, track_samplerate kHz] ```