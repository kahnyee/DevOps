import random as rng
import time
from time import sleep
import DataGeneration
def main():
    while True:
        Temperature = round(rng.uniform(20, 40), 1)
        Humidity = round(rng.uniform(0, 100), 1)
        EC_level = round(rng.uniform(0, 1), 0)
        pH_level = round(rng.uniform(0, 14), 0)
        light_level = round(rng.uniform(0, 1023), 0)
        DataGeneration.DataGeneration(Temperature,Humidity,EC_level,pH_level,light_level)
        sleep(2)

if __name__ == "__main__":
    main()