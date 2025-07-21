import numpy as np

def gauss_elimination(a_matrix,b_matrix):
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Error! Please input square matrix")
        return
    if a_matrix.shape[0] != b_matrix.shape[0]:
        print("Error not enough equation for the solution")
        return
    augmented_martrix=np.concatenate((a_matrix,b_matrix),axis=1,dtype=float)

    print(f"augmented matrix is {augmented_martrix}")
    i = 0
    j = 0
    n = 0
    n=len(b_matrix)
    m=0
    p=0
    x=np.zeros(n)
    while i<n:
        for j in range(i+1,n):
            scaling_factor= augmented_martrix[j][i]/augmented_martrix[i][i]
            augmented_martrix[j]=augmented_martrix[j]-(scaling_factor* augmented_martrix[i])
        i=i+1
    print(f"augmented matrix is: {augmented_martrix}")
    m=augmented_martrix.shape[1]
    x[n-1]=augmented_martrix[n-1][m-1]/augmented_martrix[n-1][n-1]
    for p in range(n-2,-1,-1):
        sum=0
        for k in range(p+1,n):
            sum=sum+augmented_martrix[p][k]*x[k]
        x[p]=(augmented_martrix[p][n]-sum)/augmented_martrix[p][p]

    print(f"solution is: {x}")

variable_matrix=np.array([[1,5,8,5],[2,6,5,8],[5,1,2,4],[1,4,6,8]])
constant_matrix=np.array([[1],[5],[8],[2]])
gauss_elimination(variable_matrix,constant_matrix)

