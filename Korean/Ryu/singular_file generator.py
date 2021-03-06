from fileinput import filename
import os
lines = []
my_dir = os.getcwd()
excluded_files = 'Ryu_train_gold.txt .DS_Store Ryu.txt 0metadata.cdc Ryu_test_gold.txt singular_file generator.py Ryu_test.txt Ryu_train_unseg.txt Ryu_train.txt Ryu_test_unseg.txt'
for subdir, dirs, files in os.walk(my_dir):
    #print(subdir,files)
    for fname in files:
        if(fname != "010600c.cha"):
            print(fname)
            with open(os.path.join(subdir,fname), "r", encoding='utf-8', errors='ignore') as fin:
                for line in fin:
                    line.strip()
                    if line.startswith("*MOT") and line.find('[/]') == -1 and line.find('(') == -1:
                        lines.append(line)

# for e in lines:
#     print(e)
f = open("../Ryu_train.txt","w")
g = open("../Ryu_test.txt","w")

eighty = (int)(len(lines)*0.8)
for e in lines[:eighty]:
    f.write(e+"")

for e in lines[eighty:]:
    g.write(e+"")

