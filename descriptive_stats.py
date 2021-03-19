salary_mean = round(salary.mean(),2) #round up to two digits
salary_median = salary.median() 
sd_salary = round(np.std(salary),2) #round up to two digits

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

print("Your # of data is:",len(salary))
print("Mean is:", salary_mean)
print("Median is:", salary_median)
print("Mode is:", sorted(mode(salary.to_list())))
print("Standard Deviation is:", sd_salary)
print("Your range is:", max(salary) - min(salary))
