'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: upload.py
@time: 2020/8/24 0024 22:22
@desc:
'''
# from application.utils import photos,files,log


# 配置参数使用UPLOADED_ + UploadSet.name + _DEST这种形式
# UPLOADED_FILES_DEST = xxx
# UPLOADED_PHOTOS_DEST = xxx

# def save_photo_file(file):
#     try:
#         filename = photos.save(file)
#         # 返回文件路径
#         file_url = photos.url(filename)
#         basename = photos.get_basename(filename) #文件名
#         path = photos.path(filename)
#         print('file_url =', file_url)  # http://127.0.0.1:8000/_uploads/photos/1525269617847e958494e4a.jpg
#         print('basename =', basename)  # 1525269617847e958494e4a.jpg
#         print('path =', path)  # uploads\1525269617847e958494e4a.jpg
#         return path
#     except Exception as e :
#         log.error('save_photo_file - error - {}'.format(e))