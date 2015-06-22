[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

**Problem:**  
What percentage of the male population have heights between 178cm and 185cm?

**Solution:**  
    import scipy.stats

    mu = 178  
    sigma = 7.7

    dist = scipy.stats.norm(mu, sigma)

    #What percentage of population is more than one standard deviation(7.7) below the mean(178)?  
    #dist.cdf(178-7.7)  
    #0.16 or 16%

    #What percentage of population has height between 178cm and 185cm?  
    #subtract CDF of below 5'10 from CDF of below 6'1 to get percentage between  
    print 100 * (dist.cdf(185) - dist.cdf(177.7))
    
Answer: 0.33 or 33% of the U.S. male population can join Blue Man Group

