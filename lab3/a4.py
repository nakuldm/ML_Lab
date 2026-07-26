def minkowski_dist(x,y,p):
    distance = 0
    for i in range(len(x)):
        distance += abs(x[i] -y[i]) ** p
    return distance ** (1/p)

p1 = [1,2,3]
p2 = [3,6,7]

d1=minkowski_dist(p1, p2, 1)
d2=minkowski_dist(p1, p2, 2)

print("p=1:", d1)
print("p=2:", d2)