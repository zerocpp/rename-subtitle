import os
import re

def rename_subtitles_deep_search(root_dir):
    # 定义视频和字幕文件的扩展名
    video_extensions = ['.mkv', '.mp4', '.avi']
    subtitle_extensions = ['.srt', '.ass', '.sub']

    # 用于查找SxxExx模式（季和集）的正则表达式
    pattern = re.compile(r'S\d{2}E\d{2}', re.IGNORECASE)

    # 遍历root_dir目录下的所有文件和子目录
    for root, dirs, files in os.walk(root_dir):
        video_files = {}
        # 先找到所有视频文件并记录它们的基本名（不含扩展名）和完整路径
        for file in files:
            if os.path.splitext(file)[1].lower() in video_extensions:
                match = pattern.search(file)
                if match:
                    video_files[match.group().upper()] = os.path.splitext(file)[0]

        # 再查找并重命名所有匹配的字幕文件
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in subtitle_extensions:
                match = pattern.search(file)
                if match and match.group().upper() in video_files:
                    new_subtitle_name = video_files[match.group().upper()] + file_ext
                    old_subtitle_path = os.path.join(root, file)
                    new_subtitle_path = os.path.join(root, new_subtitle_name)
                    # 重命名字幕文件
                    os.rename(old_subtitle_path, new_subtitle_path)
                    print(f"Renamed '{file}' to '{new_subtitle_name}' in directory '{root}'")



root_dir = 'Z:\\tv\\Desperate.Housewives.S01-S08.1080p.WEB-DL.DDP5.1.x264-TrollHD'
rename_subtitles_deep_search(root_dir)