[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

**Problem:**  
Compare the actual distribution and the biased distribution for how many children are in a family.

**How I Solved It:**  
1. Retrieve variable *numkdhh*.  
2. Construct PMF based on *numkdhh*.  
3. Compute mean of actual PMF.  
4. Define BiasPmf() for computation of the biased pmf distribution.  
5. Construct Biased PMF based on pmf generated from BiasPmf().  
6. Plot both distributions using thinkplot module.  
7. Compute mean of Biased PMF.  
8. Print both means.

**Solution(Code):**

    import chap01soln  
    import thinkstats2  
    import thinkplot  

    resp = chap01soln.ReadFemResp()  
    numkdhh = resp.numkdhh

    pmf = thinkstats2.Pmf(numkdhh, label = "actual")  
    pmf_mean = pmf.Mean() 

    def BiasPmf(pmf, label):
      new_pmf = pmf.Copy(label = label)
  	  
  	  for x, y in new_pmf.Items():
  		  new_pmf.Mult(x, x)
  
  	  new_pmf.Normalize()
  	  return new_pmf

    biased_pmf = BiasPmf(pmf, label = "biased")  
    biased_mean = biased_pmf.Mean()

    thinkplot.PrePlot(2)  
    thinkplot.Pmfs([pmf, biased_pmf])  
    thinkplot.Show(xlabel = 'family size', ylabel = 'PMF')  

    print "PMF Mean: %s" % (pmf_mean)  
    print "Biased PMF Mean: %s" % (biased_mean)
    
  
