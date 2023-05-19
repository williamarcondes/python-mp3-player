from pygame import mixer

mixer.init()
print("Que musica deseja tocar?")
musica = input()
mixer.music.load(musica)

print("Tocando sua musica")
mixer.music.play()

input()