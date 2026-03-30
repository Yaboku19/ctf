import base64
import zlib

cookie = ".eJwty0sKgCAQANC7zFoCP-joZUJqEsEfaqvo7rlo--A9kGoIdIKDy6dBwKDOtg86Os2FaLn6bcZMY_rcwHFjFFothN6kREQhGNyDevGZVvJnjgXeD0hWHG8.acrEYg.SLRxaSyracFyX3pmeEQDvlieb_s"
parts = cookie.split(".")
payload = next(p for p in parts if p) 

# fix padding
payload += "=" * (-len(payload) % 4)

decoded = base64.urlsafe_b64decode(payload)

# try decompress (Flask sometimes compresses)
try:
    decoded = zlib.decompress(decoded)
except:
    pass

print(decoded)