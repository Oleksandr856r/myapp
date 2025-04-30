import streamlit as st
import requests
import threading
import time
import socket
from flask_server import run_flask

@st.cache_resource
def start_flask():
    def run():
        run_flask()
    t = threading.Thread(target=run, daemon=True)
    t.start()
    time.sleep(2)

# Перевірка, чи порт зайнятий
def is_port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex((host, port)) == 0

# Запуск Flask, якщо ще не працює
if not is_port_open("localhost", 8000):
    start_flask()

st.title("Streamlit + Flask")

if st.button("Отримати дані з Flask API"):
    try:
        response = requests.get("http://localhost:8000/api/hello")
        st.json(response.json())
    except Exception as e:
        st.error(f"Помилка підключення: {e}")
