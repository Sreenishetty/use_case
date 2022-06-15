import os 
from datetime import datetime

FILE_NAME = 'Inventory'
fname = datetime.now().strftime(FILE_NAME + '_%Y_%m_%d_%H_%M_%S' + '.txt')

def getDf():
    with open(fname, 'a') as f:
        a = [['/etc/hosts'],['/etc/resolv.conf'],['/etc/nsswitch.conf'],['/etc/passwd'],['/etc/group'],['/etc/shadow']]
        c = [['Hosts_Entries :'],['Resolve_Entry :'],['Switch_Entry :'],['Password_Entry :'],['Group_Entry :'],['Shadow_Entry :']]
        for i,j in zip(a,c):
            # print(i,j)
            for line in os.popen("sudo cat {}".format(i[0])).readlines():
                li=line.rstrip()
                if not li.startswith("#") and li.strip():
                    # print(line)
                    f.write("{}{}".format(j[0],line))
            f.write("\n")

disk_root = getDf()