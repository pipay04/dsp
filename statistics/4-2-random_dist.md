[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

**Problem:**  
Generate 1000 numbers using random.random(), plot the PMF and CDF and determine whether the distribution is uniform.

**How I Solved It:**  
1. Create a numbers list of 1000 values using random.random().  
2. Construct PMF of numbers list.  
3. Construct CDF of numbers list.  
4. Plot and show both PMF and CDF graphs.

**Solution (Code):**  
    
    import random  
    import thinkstats2  
    import thinkplot

    counter = 0  
    numbers = []

    while counter < 1000:  
	    numbers.append(random.random())  
	  counter += 1

    pmf = thinkstats2.Pmf(numbers)  
    cdf = thinkstats2.Cdf(numbers)

    thinkplot.PrePlot(2)  
    thinkplot.Pmf(pmf)  
    thinkplot.Show(xlabel = 'random numbers', ylabel = 'PMF')  
    thinkplot.Cdf(cdf)  
    thinkplot.Show(xlabel = 'random numbers', ylabel = 'CDF')
    
The resulting shape of PMF is a rectangular distribution while that of CDF is a straight line, both indicating that this is a uniform distribution.
