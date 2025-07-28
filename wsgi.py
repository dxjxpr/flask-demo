#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/7/28 11:04
# @Author  : dxjxpr
# @File    : wsgi.py
# @Des     :

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app