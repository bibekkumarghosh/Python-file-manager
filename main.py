# ---------- small initial sample for testing and explanation ----------

# import os, shutil

# source_dir = r'C:\Users\bibek\OneDrive\Desktop\file2'
# destination_dir = r'C:\Users\bibek\OneDrive\Desktop\file1'

# files = os.listdir(source_dir)

# for f in files:
#     shutil.move(os.path.join(source_dir, f), destination_dir)


import shutil, os

def file_manager(file_source_dir, file_destination_dir):
    source_dir = file_source_dir
    destination_dir = file_destination_dir


    file_names = os.listdir(source_dir)

    for file_name in file_names:
        if os.path.join(source_dir, file_name).endswith('.txt'):
            path = os.path.join(destination_dir, 'text')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'text'))
        
        if os.path.join(source_dir, file_name).endswith('.mp3'):
            path = os.path.join(destination_dir, 'audios')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'audios'))

        if os.path.join(source_dir, file_name).endswith('.mp4'):
            path = os.path.join(destination_dir, 'videos')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'videos'))

        if os.path.join(source_dir, file_name).endswith('.zip'):
            path = os.path.join(destination_dir, 'zip')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'zip'))

        if os.path.join(source_dir, file_name).endswith('.geojson'):
            path = os.path.join(destination_dir, 'json')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'json'))

        if os.path.join(source_dir, file_name).endswith('.pdf'):
            path = os.path.join(destination_dir, 'pdf')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pdf'))

        if os.path.join(source_dir, file_name).endswith('.jpg'):
            path = os.path.join(destination_dir, 'pictures')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pictures'))

        if os.path.join(source_dir, file_name).endswith('.png'):
            path = os.path.join(destination_dir, 'pictures')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pictures'))

        if os.path.join(source_dir, file_name).endswith('.torrent'):
            path = os.path.join(destination_dir, 'torrents')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'torrents'))

        if os.path.join(source_dir, file_name).endswith('.srt'):
            path = os.path.join(destination_dir, 'srt')
            if not os.path.exists(path):
                os.mkdir(path)
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'srt'))

        


    print('Success!!!!!')


file_manager("C:\\Users\\bibek\\Downloads", "C:\\Users\\bibek\\Downloads")

