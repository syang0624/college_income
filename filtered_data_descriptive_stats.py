dataN = pd.read_csv("college data set - Northeastern.csv", sep=',')
salaryN = dataN["Starting Median Salary"]

salaryN_mean = round(salaryN.mean(),2) #round up to two digits
salaryN_median = salaryN.median() 
sd_salaryN = round(np.std(salaryN),2) #round up to two digits

def mode(lst): #since I have multiple modes, I created another function for mode
    L1=[] #count the occurrence of each number and append or add findings to the list
  
    i = 0 #count the numbers and put them into L1
    while i < len(lst) : 
        L1.append(lst.count(lst[i])) 
        i += 1

    # the occurrences for each number in sorted lst 
    # create a custom dictionary d1 for k : V 
    # k = value, v = occurence

    d1 = dict(zip(lst, L1))  
    d2=[k for (k,v) in d1.items() if v == max(L1)] # the k values with the highest v values. 
    return d2

print("Your # of data is:",len(salaryN))
print("Mean is:", salaryN_mean)
print("Median is:", salaryN_median)
print("Mode is:", sorted(mode(salaryN.to_list())))
print("Standard Deviation is:", sd_salaryN)
print("Your range is:", max(salaryN) - min(salaryN))

dataS = pd.read_csv("college data set - Southern.csv", sep=',')
salaryS = dataS["Starting Median Salary"]

salaryS_mean = round(salaryS.mean(),2) #round up to two digits
salaryS_median = salaryS.median() 
sd_salaryS = round(np.std(salaryS),2) #round up to two digits

def mode(lst): #since I have multiple modes, I created another function for mode
    L1=[] #count the occurrence of each number and append or add findings to the list
  
    i = 0 #count the numbers and put them into L1
    while i < len(lst) : 
        L1.append(lst.count(lst[i])) 
        i += 1

    # the occurrences for each number in sorted lst 
    # create a custom dictionary d1 for k : V 
    # k = value, v = occurence

    d1 = dict(zip(lst, L1))  
    d2=[k for (k,v) in d1.items() if v == max(L1)] # the k values with the highest v values. 
    return d2

print("Your # of data is:",len(salaryS))
print("Mean is:", salaryS_mean)
print("Median is:", salaryS_median)
print("Mode is:", sorted(mode(salaryS.to_list())))
print("Standard Deviation is:", sd_salaryS)
print("Your range is:", max(salaryS) - min(salaryS))
