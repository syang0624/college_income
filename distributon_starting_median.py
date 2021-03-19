plt.hist(salary, alpha=1, linewidth=5)
plt.title("Distribution of Starting Median Salary", fontsize = 15)
plt.xlabel("Starting Median Salary", fontsize = 10)
plt.ylabel("Frequency of data", fontsize = 10)
plt.gcf().set_figwidth(10)

plt.xticks([30000,35000,40000,45000,50000,55000,60000,65000,70000]) #increase xticks by 10000
plt.axvline(salary_mean, color='g', label = "Mean = 46947.06") #label legend for mean
plt.axvline(salary_median, color='r', label = "Median = 45600.00")#label legend for median
plt.legend()
ax=plt.gca()
ax.set_facecolor('w')
plt.show()
