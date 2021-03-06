import string

list= []
before = []
after = []
pindex = -1;
def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Korean/Raw Dataset/Jiwon/020020.cha") as data:
        for lines in data:
            if lines.startswith("*MOT"):
                lines = lines.replace("*MOT:\t","")
                for charac in lines:
                    if(charac == ','):
                        lines = lines.replace(' , ','|')
                        continue
                    if(charac in string.punctuation):
                        pindex = lines.index(charac)
                lines = lines[:pindex]
                before.append(lines)
                lines = lines.replace(" ","|")
                lines ='.'.join(i for i in lines)
                lines = lines.replace(".|.","|")
                list.append(lines)

        for a,b in zip(before, list):
            after.append(a+"    "+b)

def generate_file():
    f = open("Jiwon_020020_gold.txt","x")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
