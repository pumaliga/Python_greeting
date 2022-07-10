import os
from datetime import datetime
from time import sleep
import yaml


name = os.popen('whoami').read()


def say_hello(name):
    data = f"[{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] Hi {name}\n"
    return data


def get_delay():
    with open('config.yaml', 'r') as s:
        try:
            data = yaml.safe_load(s)
            delay = float(data['delay_in_sec'])
        except yaml.YAMLError as exc:
            print(exc)
    return delay


def write_data(data):
    f = open('logs/data.txt', 'a+')
    f.write(data)
    f.close()
    print(data)


while True:
    write_data(say_hello(name))
    sleep(get_delay())


