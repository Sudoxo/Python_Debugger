import inspect
import sys

#YOUR FUNCTIONS#

#MAKE SURE TO PLACE 'X' AT THE BEGINING OF YOUR FUNCTION NAME IF YOU WANT TO DEBUG IT!#
def Xyour_function(a,b):
    sample_list = []
    sample_list.append(a)
    a += 7
    Xyour_second_function(a)
    sample_list.append(a)
    sample_list.append(b)
    sample_list[0] = b

def Xyour_second_function(x):
    x+=1
    return x

###################

def trace_calls(frame, event, arg):
    fname = frame.f_code.co_name
    if fname[0]=="X":
        #Get list of all variables in your funtion
        variables = frame.f_code.co_varnames
        #Make dict with initial values 
        for v in variables:
            var_info[v] = []
            var_values[v] = []
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
                            #print("Line " + str(line-1) + ": value in '" + v + "' on index number " + str(it) + " changed from " + str(val[v][it]) + " to " + str(state[v][it]))
                            val[v][it] = state[v][it]
                            var_values[v].append([str(state[v]),line-1])
                            
                    #New element
                    else:
                        #print("Line " + str(line-1) + ": " + str(state[v][it]) + " added to list '" + v + "' on index number " + str(it))
                        val[v].append(state[v][it])
                        var_values[v].append([str(state[v]),line-1])

            #SINGLE VARIABLES
            '''elif'''            
            if state[v] != val[v]:
                #print("Line " + str(line-1) + ": '" + v + "' changed from " + str(val[v]) + " to " + str(state[v]))
                #New array case
                if(state[v] == []):
                    val[v] = []
                    var_info[v].append(line-1)
                    var_info[v].append(frame.f_code.co_name)
                    var_info[v].append(type([]))
                    
                else:
                    if(val[v]==None):
                        var_info[v].append(line-1)
                        var_info[v].append(frame.f_code.co_name)
                    val[v] = state[v]
                    var_values[v].append([val[v],line-1])
                    if(len(var_info[v])==2):
                        var_info[v].append(type(val[v]))
            
                    
            
                
var_info = {}
var_values = {}
val = {}
sys.settrace(trace_calls)
Xyour_function(1,10)
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
for v in var_info:
    print("Variable: '" + v +"'")
    print("Type: " + str(var_info[v][2]))
    print("Instantiated in line " + str(var_info[v][0]) + " in function '" + str(var_info[v][1]) + "'")
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("\nCHANGES\n")
for v in var_values:
    print("Variable: '" + v +"'\n")
    for c in var_values[v]:
        print("Value changed to: " + str(c[0]) + " in line " + str(c[1]) + "\n") 
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    
