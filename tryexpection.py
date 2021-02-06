#!/usr/bin/python3

try:
    'hello'+113
except TypeError:
    print('\n字串不能加整數拉！會不會啦！\n')
except:
    print('\n發生不明錯誤！ 囧')