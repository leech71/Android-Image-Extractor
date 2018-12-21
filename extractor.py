
import os
from shutil import copyfile


full_image_names = []

image_names = []

dir_path_list = []

image_name_path = './drawable-mdpi'

image_dest_folder = './images/'

mdpi_path = '/drawable-mdpi'

hdpi_path = '/drawable-hdpi'

xhdpi_path = '/drawable-xhdpi'

xxhdpi_path = '/drawable-xxhdpi'

xxxhdpi_path = '/drawable-xxxhdpi'

image_versions_path = ['/drawable-mdpi', '/drawable-hdpi', '/drawable-xhdpi', '/drawable-xxhdpi', '/drawable-xxxhdpi']


def print_list(l):
    for item in l:
        print(item)

def create_directory(l):
    for item in l:
        filename, file_extension = os.path.splitext(item)
        
        if os.path.exists(image_dest_folder + filename) == False:
            os.mkdir(image_dest_folder + filename)
            for image_version in image_versions_path:
                os.mkdir(image_dest_folder + filename + image_version)
        image_names.append(filename)
        dir_path_list.append(image_dest_folder + filename)


def run():
    for path in image_versions_path:
        for image_name in full_image_names:
            src = '.' + path + '/' + image_name
            dest = image_dest_folder + os.path.splitext(image_name)[0] + path + '/' + image_name
            print('Copying from ' + src + ' to ' + dest)
            copyfile(src, dest)

for(dirpath, dirnames, filenames) in os.walk(image_name_path):
    full_image_names.extend(filenames)
    break # Top level directory only
for item in full_image_names:
    filename, file_extension = os.path.splitext(item)
    if file_extension[1:] == 'xml':
        full_image_names.remove(item)

# print_list(full_image_names)

create_directory(full_image_names)

run()


# Resources
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory?rq=1
# https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python