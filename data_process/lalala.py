import os


folder_path = '/datas/wanglin/learn_code/Video-ChatGPT-main/data_process/video_data'
    # 获取文件夹中的所有文件名
file_names = os.listdir(folder_path)

for file_name in file_names:
    old_file_path = os.path.join(folder_path, file_name)

    new_file_name = file_name[:-4] + ".avi.pkl"
    print(new_file_name)
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)
    