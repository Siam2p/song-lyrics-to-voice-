import time
import threading
import pyttsx3

lyrics = [
    "Ooh",
    "I, I just woke up from a dream",
    "Where you and I had to say goodbye",
    "And I don't know what it all means",
    "But since I survived, I realized",
    "Wherever you go, that's where I'll follow",
    "Nobody's promised tomorrow",
    "So I'ma love you every night like it's the last night",
    "Like it's the last night",
    "If the world was ending, I'd wanna be next to you",
    "If the party was over and our time on Earth was through",
    "I'd wanna hold you just for a while and die with a smile",
    "If the world was ending, I'd wanna be next to you",
    "Ooh",
    "Ooh, lost, lost in the words that we scream",
    "I don't even wanna do this anymore",
    "Cause you already know what you mean to me",
    "And our love's the only war worth fighting for",
    "Wherever you go, that's where I'll follow",
    "Nobody's promised tomorrow",
    "So I'ma love you every night like it's the last night",
    "Like it's the last night",
    "If the world was ending, I'd wanna be next to you",
    "If the party was over and our time on Earth was through",
    "I'd wanna hold you just for a while and die with a smile",
    "If the world was ending, I'd wanna be next to you",
    "Right next to you",
    "Next to you",
    "Right next to you",
    "Oh-oh, oh",
    "If the world was ending, I'd wanna be next to you",
    "If the party was over and our time on Earth was through",
    "I'd wanna hold you just for a while and die with a smile",
    "If the world was ending, I'd wanna be next to you",
    "If the world was ending, I'd wanna be next to you",
    "Ooh",
    "I'd wanna be next to you"
]

def sing_lyrics(lyrics):
  def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(text)
    engine.runAndWait()

  for line in lyrics:
    t = threading.Thread(target=speak, args=(line,))
    t.start()
    for char in line:
      print(char, end='', flush=True)
      time.sleep(0.1)
    t.join()
    time.sleep(0.5)
    print()

sing_lyrics(lyrics)