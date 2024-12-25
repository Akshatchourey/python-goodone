import os
import random
import pymysql
import tkinter as tk
from smtplib import SMTP
from datetime import datetime, timedelta
from dotenv import load_dotenv
from twilio.rest import Client
from tkinter import ttk, messagebox
from email.mime.text import MIMEText
from PIL import Image, ImageTk, ImageDraw
from email.mime.multipart import MIMEMultipart

import win32gui, win32con
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

load_dotenv()
timeout = 10
db = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="money",
    host=os.environ.get('DB_HOST'),
    password=os.environ.get('DB_PASSWORD_DEFAULT'),
    read_timeout=timeout,
    user=os.environ.get('DB_USER_DEFAULT'),
    write_timeout=timeout,
)

def database():
    return db
