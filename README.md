# 射撃王 Visualizer 

- A simple html visualizer for [射撃王](https://atcoder.jp/contests/abc023/tasks/abc023_d)
- Folder structure explained as follows
```
.
├── README.me       
├── algorithms.py   # Algorithm for solving 射撃王
├── barebone.py     # A scratch version for the final algorithm
├── main.py         # The entry point. Run this script to         
├                     generate a step-wise solution to the
├                     problem specified in <problem.py>.         
├                     The generated solution is stored in <trace.jsonp>
├── problem.py               # Write your problem parameter here
├── shageki_visualizer.html  # The visualizer interface
├── shagekiou.py             # The problem representation
├── trace.jsonp              # Program generated data, representing each critical state
├                              in solving the problem as specified in <problem.py>
├── trace.py                 # The tracer program which keeps track of each 
├                              critical step in 射撃王 problem
├── trace.template            
├── utils.py
```