# ManojMorais_Statistics Module

## Introduction

This Python module simplifies the process of performing a two-sample t-test and gets  all relevant tables/output such as group-wise mean, count, standard deviation, 
total number of obserations along with the t-test results and decision making (accept/reject null hypothesis ) at 5% level,  
which is helpful for those who are unfamiliar with advanced statistical concepts.

## Installation
You can install this module using pip:
pip install ManojMorais_Statistics



# Example: Perform a two-sample t-test




Suppose, you want to see whether there exists significant differences in mean marks of male and female students
2 columns: Gender ( Male: coded as 0,and Female: coded as 1) and Marks

load excel file in python using pandas 

from ManojMorais_Statistics import Ttest_2sample

Ttest_2Sample enables you to give two variables namely group 1 which is your categorical variable and group 2 is your continous variable.
Ttest_2Sample(data['Gender'], data['Marks'])

Guess what! Thats it!


## Dependencies 

This module relies on standard Python libraries scipy.stats, pandas, and numpy

## License 

This project is licensed under the MIT License - see the LICENSE file for details 

