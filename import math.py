import math
u=math.sqrt(12.4*(math.e)**2 + 0.6*(math.e)**(-1)*math.sqrt(0.0548)/0.389*(math.log(3)+math.sin(1)))
v=math.tan(5*math.tan(math.sqrt(3)/3)-1/4*math.sin(math.sqrt(3)/2))
if abs(u)<abs(v):
    l=(3*u+v)/(u**2+v**2)
else:
    l=u*v
print(l)