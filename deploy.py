#!/usr/bin/env python
# coding=utf-8
'''
Author: Johannes Liu
LastEditors: Johannes Liu
email: iexkliu@gmail.com
github: https://github.com/johannesliu
Date: 2023-03-28 18:10:39
LastEditTime: 2023-03-28 18:13:37
motto: Still water run deep
Description: Modify here please
FilePath: \ReDevOps\deploy.py
'''

import os 

os.system("mdbook build")

os.system("git add -A")
os.system('git commit -m "update"')
os.system("git push")