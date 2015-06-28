[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

**Problem:**  
Simulate experiment 1000 times with sample size n = 10 from an exponential distribution with lambda = 2. Plot the sampling distribution of the estimate L. Compute standard error of the estimate and the 90% confidence interval.  
Repeat the experiment with different values of n and make a plot of standard error versus n.

**Solution:**

    import numpy as np  
    import math  
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

    def Estimate(n=10, m=1000):
      """
      n: sample size
      m: number of iterations
      """
      lam = 2 

      means = []

      for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        means.append(L)

      cdf = thinkstats2.Cdf(means)
      ci_lower = cdf.Percentile(5)
      ci_upper = cdf.Percentile(95)
      stderr = RMSE(means, lam)

      thinkplot.Cdf(cdf)
      thinkplot.Show(xlabel='sample mean',
                   ylabel='CDF',
                   title='Sampling distribution')

      print "90%% confidence interval (CI) is (%.2f, %.2f) \nstandard error (SE) is %.2f" % (ci_lower, ci_upper, stderr)

    def Estimate2(n=10, m=1000):
      lam = 2
      means = []

      for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        means.append(L)

      stderr = RMSE(means, lam)
      return "%.2f" % (stderr, )

    def main():  
      Estimate()

      stderr = []
      sample_size = []

      for i in range(5, 50, 5):
        sample_size.append(i)
        stderr.append(Estimate2(i, m=1000))

      thinkplot.Scatter(stderr, sample_size)
      thinkplot.Show(xlabel='standard error (SE)', ylabel='sample size (n)')

    if __name__ == '__main__':
      main()
      
  1. Estimate(10, 1000) yields the following results:  
      90% CI: (1.30, 3.72)  
      SE: 0.85
  2. When experimenting with different values of n, based on the plot of standard error versus n, as n increases the standard error decreases.
