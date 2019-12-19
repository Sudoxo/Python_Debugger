import inspect
import sys

#YOUR FUNCTION
def your_function(a,b):
    sample_list = []
    sample_list.append(a)
    a += 7
    sample_list.append(a)
    sample_list.append(b)
    sample_list[0] = b

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
            
            #ARRAYS AND TUPLES
            
            if isinstance(val[v],(list,tuple)):
                for it in range(0,len(state[v])):
                    
                    #If index already exist
                    if(it<len(val[v])):
                        #And It've changed
                        if(val[v][it] != state[v][it]):
                            print("Line " + str(line-1) + ": value in '" + v + "' on index number " + str(it) + " changed from " + str(val[v][it]) + " to " + str(state[v][it]))
                            val[v][it] = state[v][it]
                            
                    #New element
                    else:
                        print("Line " + str(line-1) + ": " + str(state[v][it]) + " added to list '" + v + "' on index number " + str(it))
                        val[v].append(state[v][it])
                        
            #SINGLE VARIABLES
                        
            elif state[v] != val[v]:
                print("Line " + str(line-1) + ": '" + v + "' changed from " + str(val[v]) + " to " + str(state[v]))
                #New array case
                if(state[v] == []):
                    val[v] = []
                else:
                    
                    val[v] = state[v]
            
                    
            
                
    
val = {}
sys.settrace(trace_calls)
your_function(1,10)
