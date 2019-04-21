import requests
from flask import Flask, request, send_file, make_response

# url = (loadable link with the text file)

def get_url():
    input_path = cpu_dir + 'users/users.txt'
    input_file = open(input_path, 'rt')
    contents = input_file.read()
    url = contents.rstrip()
    input_file.close()
    return str(url)

def new_download(filename):
    get_url()
    r = requests.get(url, allow_redirects = True)
    open(filename, 'wb').write(r.content)

def download_data(url, filename):
    r = requests.get(url, allow_redirects = True)
    open(filename, 'wb').write(r.content)
    return
