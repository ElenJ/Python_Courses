# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:23:43 2019

На этой неделе мы с вами реализуем собственный key-value storage. Вашей задачей будет написать скрипт, который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).

Запись значения по ключу

> storage.py --key key_name --val value

Получение значения по ключу

> storage.py --key key_name

Ответом в данном случае будет вывод с помощью print соответствующего значения

> value

или

> value_1, value_2

если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке их добавления. Обратите внимание на пробел после запятой.

Если значений по ключу не было найдено, выводите пустую строку или None.

Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей будет считать аргументы, переданные вашей программе, и записать соответствующую пару ключ-значение в файл хранилища или вывести значения, если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json. Проверьте добавление нескольких ключей и разных значений.

Файл следует создавать с помощью модуля tempfile.
"""

import os
import sys
import json
#import tempfile
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("key")
#parser.add_argument("value")
#args = parser.parse_args()
#parser = argparse.ArgumentParser()
#parser.add_argument("-key","-k", type = str, help ="parameters - key. type - str")
#parser.add_argument("-value","-v", type = str, help ="parameters - value. type - str")
	
#args= parser.parse_args()
#if args.key is None:#
#	print("Error. -key is not defined")



#storage_path = os.path.join(r'C:\Users\Python\playground', 'storage.data')
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

arg_names = ['command', 'mykey', 'myvalue']
#sys.argv = ['bls','ad', 3]
args = dict(zip(arg_names, sys.argv))

mykey = args.get('mykey')
myvalue = args.get('myvalue')


with open(storage_path, 'r') as f:
   old_dict = (json.loads(f.read()))

#prints value, if value present in dict
if (old_dict.get(mykey, 'not in dict') == 'not in dict') and  ('myvalue' in args): #a value was passed to a new key
    old_dict.update({mykey:myvalue})    
    print(old_dict.get(mykey, 'not in dict')) 
elif (old_dict.get(mykey, 'not in dict') != 'not in dict') and  ('myvalue' in args): #key already in dict, is updated
    old_dict.update({mykey:myvalue})
    print(old_dict.get(mykey, 'not in dict')) 
elif (old_dict.get(mykey, 'not in dict') == 'not in dict') and  ('myvalue' not in args): #no value passed, key not in dict
    print(old_dict.get(mykey, 'not in dict'))
elif ('myvalue' not in args): #no value passed
    
    valuelist = [old_dict.get(mykey)]
    tag_list = []
    for i in valuelist:
        i = str(i)
        for part in i.split(','):
            #print(part)      
            tag_list.append(part.strip())    
    print(', '.join(tag_list))     
    
 
with open(storage_path, 'w') as f:
    f.write(json.dumps(old_dict, separators=(',', ':')))

