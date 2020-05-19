import io
import requests
import zipfile


# with open('/tmp/a.txt', 'w') as f:
#     f.write('test test')
#
# with open('/tmp/a.txt', 'r') as f:
#     print(f.read())
#
# f = io.BytesIO()
# f.write(b'string io test')
# f.seek(0)
# print(f.read())

url = ('https://files.pythonhosted.org/packages/ac/d6/0f6c0d9d0b07bbb2085e94a71aded1e1'
       '37c7c9002ac54924bc1c0adf748a/setuptools-46.4.0.zip')

f = io.BytesIO()

r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
       with z.open('setuptools-46.4.0/README.rst') as r:
              print(r.read().decode())
