# Optimization-Methods-in-Management-Science


**In the context of the exercise, we will solve a vehicle routing problem aimed at minimizing the total energy required for the transportation of products, which in turn minimizes transportation costs. The operational scenario is as follows:**

1. We need to transport products from a central warehouse to a total of 250 customers \(N = \{1, 2, \ldots, 250\}\), who are located in various places.
2. Each customer \(i \in N\) has ordered a quantity of products \(d_i\).
3. A homogeneous fleet of vehicles will be hired for the transport of the supplies.
   a. Each vehicle has a tare weight of \(W = 6 \, \text{tn}\).
   b. Each vehicle has a maximum load capacity of \(Q = 8 \, \text{tn}\).
4. Each truck starts its route from the central warehouse \(d = \{0\}\) and successively visits a set of customers.
5. Each customer \(i \in N\) is satisfied by a single visit from an exclusive vehicle. Therefore, when a vehicle visits a service point, it delivers the required quantity of products \(d_i\).
6. The routes are completed at the last customer served (external fleet - open routes).
7. The cost of the total transportation activity will be calculated based on the total ton-kilometers (tn x km) of the routes. Therefore, the design of the routes should minimize the total gross (truck tare and load weight) ton-kilometers traveled.

In other words, if we have a solution \(S:(0,2,3,4,1)\) for a problem with 4 customers, the total ton-kilometers traveled is:
\[ z(S) = (T + d_1 + d_2 + d_3 + d_4) \cdot c_{12} + (T + d_2 + d_3 + d_4) \cdot c_{23} + (T + d_3 + d_4) \cdot c_{34} + (T + d_4) \cdot c_{45} \]

**Comments**:  
The problem along with its characteristics can be found in the file **Instance.txt**.  
Assume that the distance between two nodes in the network is equal to the Euclidean distance of the nodes.

**Instructions**:  
You must submit a folder with your project compressed as a zip file.  
Your code must run within five minutes on a relatively modern PC.  
Your code should produce a txt file with your final solution, which must follow the format of the file **example_solution.txt**. This file should already be in the folder with your Python project.  
You can use the **sol_checker** to verify if your solution meets the problem specifications.  
If your code uses random generators (for solving and NOT for creating the network), they must be initialized with one of the following seeds: 1, 2, 3, 4, 5.

---

