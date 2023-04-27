import numpy as np
import random

cities = np.array([
    [0,12,22,15,21,21,15,21,21],
    [12,0,8,11,13,13,11,13,13],
    [22,8,0,16,18,18,16,18,18],
    [15,11,16,0,19,19,16,19,19],
    [21,13,18,19,0,14,19,20,20],
    [21,13,18,19,14,0,12,12,21],
    [15,11,16,16,19,12,0,22,13],
    [21,13,18,19,20,12,22,0,18],
    [21,13,18,19,20,21,13,18,0]
])

n_cities = len(cities)

n_population = 10
randomnumber = 0
mutation_rate = 0.5
AllChromoseme = []
Allfitness = []
AllllChrom = []


def genesis():
    for i in range(n_cities):
        sol_i = np.random.choice(list(range(1,10)), 9, replace=False)
        AllChromoseme.append(list(sol_i))
        AllllChrom.append(list(sol_i))



def calcFitness():
    for i in range(len(AllllChrom)):
        distance = 0
        for j in range(len(AllllChrom[i])):
            if j+1 > (len(AllllChrom[i])-1):
                firstcity = (AllllChrom[i][0]) - 1
                distance += cities[(AllllChrom[i][j]-1)][firstcity]
            else:
                distance += cities[(AllllChrom[i][j])-1][(AllllChrom[i][j+1])-1]    
        Allfitness.append(distance)


def randomSelect():
    global randomnumber
    randomnumber = random.randint(0,len(AllChromoseme)-1)
    return AllChromoseme[randomnumber]

def randomMutation(chrom):
    randomindex = random.randint(0,len(chrom)-1)
    randomindex2 = random.randint(0,len(chrom)-1)
    if(random.random() < mutation_rate):
        temp = chrom[randomindex]
        chrom[randomindex] = chrom[randomindex2]
        chrom[randomindex2] = temp


def findMissingNumbers(arr,N):
    temp = [0] * (N+1)
 
    for i in range(0, N):
        temp[arr[i] - 1] = 1
 
    for i in range(0, N+1):
        if(temp[i] == 0):
            ans = i + 1
    return ans


def crossOver(a,b):  
    
    chrom1 = a
    chrom2 = b  
    OrderA = chrom1[0:3]
    OrderB = chrom2[0:3]
    for i in range(len(OrderB)):
        for j in range(len(chrom1)):
            if OrderB[i] == chrom1[j]:
                chrom1[j] = OrderA[i]
    for i in range(len(OrderA)):
        for j in range(len(chrom2)):
            if OrderA[i] == chrom2[j]:
                chrom2[j] = OrderB[i]
    
    
    for i in range(len(OrderA)):
        chrom2[i] = OrderA[i]
    for i in range(len(OrderB)):
        chrom1[i] = OrderB[i]  
    
    
    randomMutation(chrom1)
    randomMutation(chrom2)

 
    
    numberofduplicate = 0
    numberofduplicate2 = 0

    for i in range(0,len(chrom1)):
        for j in range(i+1,len(chrom1)):
            if chrom1[i] == chrom1[j]:
                numberofduplicate += 1
                
    for i in range(0,len(chrom2)):
        for j in range(i+1,len(chrom2)):
            if chrom2[i] == chrom2[j]:
                numberofduplicate2 += 1

    if numberofduplicate > 0:
        numbermissin1 = findMissingNumbers(chrom1,len(chrom1)-1)
        for i in range(0,len(chrom1)):
            for j in range(i+1,len(chrom1)):
                if chrom1[i] == chrom1[j]:
                    chrom1[j] = numbermissin1
                    
    if numberofduplicate2 > 0:
        numbermissin2 = findMissingNumbers(chrom2,len(chrom2)-1)
        for i in range(0,len(chrom2)):
            for j in range(i+1,len(chrom2)):
                if chrom2[i] == chrom2[j]:
                    chrom2[j] = numbermissin2
    
    #last index
    if chrom1[len(chrom1)-1] == chrom1[len(chrom1)-2]:
        numbermissin1 = findMissingNumbers(chrom1,len(chrom1)-1)
        if random.random() > 0.5:
            chrom1[len(chrom1)-2] = numbermissin1
        else:
            chrom1[len(chrom1)-1] = numbermissin1

    if chrom2[len(chrom2)-1] == chrom2[len(chrom2)-2]:
        numbermissin2 = findMissingNumbers(chrom2,len(chrom2)-1)
        if random.random() > 0.5:
            chrom2[len(chrom2)-2] = numbermissin2
        else:
            chrom2[len(chrom2)-1] = numbermissin2      
    
    AllChromoseme.append(chrom1)
    AllChromoseme.append(chrom2)
    AllllChrom.append(chrom1)
    AllllChrom.append(chrom2)



def main():
    genesis()
    print(AllllChrom)
    print(Allfitness)
    print()
    
    for i in range(500):
        a = randomSelect()
        AllChromoseme.pop(randomnumber)
        b = randomSelect()
        AllChromoseme.pop(randomnumber)
        crossOver(a,b)
        

    bestChoreme = AllllChrom[0]    
    calcFitness()
    bestfitness = Allfitness[0]
    for i in range(0,len(Allfitness)):
        if bestfitness > Allfitness[i]: 
            bestChoreme = AllllChrom[i]
            bestfitness = Allfitness[i]      
    
    
    print(AllllChrom)
    print(Allfitness)
    print()
    print("Best Distance =")
    print(bestfitness)
    print("Best Chrome =")
    print(bestChoreme)



main()