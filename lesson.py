import subprocess


# subprocess.run(['ls', '-al'])
# r = subprocess.run('lsaaaa', shell=True, check=True)
# print(r.returncode)
# print('###')

p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)