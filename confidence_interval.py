#confidence interval 1

stats.t.interval(alpha=0.95, df=len(salary)-1, loc=np.mean(salary), scale=stats.sem(salary))

#confidence interval northeastern

stats.t.interval(alpha=0.95, df=len(salaryN)-1, loc=np.mean(salaryN), scale=stats.sem(salaryN))


#confidence interval southern

stats.t.interval(alpha=0.95, df=len(salaryS)-1, loc=np.mean(salaryS), scale=stats.sem(salaryS))
