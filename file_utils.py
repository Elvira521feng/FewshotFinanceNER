# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 6:46 下午
# @Author  : JiangYanQun
# @File    : file_utils.py


def get_file_name_base_on_postfix(dir_path, postfix):
    r"""
    在dir_path中寻找后缀为postfix的文件.
    :param dir_path: str, 文件夹
    :param postfix: 形如".bin", ".json"等
    :return: str，文件的路径
    """
    files = list(filter(lambda filename: filename.endswith(postfix), os.listdir(os.path.join(dir_path))))
    if len(files) == 0:
        raise FileNotFoundError(f"There is no file endswith {postfix} file in {dir_path}")
    elif len(files) > 1:
        raise FileExistsError(f"There are multiple *{postfix} files in {dir_path}")
    return os.path.join(dir_path, files[0])