import numpy as np
class polar_bec:
    # to use this librairy you must import nmpy like bellow: import numpy as np
    def init(self):

        global f, i
        f = []
        i = 0
        s = []

    def bec_cal(P, L):
        # P is the ereasure probability
        # L is level of polarisation they start from one
        if L == 1:
            print('test')
            P1 = P * P
            P2 = P * (2 - P)

            context = {
                'P1': P1,
                'P2': P2,

            }
            f.append(P1)
            f.append(P2)
            # print("f is ", f)
            return (P1, P2)
        else:
            return (bec_cal(P * P, L - 1), bec_cal(P * (2 - P), L - 1))


