# tada-type-graph
[![Build Status](https://semaphoreci.com/api/v1/ahmad88me/tada-type-graph/branches/master/badge.svg)](https://semaphoreci.com/ahmad88me/tada-type-graph)
[![codecov](https://codecov.io/gh/oeg-upm/tada-type-graph/branch/master/graph/badge.svg)](https://codecov.io/gh/oeg-upm/tada-type-graph)


This piece of code is to be used to build type graphs. This is not meant to be used alone. 

It include pieces of code to compute the *specificity* and *coverage* but extra code to coverage
in the first place need to exist in the application using this library.
  
# Remarks
`add_v(title, parents)` : if `parents` is `None`, it means that it does not know
the parents of this node (with the given `title`) yet. It also means that the roots
of the graph will not be updated.
