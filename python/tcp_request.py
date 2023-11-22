import requests
import csv
import socket

def write_data_to_csv(group: int):
    r = requests.get(f"http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid={group}")

    with open("python/data.csv", "w", newline='') as data:
        inputData = csv.writer(data, delimiter=' ',
                             quoting=csv.QUOTE_MINIMAL)
        inputData.writerow(r.text)

def write_data_to_txt(group: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    groupWanted = f'{group}\n'
    groupWanted = groupWanted.encode()
    s.connect(('172.20.241.9', 20000))
    s.sendall(groupWanted)

    chunks = []
    while True:
        data = s.recv(1024)
        if len(data) == 0:
            break
        chunks.append(data.decode('utf-8'))

    with open("python/data.txt", "w", newline='') as data:
        for i in chunks:
            data.write(i)
            print(i, end = '')

    s.close()

if '__main__':
    write_data_to_txt(3)
    write_data_to_csv(3)