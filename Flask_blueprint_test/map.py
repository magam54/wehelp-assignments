# from flask import Blueprint, render_template, abort
# from jinja2 import TemplateNotFound
from anotherone import another

def first():
    print("我是第一個檔案")
    print("name", __name__)

first()
another()