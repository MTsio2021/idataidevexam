import os, numpy

mult = int(os.environ["a"]) * int(os.environ["b"])

print(mult)

log1 =  numpy.log(int(os.environ["a"]) * int(os.environ["b"]))
log2 =  numpy.log(int(os.environ["a"])) + numpy.log(int(os.environ["b"]))

print(log1)
print(log2)