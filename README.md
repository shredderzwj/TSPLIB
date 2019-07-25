# TSPLIB


TSPLIB is a library of sample instances for the TSP (Traveling Salesman Problem 旅行商问题) from various sources and of various types.

Please read the FAQ and the Documentation first.

+ Data files is saved in folder 'res'，\*.tsp file save point coordinates，\*.tour file indicates the optimal solution path.

+ Documentation file is 'tsp95.pdf'.

+ FAQ as follows.

+ [Data Website 1 -> http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/index.html](http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/index.html)

+ [Data Website 2 -> https://wwwproxy.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/](https://wwwproxy.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/)


## TSPLIB FAQ: Questions and Answers
Q: I found a better solution than the one claimed to be optimal in TSPLIB, is this possible?

A: This never occured so far. In all cases when someone believed to have found a better solution, it was not taken into account that it is exactly specified how distances for TSPLIB problems have to computed. Typical errors are

+ evaluation of distances for geometric problem instances as floating-point numbers,
+ false computation of geographic distances,
+ use of display coordinates for distance computations.

Note, however, that due to round-off errors distance evaluations may slightly differ on different machines.

Q: Are the given solution values only the best ones known?.

A: No, for every problem either the value of a provably optimal solution or an interval given by the best known lower and upper bound is listed. The optimality of solutions has been proven by branch-and-cut or branch-and-bound algorithms.

Q: I get wrong distances for problems of type GEO.

A: There has been some confusion of how to compute the distances. I use the following code.

For converting coordinate input to longitude and latitude in radian:

  PI = 3.141592;

  deg = (int) x[i]; 
  min = x[i]- deg; 
  rad = PI * (deg + 5.0 * min/ 3.0) / 180.0; 
  
For computing the geographical distance:

 RRR = 6378.388;

 q1 = cos( longitude[i] - longitude[j] ); 

 q2 = cos( latitude[i] - latitude[j] ); 

 q3 = cos( latitude[i] + latitude[j] ); 

 dij = (int) ( RRR * acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0);

Q: What does the function nint() do?

A: The function "int nint (double x)" converts x into int format rounding to the nearest int value, except halfway cases are rounded to the int value larger in magnitude. This corresponds to the Fortran generic intrinsic function nint. But, rounding like "(int) (x+0.5)" should give the same results for TSPLIB problems. 
Actually, it is better to use just "int" as in the previous answer.

Q: Are contributions still welcome?

A: Basically yes, but, in view of the many problem instances that are already available, new instances should either be real challenge problems or be of general interest.

Q: Is an optimal tour available for every solved problem instance?

A: No. We have included several optimal tours for testing purposes. It is not intended to provide all optimal tours. It should still be a challenge to find one.

Q: Are there optimal solutions available for instances other than symmetric ones?

A: So far, no other optimal solutions have been made available.

Q: Which format has been used to store the data?

A: All data has been compressed with the command "gzip" and has to be read using "gzip -d". Please contact your system administrator if this command is not available.

## Some remarks

Here are some answers to questions or remarks that frequently occur. 
 
+ All files have been compressed under UNIX using "gzip". To uncompress the files "gzip -d" has to be used.

 
+ Problem a280 contains a double node, so there are essentially only 279 nodes. We have not changed the problem name, though.

 
+ Display data must not be used for distance computations. It is only provided for obtaining a graphical display of a problem.

 
+ As written in the documentation, the asymmetric problems ftv90, ftv100, ftv110, ftv120, ftv130, ftv140, ftv150, and ftv160 are all derived from ftv170.

 
+ Yes, one can obtain "shorter" tours if distances are not rounded, but this would define different problem instances.

 
+ I do not keep track of the latest results on the vehicle routing problem instances.

 
+ Optimal solutions are mathematically proven optimal solutions not just heuristic solutions.

 
+ There may exist several shortest tours for a problem instance.

 
+ Distances may differ slightly due to numerical rounding. But if there is a big difference between your tour length and the tour lenghts provided then there is certainly a mistake.

 
+ We can give no further support for obtaining the data.

## References

Applegate, D., Bixby, R., Chvatal, V. and W. Cook (1994), "Finding cuts in the TSP (A preliminary report)", Research Report, Rice University

Jünger, M., G. Reinelt and G. Rinaldi (1996), "The Traveling Salesman Problem", in: M. Ball, T. Magnanti, C. L. Monma and G.L. Nemhauser (eds.), Handbooks in Operations Research and Management Sciences: Networks, North-Holland

Jünger, M., G. Reinelt and G. Rinaldi (1997), "The Traveling Salesman Problem", in: M. Dell' Amico, F. Maffioli, S. Martello (eds.), Annotated Bibliographies in Combinatorial Optimization, 199-221, Wiley

Jünger, M., G. Reinelt and S. Thienel (1994), "Optimal and Provably Good Solutions for the Symmetric Traveling Salesman Problem", Zeitschrift fu"r Operations Research (40), 183-217

Padberg, M.W. and G. Rinaldi (1987), "Optimization of a 532 City Symmetric Traveling Salesman Problem by Branch and Cut", Operations Research Letters (6), 1-7

Padberg, M.W. and G. Rinaldi (1991), "A Branch and Cut Algorithm for the Resolution of Large-scale Symmetric Traveling Salesman Problems" SIAM Review (33), 60-100} 
