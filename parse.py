import os,sys
def load_file(file):
    if not os.path.exists(file):
        sys.exit("{0} not found".format(file))
    with open(file, 'rt') as f:
        data = f.read()
        return data

if (len(sys.argv) < 2):
    sys.exit('please give me log\nExample: python test.py /home/httpd/access.log') 

file_path = sys.argv[1]
data = load_file(file_path)
iplist = {}  # create an empty dict
for line in data.split('\n'):
    if line != "":
        line = line.split()[0]   # remove newline.
    else:
        continue
    if line: # if not a blank line.
        iplist.setdefault(line, 0) # check for ip and add with default value of 0
        iplist[line] += 1 # increment

top_5 = sorted(iplist.items(), key=lambda x: x[1], reverse=True)[:5]
for top in top_5:
    print("""IP: {} \t COUNT: {} """.format(top[0],top[1]))
