# pooltest
gross misuse of multiprocessing

dont know how to do proper read me 

test of multiprocessing.pool & starmaps for nested data and variable response times

tracking processes and responses:
  var A = list which holds pool object (index 1) and associated starmap_async obj for further querying
          (when response is ready (all processes returned) async obj is changed to response obj
  mlist = multiprocessing.Manager.list object containing list whose values are updated in real time by the starmap processes 
  
prints nonsense
