import os 
import shutil

current_dir = 'C:/Users/skyem/Downloads'
if os.getcwd() == current_dir:
    print('right directory')
else:
    os.chdir('C:/Users/skyem/Downloads')
    print('i changed directory')
    print('current on -->' + os.getcwd())

def exe():
    aux = os.listdir()
    exe = []
    for x in aux:
        if 'exe' in x:
            print('um arquivo exe')
            exe.append(x)

    print(exe)
    for x in exe:
        shutil.move('C:/Users/skyem/Downloads/' + x, 'C:/Users/skyem/Downloads/exe')

def rar():
    aux = os.listdir()
    rar = []
    if 'Arquivos RAR' in aux:
        print('ja existe pasta rar neste diretorio')
    else:
        os.mkdir('Arquivos RAR')
    for x in aux:
        if 'rar' in x:
            print('um arquivo rar')
            rar.append(x)

    print(rar)
    for x in rar:
        shutil.move('C:/Users/skyem/Downloads/' + x, 'C:/Users/skyem/Downloads/Arquivos RAR')

def img_png():
    aux = os.listdir()
    img = []
    for x in aux:
        if 'png' in x:
            print('um arquivo img')
            img.append(x)
    print(img)
    for x in img:
        shutil.move('C:/Users/skyem/Downloads/' + x,'C:/Users/skyem/Pictures')

def img_jpg():
    aux = os.listdir()
    img = []
    for x in aux:
        if 'jpg' in x:
            print('um arquivo img')
            img.append(x)
    print(img)
    for x in img:
        shutil.move('C:/Users/skyem/Downloads/' + x,'C:/Users/skyem/Pictures')

def mp3():
    aux = os.listdir()
    mptres = []
    for x in aux:
        if 'mp3' in x:
            print('um arquivo mp3')
            mptres.append(x)
    print(mptres)
    for x in mptres:
        shutil.move('C:/Users/skyem/Downloads/' + x,'C:/Users/skyem/Music')

def pdf():
    aux = os.listdir()
    pdf = []
    for x in aux:
        if 'pdf' in x:
            print('um arquivo pdf')
            pdf.append(x)
    print(pdf)
    for x in pdf:
        shutil.move('C:/Users/skyem/Downloads/' + x,'C:/Users/skyem/Documents/General PDFs')

def mp4():
    aux = os.listdir()
    mpquatro = []
    for x in aux:
        if 'mp4' in x:
            print('um arquivo mp4')
            mpquatro.append(x)
    print(mpquatro)
    for x in mpquatro:
        shutil.move('C:/Users/skyem/Downloads/' + x,'C:/Users/skyem/Videos')

exe()
rar()
img_png()
img_jpg()
mp3()
pdf()
mp4()
