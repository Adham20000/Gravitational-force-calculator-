#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Hey..\nI'm going to help you calculate the Gravitational force.")
G = float(input("Enter the Gravity: "))
M = float(input("Enter the Earth's mass: "))
m = float(input("Enter the Moon's mass: "))
r = float(input("Enter the radius: "))
Fg = (G * M * m) / (r * r)

print("Your inputs:\n G: {}\n M: {}\n m: {}\n r: {}".format(G, M, m, r))
print("The Gravitational force is:", Fg)

