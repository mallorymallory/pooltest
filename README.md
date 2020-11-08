# pooltest
gross misuse of multiprocessing

dont know how to do proper read me 

test of multiprocessing.pool & starmaps for nested data and variable response times

tracking processes and responses:

var A = list which holds pool object (index 0) and associated starmap_async obj for further querying (index 1)
(when response is ready (all processes returned) async obj is changed to response obj
  
var mlist = multiprocessing.Manager.list object containing list(s) whose values are updated in real time by the starmap processes
can be used to review and respond to responses in realtime rather than wait for all processes to end (.get()) which may not be feasible due to variable response times
  
prints nonsense
