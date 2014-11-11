import os
import shutil
import tempfile

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
MYCVS = SOURCE_DIR + '/mycvs.py'

TEST_DIR = tempfile.mkdtemp()
print('tempfile returned', TEST_DIR)


def start_test():
    os.chdir(TEST_DIR)


def end_test():
    pass


def test_init_creates_directory_mycvs_if_not_existed():
    start_test()

    command_line = 'C:/Python33/python.exe ' + MYCVS + ' init'
    print('Running:', command_line)
    os.system(command_line)
    print(os.listdir(TEST_DIR))
    if os.path.isdir('mycvs'):
        print('Test passed')
    else:
        print('Test failed')

    end_test()


test_init_creates_directory_mycvs_if_not_existed()