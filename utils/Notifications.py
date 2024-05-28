import requests

def send_push_notification():
    requests.post('https://marmoset-select-barnacle.ngrok-free.app/send/')