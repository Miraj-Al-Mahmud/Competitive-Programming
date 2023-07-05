import io,os, baba_yaga, sys
from baba_yaga import L, LT
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdout = open(F'{baba_yaga.output_file}', 'w')



k = '1 2 3 4 5 6 7 9 10 12 13 15 16 17 18 19 20 21 22 23 24 25 27 28 29 31 33 36 37 38 39 41 42 43 44 45 47 49 50 51 52 54 57 58 59 60 73 74 76 77 79 80 83'
l = k.split()
print(f"{len(l)}",end="\n")