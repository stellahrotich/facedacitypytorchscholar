#getting started with pytorch
#tensors

from __future__ import print_function
import torch

#create a 5x3 matrix, uninitialized:
x = torch.empty(5, 3)
print(x)

#create a randomly initialized matrix:
x = torch.rand(5, 3)
print(x)

#create a matrix filled zeros and of dtype long:
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

#construct a tensor directly from data:
x = torch.tensor([5.5, 3])
print(x)

# new_* methods take in sizes
x = x.new_ones(5, 3, dtype=torch.double)    
print(x)

#override dtype!
x = torch.randn_like(x, dtype=torch.float)    
print(x)  

#get size of a tensor
print(x.size())

#tensor addition syntax1
y = torch.rand(5, 3)
print(x + y)

#tensor addition syntax2
print(torch.add(x, y))

#providing tensor output as an argument
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

#addition in place
# adds x to y
y.add_(x)
print(y)

#indexing just like in numpy
print(x[:, 1])

#resize.reshape tensor
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

#to get python as a value nummber
x = torch.randn(1)
print(x)
print(x.item())



#Tensor has operations, including transposing, indexing, slicing, mathematical operations, linear algebra, random numbers
# let us run this cell only if CUDA is available
# We will use ``torch.device`` objects to move tensors in and out of GPU
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!
    b = a.numpy()
print(b)

#output after changing to array
a.add_(1)
print(a)
print(b)

#convering numpy array to tensor torch
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

Tensors can be moved onto any device using the .to method.
    
 #The autograd package provides automatic differentiation for all operations on Tensors
 #torch.Tensor is the central class of the package
 
 #track all operations 
 .requires_grad #set it as True
 
 #to finish tracking operations
 .backward()
 
 #stop
 .detach()
 

#converting a tensor torch to array
a = torch.ones(5)
print(a)





