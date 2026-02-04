Python manages memory automatically through a combination of reference counting and a generational garbage collector.

**Memory Management in Python**
reference in stack
actual object in memory - heap

**Garbage Collection Mechanisms**
1. Reference Counting (Primary Mechanism)
2. Generational Garbage Collection (Cycle Detection)   , it have three generation 0. 1. 2 for checking frequently for 0 , less for 1 , very low for 2

Languages that primarily use reference counting often employ supplementary mechanisms to address cycles [2]. Common solutions include: 
1. Tracing Garbage Collection: This method (like mark-and-sweep) traverses


