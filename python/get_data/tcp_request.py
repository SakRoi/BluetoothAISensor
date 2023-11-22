import requests
import socket

def write_data_to_csv(group: int):
    r = requests.get(f"http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid={group}")

    with open("data.csv", "w", newline='') as data:
        j = "nro,date,group,device,direction,x,y,z,zero,sensor\n"
        data.write(j)
        for i in (r.text).replace(";", ","):
            data.write(i)
            print(i, end = '')

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

    with open("data.txt", "w", newline='') as data:
        for i in chunks:
            data.write(i)
            print(i, end = '')

    s.close()

if '__main__':
    #write_data_to_txt(3)
    write_data_to_csv(3)