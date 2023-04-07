# NPS-calculator

NPS calculator is a tool to calculate Net promoter score of any business/service.

Net Promoter Score helps understand customer satisfaction of any kind of business.
It all starts by asking only one question to the customer which is "On a scale from 0 to 10, how likely are you
to recommend this product/company to a friend or colleague?".

So, all the ratings as answers are accumulated from the customer and NPS is calculated by applying the formula:
  
      NPS = % Promoters - % Demoters

%Promoters: The percentage of customers who has given rating above 8.

%Demoters: The percentage of customers who has given rating below 7.

![net-promoter-score-1](https://user-images.githubusercontent.com/30626886/230363047-98be7236-737e-4a5d-be48-7cb1b3ba2fac.jpg)


To calculate NPS, I have used a simple package from python which is numpy and a well known concept of Numpy arrays which is 'Masking'.

It hardly took 6-7 lines of code to calculate NPS. Below are the steps for calculating the same.

    * Importing numpy library #Please install numpy if it is not installed.
  
    * Loading ratings data from a text file.
  
    * Calculating total number of customers.
  
    * Calculating Promoters and Demoters percentages.
  
    * Finally, putting everything in NPS formula.
  



Some insights which can be drawn from the NPS.

    * If the NPS is below 30, then the business is not doing well and the services/products by the company are very poor.
  
    * If the NPS is 50, then the business is doing good.
  
    * If the NPS is 50+, then the business is doing extremely good and their customer satisfaction is very high.


Here is the link for the streamlit application which was developed to calculate NPS.
https://nps-calculator.onrender.com/
All you need to provide a text file with only ratings as shown in the sample.txt file.

![NPS-2](https://user-images.githubusercontent.com/30626886/230366258-43f33fa0-c6d9-4710-8a1d-077ce04910aa.jpg)
