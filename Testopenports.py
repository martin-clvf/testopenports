import sys
import csv
import socket

def is_port_open(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False

def test_ports(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = next(reader)
        headers.append('Port Open')
        rows = []
        for row in reader:
            ip = row[0]
            ports = row[1:]
            results = []
            for port in ports:
                results.append(str(is_port_open(ip, int(port))).lower())
                print("ip : ", ip, "port : ", port, "result : ", results[-1])
            row += results
            rows.append(row)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(headers)
            writer.writerows(rows)

if __name__ == '__main__':
    test_ports(sys.argv[1])
