#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('Sarah', 'F')
enroll('Sarah', 'F', age = 7)
enroll('bob','M', city = 'Shanghai')
enroll('Hi','M')
