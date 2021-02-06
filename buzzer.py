import RPi.GPIO as GPIO
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

from signal import pause
from time import sleep


## buzzer on GPIO16
# my_buzzer = Buzzer(16)
my_tonebuzzer = TonalBuzzer(16)
# my_tonebuzzer.play(540.0)
melody=['C4','D4','E4','F4','G4','A4','B4','C5']
i=0
while True:
    i=0
    my_tonebuzzer.play(melody[i])
    sleep(0.25)
    i=i+1

# my_tonebuzzer.play(Tone("A4"))
# my_tonebuzzer.play(Tone(220.0))
# my_tonebuzzer.play(Tone(60))
# my_tonebuzzer.play("A4")
