import csv
from pathlib import Path

ROOTH_PATH = Path(__file__).parent

with open(ROOTH_PATH / 'example.csv', "w", newline="", encoding='UTF-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["nome", "idade"])
    writer.writerow(["ana", "18"])
    writer.writerow(["maria", "78"])
    