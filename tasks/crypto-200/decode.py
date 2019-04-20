import base64
with open('b64.txt', 'rb') as b64:
    out = open('flagg.zip', 'wb')
    out.write(base64.b64decode(b64.read()))
    out.close()