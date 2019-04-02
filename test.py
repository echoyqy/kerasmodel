import numpy as np
import modulate
Y = np.random.randint(0,2,[1, 64]).astype('float32')
Y=np.array(Y)
# print(type(Y))
b=modulate.encode2d(Y)
print(b)
