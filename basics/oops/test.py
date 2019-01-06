import sys
sys.path.append("/home/deepan//Documents/Codes/cpython/basics/oops/")
import sftp
from time import time
start = time()
server = sftp.Server("1","2","3","$")
server.response()
end = time()
print(end-start)
