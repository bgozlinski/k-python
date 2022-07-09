from kalk_v3 import make_opperation
import logging

logging.basicConfig(level=logging.DEBUG, filename="kalkulator.logs")
logger = logging.getLogger(__name__)

#  odczytaj dane z data.txt i wykonaj obliczenie zgodnie z zawartoscia wierszy
#  wiersze zbudowane sa wg schematu
#  operacja a b

try:
    with open("data.txt") as f:
        data = f.readlines()

        for line in data:
            operation, a, b = line.split()
            print(f"{a} {operation} {b} = {make_opperation(int(a), int(b), operation)}")
except:
    logger.error("Wstapil blad", exc_info=True)
