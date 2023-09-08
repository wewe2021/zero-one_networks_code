import numpy as np 
def checkN(N,s,r): #'N' is the stoichiomatric matrix of the network G, 's' is the number of species of G and 'r' is the number of reactions of G
    N=np.array(N)
    c = 1 # c=1 represents that N satisfies the requirement
    s = N.shape[0]
    print(f"The rank of N is {np.linalg.matrix_rank(N)}.")
    if np.linalg.matrix_rank(N) == 1:
        for i in range(s):
            if np.all(N[i, :] == 0):
                continue
            elif (np.size(np.where(N[i, :] < 0)) != 0) and (np.size(np.where(N[i, :] > 0)) != 0):
                break
            else:
                c = 0
                break
    else:
        for i in range(s - 1):
            for j in range(i + 1, s):
                 if np.linalg.matrix_rank([N[i,:],N[j,:]]) == 1:
                     continue
                 else:
                     Nbase=np.vstack((N[i,:],N[j,:]))
                     break
                    
        if (np.size(np.where(Nbase[1, :] < 0)) != 0) and (np.size(np.where(Nbase[1, :] > 0)) != 0) and (np.size(np.where(Nbase[0, :] < 0)) != 0) and (np.size(np.where(Nbase[0, :] > 0)) != 0):
            if (np.size(np.where(Nbase[1, :]+Nbase[0,:] < 0)) != 0) and (np.size(np.where(Nbase[1, :]+Nbase[0,:] > 0)) != 0) and (np.size(np.where(Nbase[1, :]-Nbase[0,:] < 0)) != 0) and (np.size(np.where(Nbase[1, :]-Nbase[0,:] > 0)) != 0):
                c=1
            else:
                c=0
        else:
            c=0
    if c==0:
        print("The network has no positivve steady state.")
    else:
        print("There exist parameters such that the network has positive steady state.")
        
        
