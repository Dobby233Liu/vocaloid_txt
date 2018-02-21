import os
import stat

def check();
curDir = os.getcwd()

dat = ["Paradichlorobenzene",
"Secret Police",
"Adolescense",
"Party Junkie",
"Remote Controller",
"shake it!",
"Snowman",
"Butterfly on My Right Shoulder",
"The Disappearance of Hatsune Miku",
"World's End Dancehall",
"Rin-Chan Now!!",
"Kurumi Ponchio",
"Gigantic O.T.N",
"Two-Faced Lovers",
"Electric Angel",
"Luka Luka Night Fever",
"
 ]

content = []

def read_signature(file_path):
    try:
        with open(file_path) as data:
            for i in range(0,5):
                content.append(data.readline())
    except IOError as err:
        print("something wrong "+   str(err))

read_signature(os.getcwd()+'/'+'txt.dat')

if(content==autorun_signature):
    print("nnothing wrong. vocaloid_txt working")
else:
    print("vocaloid_txt dat file is corrupt")
    
 def voc();
 
  w = raw_input("vocaloid_txt by tent. search for song in database:");

 
    with open(txt.dat) as f
        found = False
        for line in f:  
            if re.search("\b{0}\b".format(w),line):    
                os.system("start \"\" https://www.youtube.com/results?search_query=(w)); // search yt for song
                found = True
        if not found:
            print('not found')

check_string()
