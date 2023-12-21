import requests
import socket

def write_data_to_csv(group: int):
    '''Get the groups data from the API'''

    r = requests.get(f"http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid={group}")

    with open("data.csv", "w", newline='') as data:
        j = "nro,date,group,device,direction,x,y,z,zero,sensor\n"
        data.write(j)
        for i in (r.text).replace(";", ","):
            data.write(i)
            print(i, end = '')

def write_data_to_txt(group: int):
    '''Get the groups data from a specific port'''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    groupWanted = f'{group}\n'
    groupWanted = groupWanted.encode()
    s.connect(('172.20.241.9', 20000))
    s.sendall(groupWanted)

    chunks = []
    #receive the data and decode it to utf-8
    while True:
        data = s.recv(1024)
        if len(data) == 0:
            break
        chunks.append(data.decode('utf-8'))

    #Write the data to a .txt file
    with open("data.txt", "w", newline='') as data:
        for i in chunks:
            data.write(i)
            print(i, end = '')

    s.close()

if '__main__':
    '''Write the wanted groups data as .txt and/or .csv file'''
    #write_data_to_txt(3)
    write_data_to_csv(3)