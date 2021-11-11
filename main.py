import os
import shutil

from cfg import main_dir
from cfg import list_cmds

current_dir = r''
main_path = main_dir
status = False


# ИЗМЕНИТЬ НАЗВАНИЯ КОМАНД
def menu():
    global current_dir
    global main_path
    while True:
        cmd = input('Введите вашу команду, help - для помощи: ').split()

        if cmd[0] == 'help':  # ПОМОЩЬ
            print(list_cmds)

        elif cmd[0] == 'mkdir':  # СОЗДАНИЕ ПАПКИ
            try:
                create_dir(cmd[1])
            except Exception as e:
                print(e)
            except IndexError:
                print('Неверно введена команда!')

        elif cmd[0] == 'dldir':  # УДАЛЕНИЕ ПАПКИ
            try:
                delete_dir(cmd[1])
            except Exception as e:
                print(e)
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'goto':  # выход на уровень - up или название папки
            try:
                if cmd[1] == 'up':
                    if current_dir != main_path:
                        current_dir = '/'.join(current_dir.split('/')[:-1])
                        where()
                    else:
                        print('Вы не можете покинуть установленную корневую папку!')
                else:
                    current_dir = main_path + '\\' + cmd[1]
                    where()
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'mkfile':
            try:
                mkfile(cmd[1])
            except IndexError:
                print('Неверно введена команда')
            except:
                print('Невозможно создать такой файл')

        elif cmd[0] == 'wrt':
            try:
                write(cmd[1], ' '.join(cmd[2:]))
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'open':
            try:
                read(cmd[1])
            except:
                print('Неверно введена команда')
        elif cmd[0] == 'del':
            try:
                rmfile(cmd[1])
            except Exception as e:
                print(e)
            except:
                print('Неверно введена команда')


        elif cmd[0] == 'copy':
            try:
                move_cp(cmd[1], cmd[2], cmd[3])
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'move':
            try:
                move(cmd[1], cmd[2])
                rmfile(cmd[1])
            except:
                print('Неверно введена команда')


        elif cmd[0] == 'rename':
            try:
                rename(cmd[1], cmd[2])
            except:
                print('Неверно введена команда')


        elif cmd[0] == 'where':
            where()


        elif cmd[0] == 'exit':
            break


        else:
            print('Неверная команда, введите заново!')


def create_dir(name):
    os.mkdir(current_dir + '/' + name)


def delete_dir(name):
    os.rmdir(current_dir + '/' + name)


def read(name):
    f = open(current_dir + '/' + name, 'r')
    text = f.readlines()
    f.close()
    for i in text:
        print(i, end='')


def write(name, text):
    print(text)
    f = open(current_dir + '/' + name, 'w')
    f.write(text)
    f.close()


def mkfile(name):
    my_file = open(current_dir + '/' + name, "w+")


def rmfile(name):
    os.remove(current_dir + '/' + name)


def rename(name, newname):
    os.rename(current_dir + '/' + name, newname)


def move(name, path):
    shutil.move(current_dir + '/' + name, current_dir + '/' + path)


def move_cp(name, path, newname):
    shutil.move(current_dir + '/' + name, current_dir + '/' + path)
    os.rename(current_dir + '/' + path + '/' + name, newname)


def where():
    print(f'Вы находитесь здесь {current_dir}')


if __name__ == "__main__":
    if main_path == r'' or not (os.path.exists(main_path)):
        status = False
        main_path = input('Введите существующий доступный путь к файлу')
    else:
        status = True
        current_dir = main_dir
        menu()
