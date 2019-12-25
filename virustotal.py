# -*- coding: utf-8 -*-
import webbrowser
import requests
import os
import getpass
import sys

def clean(to_scan):
    path = r'C:\Users\{}\Downloads"\"'.format(str(getpass.getuser()))
    path = path.replace('"', '')
    to_scan = str(to_scan).replace('}', '')
    to_scan = str(to_scan).replace('{', '')
    to_scan = path + str(to_scan)
    to_scan = to_scan.replace("'", '')
    return to_scan
def settings():
    if 'settings' not in os.listdir(str(os.getcwd())):
        os.makedirs(str(os.getcwd()) + '\settings')
        path = str(os.getcwd()) + '\settings'
        print(path)
        with open(path + '/settings.txt', 'w', encoding='utf-8') as f:
            api = input('Enter your api-key: ')
            f.write(api)
    else:
        settings_txt = os.getcwd() + r'\settings\settings.txt'
        with open(settings_txt, 'r', encoding='utf-8') as f:
            r = f.read(10000)
            if r != ' ' and r != '':
                print('Программу вы запускаете не в первый раз, api вы уже вводили.')
            else:
                f.close()
                with open(settings_txt, 'w', encoding='utf-8') as f:
                    api = input('Enter your api-key: ')
                    f.write(api)
def scan(filename, api):
    api_key = {'apikey': api}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files={'file': (filename, open(filename, 'rb'))}, params=api_key)
    dct = dict(response.json())
    link = dct['permalink']
    print('[ + ] Открыли файл в браузере')
    webbrowser.open(link, new=1)
def os_check():
    files_old = os.listdir(r'C:\Users\{}\Downloads'.format(str(getpass.getuser())))
    files_old = set(files_old)
    print('Скрипт в режиме ожидания')
    while True:
        files_new = os.listdir(r'C:\Users\{}\Downloads'.format(str(getpass.getuser())))
        files_new = set(files_new)
        if files_new != files_old:
            if 'подтверждено' in str(files_new):
                continue
            to_scan = files_new - files_old
            if str(to_scan) == 'set()':
                continue
            to_scan = clean(to_scan)
            if '.tmp' not in to_scan:
                api = str(os.getcwd()) + '\settings' + '\settings.txt'
                with open(api, encoding='utf-8') as f:
                    api = f.read(100000)
                    print(api)
                print(to_scan)
                try:
                    scan(to_scan, api)
                except FileNotFoundError:
                    print('Это исправимо [ - ]', to_scan)
                    to_scan = to_scan.split(',')
                    for i in to_scan:
                        if r'C:\Users\{}\Downloads'.format(str(getpass.getuser())) not in i:
                            i = r'C:\Users\{}\Downloads\"'.format(str(getpass.getuser())).replace('"', '') + i[0:i.find(' ')] + i[i.find(' ') + 1:len(i)] # проблема в том что мы упускаем один пробел
                            print(i)
                            try:
                                scan(i, api)
                            except:
                                print(i, 'Снова не правильно')
                            else:
                                print(i)
                                print('Файл который не открывался, теперь открылся')
                        else:
                            print(i)
                files_old = files_new
settings()
os_check()
