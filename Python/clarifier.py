import io,os, baba_yaga, sys
from baba_yaga import L, LT
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdout = open(F'{baba_yaga.output_file}', 'w')



x = 22
print(f"{x.zfill(3)}",end="\n")