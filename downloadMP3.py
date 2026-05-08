from pytube import YouTube
import sys
import os

os.system("clear")

loop = True

while loop:
    print("Digite [Q/q] para sair")
    url = input("URL do youtube: ")
    if(url.lower() == "q"):
        loop = False
        os.system("clear")
        sys.exit(0)
    try:
        yt = YouTube(url)
        #yt.streams.filter(file_extension="webm",only_audio=True).first().download("/home/ghost/musicas",filename=yt.title)
        print(yt.streams.filter(file_extension="webm",only_audio=True)).first().download("/home/ghost/musicas",filename=yt.title)
        print("\033[33mBaixado ==> {}\033[1;0m".format(yt.title))
    except:
        print("Não foi possivel baixar video, talvez a URL esteja errada :)")

