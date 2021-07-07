import os
import shutil
from pathlib import Path

downloads_path = os.path.join(Path.home(), "Downloads")
print(downloads_path)
dir_list = os.listdir(downloads_path)

extension_types_set = set()
for file in dir_list:
    file_path = os.path.join(downloads_path, file)
    if os.path.isfile(file_path):
        file_name, file_extension = os.path.splitext(file)
        extension_types_set.add(file_extension)
        destination_path = ''
        if file_extension == '.pem':
            destination_path = os.path.join(downloads_path, "Certificates")
        elif file_extension.upper() == '.JPG' or file_extension.upper() == '.PNG':
            destination_path = os.path.join(downloads_path, "Images")
            # {'.docx', '.drawio', '.JPG', '.msi', '.zip', '.exe', '.ppk', '.ini', '.jpg', '.pdf', '.xlsx'}
        elif file_extension == '.xlsx' or file_extension == '.pdf' or file_extension == '.docx':
            destination_path = os.path.join(downloads_path, "Documents")
        elif file_extension == '.exe' or file_extension == '.ini' or file_extension == '.msi':
            destination_path = os.path.join(downloads_path, "Executables")
        elif file_extension == '.zip' or file_extension == '.rar':
            destination_path = os.path.join(downloads_path, "Zip")
        elif not file_extension:
            destination_path = os.path.join(downloads_path, "Others")

        print("file_path", file_path)
        print("destination_path", destination_path)

        if destination_path != '':
            print("dest not empty")
            if not os.path.isdir(destination_path):
                os.mkdir(destination_path)
            shutil.move(file_path, destination_path)
print(extension_types_set)
