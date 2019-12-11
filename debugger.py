import inspect
import sys

#YOUR FUNCTION
def your_function(a,b):
    c=3
    a= a + 1
    b = b + 2
    a = a + b
    c=5

def trace_calls(frame, event, arg):
    
    fname = "your_function"
    
    if frame.f_code.co_name == fname:
        
        #Get list of all variables in your funtion
        variables = frame.f_code.co_varnames
        
        #Make dict with initial values 
        for v in variables:
            val[v] = None;
            
        return trace_lines
    
    return 
        

def trace_lines(frame, event, arg):
    
    #Get list of all variables, dict with current values, number of current line
    variables = frame.f_code.co_varnames
    state = frame.f_locals
    line = frame.f_lineno

    #Check for changes
    for v in variables:
        if v in state:
            if state[v] != val[v]:
                print("Line " + str(line-1) + ": '" + v + "' changed from " + str(val[v]) + " to " + str(state[v]))
                val[v] = state[v]
    
val = {}
sys.settrace(trace_calls)
your_function(1,4)
