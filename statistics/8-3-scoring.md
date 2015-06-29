# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

**Problem:**   
  Write a function that takes a goal scoring rate (lam) in goals per game and simulates a game by generating the time between goals until the total time exceeds 1 gme, then returns the number of goals scored.  
  
  Write another function that simulates may games, stores the estimates of lam, then computes their mean error and RMSE.
  
  Is estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. What is the standard error? What happens to sampling error for increasing values of lam?

**Solution:**

    import numpy as np
    import math
    import random
    import thinkstats2
    import thinkplot

    def RMSE(estimates, actual):
        """Computes the root mean squared error of a sequence of estimates.

        estimate: sequence of numbers
        actual: actual value

        returns: float RMSE
        """
        e2 = [(estimate-actual)**2 for estimate in estimates]  
        mse = np.mean(e2)
        return math.sqrt(mse)
    
    def MeanError(estimates, actual):
        """Computes the mean error of a sequence of estimates.

        estimate: sequence of numbers
        actual: actual value

        returns: float mean error
        """
        errors = [estimate-actual for estimate in estimates]
        return np.mean(errors)

    def Simulate(lam):
        game = 1
        goal = 0
        time = 0
        
        while time <= game:
            time += random.expovariate(lam)
            goal += 1
            
        goal -= 1
        return goal
        
    def Estimate(lam, m):
        estimate = []
        
        for i in range(1, m+1):
            estimate.append(Simulate(lam))
            
        print ('RMSE: ', RMSE(estimate, lam))
        print ('Mean Error: ', MeanError(estimate, lam))
        
        cdf = thinkstats2.Cdf(estimate)
        ci_lower = cdf.Percentile(5)
        ci_upper = cdf.Percentile(95)
        stderr = np.std(estimate)
    
        thinkplot.Cdf(cdf)
        thinkplot.Show(xlabel='estimates',
                       ylabel='CDF',
                       title='Sampling distribution')
    
        print "90%% confidence interval (CI) is (%.2f, %.2f) \nstandard error (SE) is %.2f" % (ci_lower, ci_upper, stderr)
        
    def main():
        Simulate(2)
        
        Estimate(2, 100)
        Estimate(2, 1000)
        Estimate(2, 10000)
        Estimate(2, 100000)
        Estimate(2, 1000000)
        
        for i in range(2, 8):
            Estimate(i, 100000)
            
    if __name__ == '__main__':
        main()

1. Is estimate biased?  
  Given the simulations below with m increasing for every simulation,
  - prework_ch8_2.Estimate(2, 1000)  
      ('RMSE: ', 1.420915198032592)  
      ('Mean Error: ', -0.060999999999999999)  
  - prework_ch8_2.Estimate(2, 10000)  
      ('RMSE: ', 1.4060938802227965)  
      ('Mean Error: ', -0.0229)
  - prework_ch8_2.Estimate(2, 100000)  
      ('RMSE: ', 1.4148604171436843)  
      ('Mean Error: ', 0.0046699999999999997)
  - prework_ch8_2.Estimate(2, 1000000)  
      ('RMSE: ', 1.4137987834200452)  
      ('Mean Error: ', 0.00022499999999999999)
  - prework_ch8_2.Estimate(2, 10000000)  
      ('RMSE: ', 1.4144689109344186)  
      ('Mean Error: ', -0.00014469999999999999)

  It appears the estimate is unbiased because the estimator converges to 0 as m increases.
  
2. As value of lam increases, value of sampling error also increases

---
