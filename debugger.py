import inspect
import sys
import timeit
import linecache

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
    return 0
def Xyour_second_function(x):
    if("adad" == "asdd"):
        x+=2
    for i in range(10):
        x+=1
        x+=3
    return x

###################

def trace_calls(frame, event, arg):
    ### MAKE SETUP CODE 2 ###
    global setup_code2
    if(setup_code2 == ""):
        for x in frame.f_globals:
            if x[0] == "X":
                setup_code2 += "from __main__ import " + str(x) + ';'
    #########################
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
    #Get list of all variables, dict with current values, number of current line and code
    filename = str(frame.f_code.co_filename)
    variables = frame.f_code.co_varnames
    state = frame.f_locals
    line = frame.f_lineno
    line_c = linecache.getline(filename, line).strip()

    if(line not in lines_info):
        lines_info[line] = [1]
    else:
        lines_info[line][0] += 1

    ### MAKE SETUP CODE ###
    setup_code = ""
    for x in state:
        setup_code +=str(x)+'='+str(state[x])+';'
    setup_code = setup_code[:-1]
    #######################
    if(line_c.startswith("for ")):
        pass
    elif(line_c.startswith("return(") or line_c.startswith("return ")):
        pass
    elif(line_c.startswith("if(") or line_c.startswith("if ")):
        if(len(lines_info[line]) == 1):
            lines_info[line].append(timeit.timeit(line_c[2:].strip()[:-1], setup = setup_code2 + setup_code))
            lines_info[line].append(timeit.timeit(line_c[2:].strip()[:-1], setup = setup_code2 + setup_code))
        else:
            lines_info[line][1] = ( timeit.timeit(line_c[2:].strip()[:-1], setup = setup_code2 + setup_code) + lines_info[line][2] ) / 2
            lines_info[line][2] += timeit.timeit(line_c[2:].strip()[:-1], setup = setup_code2 + setup_code)
    else:
        if(len(lines_info[line]) == 1):
            lines_info[line].append(timeit.timeit(line_c, setup = setup_code2 + setup_code))
            lines_info[line].append(timeit.timeit(line_c, setup = setup_code2 + setup_code))
        else:
            lines_info[line][1] = ( timeit.timeit(line_c, setup = setup_code2 + setup_code) + lines_info[line][2] ) / 2
            lines_info[line][2] += timeit.timeit(line_c, setup = setup_code2 + setup_code)
        
    print("Line: " + str(line))
    print("Number of execution: " + str(lines_info[line][0]))
    if(len(lines_info[line]) > 1):
       print("Avg time: " + str(lines_info[line][1]) + " Sum: " + str(lines_info[line][2]))
    print("\n")
        
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
lines_info = {}
val = {}
setup_code2 = ""
sys.settrace(trace_calls)
Xyour_function(1,10)
sys.settrace(None)

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
for v in var_info:
    print("Variable: '" + v +"'")
    print("Type: " + str(var_info[v][2]))
    print("Instantiated in line " + str(var_info[v][0]) + " in function '" + str(var_info[v][1]) + "'")
    print("Range:")
    for x in var_values[v]:
        print(x[0], end=" ")
    print("\n")
    print("Starting value: " + str(var_values[v][0][0]) + " Final value: " + str(var_values[v][len(var_values[v])-1][0]))
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    
### PASTE YOUR FUNCTION NAME IN THIS PRINT ###
print("Total program execution time: " + str(timeit.timeit('Xyour_function(1,10)', 'from __main__ import Xyour_function')))
##############################################
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

for line in lines_info:
    print("Number of executions of line " + str(line) + ": " + str(lines_info[line][0]))

