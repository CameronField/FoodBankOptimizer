# FoodBankOptimizer
Optimizing Mississippi's Food Bank Network using Gurobipy

This repo is my contribution to my team's final project submission for 15.774 The Analytics of Operations Management. All content is my own.

## 1) Problem Background and Motivation
Food insecurity is a significant challenge in the United States, affecting millions, with Mississippi experiencing a severe crisis. Nearly one in six residents, including a substantial number of children and seniors, face food insecurity, defined as the uncertainty or inability to acquire sufficient food due to financial constraints.

The implications of food insecurity extend far beyond hunger. It correlates with increased risks of mental health issues, chronic health conditions, and significant economic burdens. These challenges are compounded in Mississippi due to logistical hurdles and limited resources, making efficient food distribution a daunting task.

The Mississippi Food Bank Network plays a crucial role in addressing this challenge. However, the state's rural nature, complex geography, and operational constraints of the existing food bank network exacerbate the difficulty in reaching those in need. The motivation behind our project is to optimize the food bank network in Mississippi, using data analysis and optimization techniques, to improve the reach and effectiveness of food assistance in the state. By doing so, we aim to ensure that the most vulnerable populations receive the necessary aid, ultimately striving to combat food insecurity in a more efficient and impactful manner.

## 2) Problem Statement
The primary challenge addressed in this project is the optimization of the Mississippi Food Bank Network's distribution system. Despite the vital role the network plays in mitigating food insecurity, several inefficiencies hinder its effectiveness. These include suboptimal routing, uneven distribution of resources, and logistical constraints that lead to delays and increased costs. These issues not only limit the network's capacity to serve the needy but also strain its limited resources. The goal of this project is to identify and implement optimization strategies that can streamline the distribution process, enhance the reach of the food bank network, and ensure that resources are utilized in the most effective manner. By tackling these logistical and operational inefficiencies, the project aims to significantly improve the delivery of food assistance to those most in need across Mississippi.

## 3) Optimization Methodology and Formulation
Current System Overview
In the existing Mississippi Food Bank Network, regional food banks serve as the primary distribution centers, delivering food to various local food pantries. These pantries then act as the final distribution points where food-insecure individuals come to collect meals. This system, while functional, faces challenges in terms of efficiency and reach, primarily due to Mississippi's rural nature and complex geography.

### Optimization Approach
Our optimization model aimed to enhance this network by strategically reallocating resources to maximize the number of food-insecure individuals sustainably fed. We employed a facility location problem framework, integrating data-driven insights from our operational research and food insecurity projections.

### Model Formulation
Geographic and Demographic Data: Utilized precise coordinates of food banks, food pantries, and city centers for calculating distances. Combined with detailed county-level food insecurity data and city population statistics, this allowed for a nuanced distribution of resources.

Operational Capacities and Risk Levels: Categorized pantries based on their capabilities, setting feeding targets per risk category in counties. This stratified approach prioritized assistance to the most affected areas, optimizing resource allocation.

#### Financial Considerations: 
Included budget constraints and meal costs in the model, ensuring financial feasibility.

#### Data-Driven Allocation: 
Adopted a weighted allocation based on city populations within each county, ensuring proportionate distribution.

#### Model Constraints: 
Incorporated realistic constraints like distance limits for individuals to travel for food, pantry capacity limits, and budget constraints.

#### Objective Function: 
Aimed to maximize the total number of food-insecure persons sustainably fed, aligning with strategic objectives.

The model's comprehensive nature, rooted in real-world operational constraints and geographic considerations, not only proposed a more efficient distribution system but also offered insights for policymakers in resource allocation and strategic planning. Here is the full model formulation:

<img width="1357" alt="Screen Shot 2024-01-15 at 5 04 32 PM" src="https://github.com/CameronField/FoodBankOptimizer/assets/78181039/d389cdc7-8733-4304-bbd4-c76a87492a18">

