# This is a sample Python script.



import plotly.graph_objs as go

import cgi
# Create instance of FieldStorage
form = cgi.FieldStorage()
forme = cgi.FieldStorage()
formee= cgi.FieldStorage()

# Get data from fields
from Polar_codes_BEC import Polar_bec

#this function init variabls
Polar_bec.__init__(0)

#this function help users to enter values
(p,n)=Polar_bec.input_p_n(0)
#p=0.7
#n=8
Polar_bec.BEC_graph(p,n)

def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
