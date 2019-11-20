#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:17:19 2019

@author: elena
Чтобы передавать данные между функциями, модулями или разными системами используются форматы данных. 
Одним из самых популярных форматов является JSON. Напишите декоратор to_json, который можно применить к различным функциям, 
чтобы преобразовывать их возвращаемое значение в JSON-формат. Не забудьте про сохранение корректного имени декорируемой функции.
"""
import json
#import functools


def to_json(func):
  #  @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper

@to_json
def get_data():
    return {
            'data': 42
    }
  
get_data()  # вернёт '{"data": 42}'

