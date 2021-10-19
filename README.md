## POLAR CODES ANLYSIS IN BINARY EREASURE CHANNEL
A demo library for polar codes in BEC about publishing librairies
### installation
```
pip install Polar_codes_BEC
```
#### GET STARTED
#### the effect of polar codes in BEC
```Python
from Polar_codes_BEC import Polar_bec

# this function init  variabls
Polar_bec.__init__(0)
# p is the ereasure probability
p=0.5
# n is the polar code length
n=4

#result
print('the new erasure probability values is',Polar_bec.BEC(p,n))

```
#### Simulation & Plotting
A function to simulate a defined polar code in BEC,
``` python
#this function help users to enter values
(p,n)=Polar_bec.input_p_n(0)
#p=0.7
#n=8
Polar_bec.BEC_graph(p,n)
```
The simulation will show the polar code result for example:
``` Python
Please enter the ereasure probability:
0.5
the ereasure probability is 0.5 

Please enter the code length:
8
the code  length is 8

after polarization we get 4 of bad channels : [0.68359375, 0.80859375, 0.87890625, 0.99609375]
after polarization we get 4 of good channels : [0.00390625, 0.12109375, 0.19140625, 0.31640625]
```

