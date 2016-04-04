import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

# need to use double quotes and a "b" around the .send method to make it
# work in python 3 because py3 needs us to switch the unicode string to a byte string
mysock.send(b"GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n")

while True:
    data = mysock.recv(512).decode() # need to use decode to switch the byte string back to unicode
    if ( len(data) < 1 ) :
        break
    print (data);

mysock.close()
