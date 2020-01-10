HOMEWORK 5: Trendlines & Algorithms


NAME:  Jordan Jackson


PROBLEM DEFINITION:

Q: What information should you know before making funding decisions?
A: A lot more than we knew for this assignment.

It would be helpful to know the historical data of how much each county was allocated, what those allocations were based on, various county measures of before and after receiving a given year's funding. Other measures for health insurance may include: causes of deaths, age distribution of deaths, unexpected expenses, premiums, and routine expenses. Furthermore, it would be important to know what each county plans to do with their funding this year and how much they are requesting.

Q: What information do you have access to?
A: The nys_deaths.csv file given in hw05files.zip and the Introduction and Chapter 1 of “Weapons of Math Destruction”

Q: Who are the relevant stakeholders, and how are they represented in your decision-making process?
A:Relevant stakeholders includes taxpayers, all those affected by the spending of each budget (such as residents of New York State), government employees (such as those who provide the governmental services budgets fund and those who manage government spending).

A: As I do not know much about the stakeholder groups and did not engage with any of them for this assignment (e.g. participatory design process), they are not represented in my decision-making process. I mainly considered the motivations of lawmakers, as I thought this algorithm was the current role of legislators. 


DATA PROVENANCE:

Q: What data did you feel you had available to you?
A: The only accessible and useable data available to me was the nys_deaths.csv file given in hw05files.zip. 

Q: Where did it come from? 
A: I don't know. It was distributed by New York State Department of Health, via https://health.data.ny.gov

Q: How was it collected? 
A: I don't know.

Q: What external research did you do to help you make your decisions?

A:I did not do external research. Reading the Introduction and Chapter 1 of “Weapons of Math Destruction” definitely influenced the decisions I made. For example, O'Neil reminded me the importance of the weighting of variables in models and algorithms. As a result, I wrote my allocating_budget() to only act on a certain proportion of the available budget. This means that depending my interpretation of the relationship (direct vs. inverse and/or strong vs. weak) between death rates on a budget category, some budgets took the ratios generated in get_ratio() more into account than others.

Additionally, O'Neil made me write my code and make more conservative decisions. I leaned much more to equal allocation of budgets among counties in the face of uncertainty given the limited variables in the provided dataset and perhaps because I felt less accountable for the results (as equal distribution seemed like a default). 

I incorporated weighting into my design by including controlling how much of the total money was going to be distributed based on my algorithm and how much was going to be evenly distributed. 


ACCOUNTABILITY:
Q: Who are you accountable to? 
A: The stakeholders (see previous).

Q: How will you know that your design has properly worked? 
A: Assuming I only look at death rates, I may know if my design has properly worked if the death rates for each county correlate with an increase or decrease in funding from the previous year. Furthermore, I checked that the code allocated the total amount of budget money available. 

Q: What safeguards have you built into your design? 
A: I only considered death rates from the latest 3 years so old information (and their associated trends and events) will not affect the current budget allocation.


MISC. COMMENTS TO GRADER:  

Rather than "In three separate functions, you should write code for each of these budgets that divides up the amount provided amongst the NY state counties", I have a function we can parametrize in 3 different ways (by putting in different variables as parameters).

ABOUT BY ALGORITHM:

1. Health Insurance
I correlated counties with higher death rates would need more money because one could assume higher death rates are due to health-insurance-related issues.

Out of the three budget categories, I made the death rates have the greatest impact on the health insurance budget category because health insurance had the most direct perceived correlation/relationship with death rates.


2. School Aid/Special Education
Although I wanted to make the education budget inversely proportional to the death rates, I was having trouble figuring this out mathematically, so I ended up reversing the order of the insurance ratios list, then assigning the those values to the alphabetized list of county names. As a result, the counties with lower rates would receive the most educational funding, but not necessarily exactly proportional to the death rates of that county.

The least death rate may mean there are the least amount of elderly people and more youth who need school aid. Thus, a lower death rate would be correlated with a higher budget allocation. 

I made the death rates have the least impact of the school budget because my assumptions and conclusions felt the most loosely correlated.

3. Social Services
Given I assumed death rates mostly reflected deaths of elderly people and social services benefit people of all ages, I gave this budget category the greatest base_allocation value. Consequently, more of the budget money was evenly distributed among counties than in the other budget categories. 