## 4) Results
The results of the optimization model reveal a nuanced picture of the Mississippi Food Bank Network's potential for improved operations. Central to our analysis were four key visualizations, each underscoring critical insights derived from the optimization model.

The network design's robustness is affirmed through the supply and demand node connections plot:

<img width="395" alt="Screen Shot 2024-01-15 at 5 10 57 PM" src="https://github.com/CameronField/FoodBankOptimizer/assets/78181039/6e3a3e3a-1e4c-47dc-a061-243533e5aad4">

Remarkably, the optimized connections largely mirror the actual configurations of the Mississippi Food Bank Network, reinforcing our model's validity and its applicability in real-world scenarios.

However, our county-level analysis indicates a persistent challenge: even under optimal conditions, the food bank network can support only about 65% of Mississippi's food-insecure population.

<img width="394" alt="Screen Shot 2024-01-15 at 5 11 06 PM" src="https://github.com/CameronField/FoodBankOptimizer/assets/78181039/8e3cf5db-274b-4f61-974c-d3dd628115e3">

This sobering statistic is further complicated by the fact that the most at-risk counties also incur the highest per-meal costs. The model pragmatically prefers reaching counties with a lower cost per meal, thereby aiding more individuals, albeit not always those in the highest need.

The relationship between the food bank network's budget and the number of food-insecure individuals served is depicted in a non-linear and diminishing returns curve. 

<img width="595" alt="Screen Shot 2024-01-15 at 5 11 16 PM" src="https://github.com/CameronField/FoodBankOptimizer/assets/78181039/1c56f74f-1cd5-4426-87c9-bcecf72696d9">

This curve underscores the importance of a minimum viable budget, pinpointing $850,000 every two weeks as the threshold for a feasible solution. It emphasizes the critical need for strategic financial planning to ensure the network's operations are both sustainable and impactful.

Lastly, the cost sensitivity analysis highlights a pivotal factor: the number of food-insecure individuals fed is highly sensitive to meal costs. 

<img width="525" alt="Screen Shot 2024-01-15 at 5 11 25 PM" src="https://github.com/CameronField/FoodBankOptimizer/assets/78181039/1b5b31fb-a322-4250-a554-fa6a0ab6b0e8">

A small increase in meal costs significantly reduces the number of people the network can serve. In contrast, transportation costs display a less pronounced effect, suggesting that efforts to reduce meal costs should be prioritized over transportation efficiencies for a more substantial impact on the network's reach.

These insights combine to form a compelling narrative of the Mississippi Food Bank Network's current state and the profound potential benefits of adopting an optimized approach to its operations.

## 5) Summary
The optimization project undertaken for the Mississippi Food Bank Network culminates in several pivotal findings that not only reflect the current operational status but also chart a course for future enhancements. The crux of the study illustrates that financial resources emerge as the most significant constraint affecting the network's capacity to address food insecurity across Mississippi effectively.

As we look toward 2025, the financial forecast necessitates a minimum of $850,000 bi-weekly to maintain a distribution network that is both sustainable and equitable. This budgetary baseline ensures that the network can operate at a level that meets a substantial portion of the needs without compromising on the reach or quality of service.

Furthermore, our analysis delineates a clear incremental benefit associated with budget increases. For each additional $250,000 allocated bi-weekly, the network gains the capacity to feed 50,000 more food-insecure individuals. This linear relationship between budget increments and the number of individuals fed highlights the potential for significant improvements in food security with targeted financial investments.

Policy makers must recognize the imperative role that budget plays in the operational effectiveness of the food bank network. It is essential that upcoming budgets reflect these findings, prioritizing the increase of financial allocations to the Mississippi Food Bank Network. In doing so, policy makers will directly contribute to combating food insecurity in the state, making a tangible difference in the lives of those who rely on the network for support.

In conclusion, this project has shed light on the operational complexities of food distribution networks and has underscored the critical need for thoughtful, data-driven decision-making in policy and budget planning to ensure that no Mississippian goes hungry.
