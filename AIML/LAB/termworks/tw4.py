import math

def minmax(cd,ni,mt,scores,td):
    if cd==td:
        return scores[ni]

    if mt:
        left = minmax(cd+1,ni*2,False,scores,td)
        right = minmax(cd+1,ni*2+1,False,scores,td)
        print("The Maximizing value at ",cd," is ",max(left,right))
        return max(left,right)
    else:
        left = minmax(cd + 1, ni * 2, True, scores, td)
        right = minmax(cd + 1, ni * 2 + 1, True, scores, td)
        print("The Minimizing value at ", cd, " is ", min(left, right))
        return min(left,right)

scores =  [5, 2, 1, 3, 6, 2, 0, 7]
treeDepth = math.floor(math.log(len(scores),2))
print("The optimal value is ",minmax(0,0,True,scores,treeDepth))