import numpy as np

def fitness_function_1(position):
    # print("position =  {}".format(position))
    x=[]
    for i in range(13):
        x.append(position[i])
    t1,t2,t3 = 0,0,0
    for i in range(4):
        t1 += x[i]
        t2 += x[i]*x[i]
    for i in range(4,13):
        t3 += x[i]
    fitness_value = 5*t1 - 5*t2 - t3
    #calculate constraint violation
    g = [0]*9
    g[0] = 2*x[0] + 2*x[1] + x[9] + x[10] - 10
    g[1] = 2*x[0] + 2*x[2] + x[9] + x[11] - 10
    g[2] = 2*x[1] + 2*x[2] + x[10] + x[11] - 10
    g[3] = -8*x[0] + x[9]
    g[4] = -8*x[1] + x[10]
    g[5] = -8*x[2] + x[11]
    g[6] = -2*x[3] - x[4] + x[9]
    g[7] = -2*x[5] - x[6] + x[10]
    g[8] = -2*x[7] - x[8] + x[11]
    #returning a very large value if any constraint is violated
    for i in range(9):
        if g[i] > 0:
            return g[i]*10000000000
    return fitness_value

def fitness_function_3(position):
    x=[]
    for i in range(7):
        x.append(position[i])
    fitness_value = (x[0]-10)**2 + 5*(x[1]-12)**2 + x[2]**4 + 3*(x[3]-11)**2 + 10*x[4]**6 + 7*x[5]**2 + x[6]**4 - 4*x[5]*x[6] - 10*x[5] - 8*x[6]    #calculate constraint violation
    g = [0]*4
    g[0] = -127 + 2*x[0]**2 + 3*x[1]**4 + x[2] + 4*x[3]**2 + 5*x[4]
    g[1] = -282 + 7*x[0] + 3*x[1] + 10*x[2]**2 + x[3] - x[4]
    g[2] = -196 + 23*x[0] + x[1]**2 + 6*x[5]**2 - 8*x[6]
    g[3] = 4*(x[0]**2) + x[1]**2 - (3*(x[0]*x[1]))+ 2*(x[2]**2) + 5*x[5] - (11*x[6])
    for i in range(4):
        if g[i]>0:
            return g[i]*10000000000
    return fitness_value

def pressure_vessel(position):
    x=[]
    for i in range(4):
        x.append(position[i])
    fitness_value = 0.6224*x[0]*x[2]*x[3] + 1.7781*x[2]*x[2]*x[1] + 3.1661*x[0]*x[0]*x[3] + 19.84*x[0]*x[0]*x[2]
    #calculate constraint violation
    g = [0]*4
    g[0] = -x[0] + 0.0193*x[2]
    g[1] = -x[1] + 0.00954*x[2]
    g[2] = - (np.pi) * x[2] * x[2] * x[3] - (4/3)*(np.pi)*x[2]*x[2]*x[2] + 1296000
    g[3] = x[3] - 240
    for i in range(4):
        if g[i]>0:
            return np.inf
    return fitness_value

if __name__ == "__main__":
    position =  [0.7782311976715822, 0.3846808337948571, 40.322792450592225, 199.95621723943196] 
    print("fitness_value = {}".format(pressure_vessel(position)))
