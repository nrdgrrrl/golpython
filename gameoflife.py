from apps.gol.grid import Grid
from machine import Pin, SPI
import apps.lib.st7789py as st7789
import random
from time import sleep

DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 135

tft = st7789.ST7789(
    SPI(2, baudrate=40000000, sck=Pin(36), mosi=Pin(35), miso=None),
    135,
    240,
    reset=Pin(33, Pin.OUT),
    cs=Pin(37, Pin.OUT),
    dc=Pin(34, Pin.OUT),
    backlight=Pin(38, Pin.OUT),
    rotation=0,
    color_order=st7789.BGR
    )

print("Initializing grid...")
grid = Grid(DISPLAY_WIDTH, DISPLAY_HEIGHT)
print("Initializing with patterns...")
glider_pattern = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

blinker_pattern = [
    [1, 1, 1]
]

toad_pattern = [
    [0, 1, 1, 1],
    [1, 1, 1, 0]
]

beacon_pattern = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]

pulsar_pattern = [
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
]



print("initializing patterns")
grid.initialize_with_patterns([glider_pattern, beacon_pattern, blinker_pattern, toad_pattern, pulsar_pattern,glider_pattern, beacon_pattern, blinker_pattern, toad_pattern, pulsar_pattern,glider_pattern, beacon_pattern, blinker_pattern, toad_pattern, pulsar_pattern])
#print("initializing random")
#grid.initialize_random()
grid.display_contents(tft)

generation_count = 0
while True:
    #print("Evolving generation:", generation_count)
    grid.evolve()
    #print("Updating display...")
    grid.display_contents(tft)
    generation_count += 1
    #sleep(10)
