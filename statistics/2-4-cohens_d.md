[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

**Problem:**  
Investigate whether first babies are lighter or heavier than others using Cohen's *d* and how it compares to pregnancy length. Use variable *totalwgt_lb*.

**How I Solved It:**  
1. Read data from NSFG pregnancy file and store in variable *preg*.  
2. Select records of live birth only.  
3. Group records into:  
    * first babies  
    * other babies  
4. Get *totalwgt_lb* for both groups.  
5. Apply Cohen's *d* function to both groups.  

**Solution(Code):**  
import nsfg  
import thinkstats2

preg = nsfg.ReadFemPreg()  
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]  
others = live[live.birthord != 1]

firsts_group = firsts.totalwgt_lb  
others_group = others.totalwgt_lb

print 'Mean: ', firsts_group.mean() - others_group.mean()  
print 'Var', firsts_group.var() - others_group.var()  
print 'Std', firsts_group.std() - others_group.std()  
print 'Cohen\'s d', thinkstats2.CohenEffectSize(firsts_group, others_group)  

The code returned the following differences in values:
* Mean: -0.12 indicating first babies are generally lighter but not significantly
* Var: 0.07 (not sure how to interpret)
* Std: 0.03 deviation in lbs
* Cohen's d: difference in means is -0.09 standard deviations
