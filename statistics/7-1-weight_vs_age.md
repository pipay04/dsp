[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

**Problem:**  
Make a scatter plot of birth weight versus mother's age. Plot percentiles of birth weight versus mother's age. Compute Pearson's and Spearman's correlations. How would you characterize the relationship between these variables?

**Solution:**
    import nsfg
    import thinkplot
    import numpy as np
    import thinkstats2

    preg = nsfg.ReadFemPreg() #read data from nsfg
    live = preg[preg.outcome == 1] #live births only
    live = live.dropna(subset=['totalwgt_lb', 'agepreg']) #drop all nan values

    thinkplot.Scatter(live['totalwgt_lb'], live['agepreg']) #scatter plot of birth weight and mother's age
    #thinkplot.Show(xlabel='weight (lbs)', ylabel='mother\'s age')

    bins = np.arange(-2, 20, 2) #NumPy array of bins from -2 to 20 (exclusive of 20) in increments of 2
    indices = np.digitize(live.totalwgt_lb, bins) #index of the bins
    groups = live.groupby(indices) #group by the indices/bins

    weights = [group.totalwgt_lb.mean() for i, group in groups] #array of birth weight means
    cdfs = [thinkstats2.Cdf(group.agepreg) for i, group in groups] #array of cdf for mother's age

    for percent in [75, 50, 25]:
	    ages = [cdf.Percentile(percent) for cdf in cdfs]
	    label = '%dth' % (percent,)
	    thinkplot.Plot(weights, ages, label=label)

    #thinkplot.Show(xlabel='weight (lbs)', ylabel='mother\'s age', label=label)

    pearson = thinkstats2.Corr(live['totalwgt_lb'], live['agepreg'])
    spearman = thinkstats2.SpearmanCorr(live['totalwgt_lb'], live['agepreg'])

    print "Pearson\'s Correlation: %f vs. Spearman\'s Correlation: %f" % (pearson, spearman)
