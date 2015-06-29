# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

**Problem:**   


**Solution:**

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
  
2. 

---
