from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special():
    year = []
     
    for i in range(1,10):
        year.append(PYBITES_BORN + timedelta(days = 100 * i ))
        year.append(PYBITES_BORN + timedelta(days = i * 365))

    return sorted(year)
    


def num_gen():
    i = 0
    while True:
        i += 1
        yield i
    
num = num_gen()
next(num)

net = input("Input your IP net, e.g. 192.168.0: " )

# define the generator
def get_nodes(net):
    for i in range(1, 6):
        yield f"{net}.{i}" #.format(net, i)

# consume it
for node in get_nodes(net):
    print('Checking IP {}'.format(node))
#    try:
#        ssh = paramiko.SSHClient()
#        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#        ssh.connect(node, username=username, password=password)
#        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /etc/hostname')
#        yield ssh_stdout.readlines()
#    finally:
#        ssh.close()
#
#    confirm = input("Do you want to continue? ")
#    if confirm == "N": exit
    
