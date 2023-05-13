import numpy as np

def norm_l2(x):
    return np.sqrt(sum(x**2))

if __name__ == '__main__':
    x = np.array([-4,-3,-2,-1,0,1,2,3,4])
    print(norm_l2(x),np.linalg.norm(x),sum(np.abs(x)))
