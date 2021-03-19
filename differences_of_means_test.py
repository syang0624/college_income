def dif_of_means_test(data1,data2,tails):
    n1 = len(data1) #length of the data is equal to the sample size
    n2 = len(data2)

    x1 = np.mean(data1) #use numpy to get mean here
    x2 = np.mean(data2)

    s1 = np.std(data1,ddof=1) # Having Bessel's correction here
    s2 = np.std(data2,ddof=1) # Therefore I use (n-1) as my denominator

    SE = np.sqrt(s1**2/n1 + s2**2/n2)
    Tscore = np.abs((x2 - x1))/SE
    df = min(n1,n2) - 1 # Using conservative estimation as Open Intro said.
    pvalue = tails*stats.t.cdf(-Tscore,df)

    SDupdated = np.sqrt((s1**2*(n1-1) + s2**2*(n2-1))/(n1+n2-2)) # OpenIntro section 5.3.6
    Cohensd = (x2 - x1)/SDupdated
    HedgesG = Cohensd*(1-(3/((4*df)-1)))

    print('t =', Tscore)
    print('p =', pvalue)
    print('d =', np.abs(Cohensd)) #get an absolute value
    print('g =', np.abs(HedgesG))
    
    
dif_of_means_test(salaryN,salaryS,2) #have two tails
