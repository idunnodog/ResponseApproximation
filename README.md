# ResponseApproximation
This is an approximation python app to predict what response might system have to take into account for load testing. 

it uses historical stat to group by seconds/minutes calculating 90 percentile for main measurement (response time). 
Then it find right coefficients for approximation functions and give you it and graphs:
![alt text](https://i.ibb.co/z6v6G7N/2020-05-02-03-57-22.jpg)

You can choose different functions:
![alt text](https://i.ibb.co/bgcQrrV/2020-05-02-04-01-41.jpg)
