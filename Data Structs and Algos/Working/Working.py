def maxNumberOfBalancedShipments(weights):
    numberofships=0
    n = len(weights)
    if(n<=1):
        return 0
    testarr = [weights[0]]
    for x in range(1,n):
        testarr.append(weights[x])
        if(len(testarr)>1 and testarr[-1]<max(testarr)):
            numberofships += 1
            testarr = []
    return numberofships

if __name__ == "__main__":
    weights = [5,4,3,2,1]
    print (maxNumberOfBalancedShipments(weights))