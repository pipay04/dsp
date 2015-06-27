[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

**Problem:**  
Compute the mean, median, skewness and Pearson's skewness of the sample. What fraction of households report a taxable income below the mean? How do the results depend on the assumed upper bound?

**Solution:**

    import numpy as np
    import hinc
    import math
    import thinkstats2
    import thinkplot
    
    def InterpolateSample(df, log_upper=6.0):  
        """Makes a sample of log10 household income.
        Assumes that log10 income is uniform in each range.
        df: DataFrame with columns income and freq
        log_upper: log10 of the assumed upper bound for the highest range
        returns: NumPy array of log10 household income
        """
        # compute the log10 of the upper bound for each range
        df['log_upper'] = np.log10(df.income)
    
        # get the lower bounds by shifting the upper bound and filling in
        # the first element
        df['log_lower'] = df.log_upper.shift(1)
        df.log_lower[0] = 3.0
    
        # plug in a value for the unknown upper bound of the highest range
        df.log_upper[41] = log_upper
    
        # use the freq column to generate the right number of values in
        # each range
        arrays = []
        for _, row in df.iterrows():
            vals = np.linspace(row.log_lower, row.log_upper, row.freq)
            arrays.append(vals)
    
        # collect the arrays into a single sample
        log_sample = np.concatenate(arrays)
        return log_sample

    def EvalCdf(sample, x): #to get percentage below mean
        count = 0.0
        for value in sample:
            if value <= x:
                count += 1
        prob = count / len(sample)
        return prob
    
    df = hinc.ReadData() #read data
    sample = InterpolateSample(df) #sample values with upper bound at log10 to the 6
    conv_sample = np.power(10, sample) #convert sample values to actual dollar values
    
    log_cdf = thinkstats2.Cdf(sample) #cdf values of sample
    thinkplot.Cdf(log_cdf) #create cdf plot
    thinkplot.Show(xlabel='household income', ylabel='CDF') #show cdf plot
    
    mean = thinkstats2.RawMoment(conv_sample, k=1) #get mean of converted sample
    median = thinkstats2.Median(conv_sample) #get median of converted sample
    percentage = EvalCdf(conv_sample, mean) #get percentage of converted sample values lesser or equal to the mean
    skewness = thinkstats2.Skewness(conv_sample) #get skewness
    pearson = thinkstats2.PearsonMedianSkewness(conv_sample) #get pearson's skewness
    print "Upper bound log10 6.0 \nmean: %f \nmedian: %f \nskewness: %f \nPearson's skewness: %f \nFraction of income below the mean: %f" % (mean, median, skewness, pearson, percentage)
    
    pdf = thinkstats2.EstimatedPdf(conv_sample)
    thinkplot.Pdf(pdf, label='sample')
    thinkplot.Show(xlabel='household income', ylabel='PDF')
    
    #log10 7.0
    sample_7 = InterpolateSample(df, 7.0) #sample values with upper bound at log10 to the 7
    conv_sample_7 = np.power(10, sample_7) #convert sample values to actual dollar values
    
    log_cdf_7 = thinkstats2.Cdf(sample_7) #cdf values of sample
    thinkplot.Cdf(log_cdf_7) #create cdf plot
    thinkplot.Show(xlabel='household income', ylabel='CDF') #show cdf plot
    
    mean_7 = thinkstats2.RawMoment(conv_sample_7, k=1) #get mean of converted sample
    median_7 = thinkstats2.Median(conv_sample_7) #get median of converted sample
    percentage_7 = EvalCdf(conv_sample_7, mean_7) #get percentage of converted sample values lesser or equal to the mean
    skewness_7 = thinkstats2.Skewness(conv_sample_7) #get skewness
    pearson_7 = thinkstats2.PearsonMedianSkewness(conv_sample_7) #get pearson's skewness
    print "Upper bound log10 7.0 \nmean: %f \nmedian: %f \nskewness: %f \nPearson's skewness: %f \nFraction of income below the mean: %f" % (mean_7, median_7, skewness_7, pearson_7, percentage_7)
    
    pdf = thinkstats2.EstimatedPdf(conv_sample_7)
    thinkplot.Pdf(pdf, label='sample')
    thinkplot.Show(xlabel='household income', ylabel='PDF')
