from checkers import *

def geoservice(funs, **fun_args):
    
    if isinstance(funs, list):
        first_fun = funs[0]
        check_fun(first_fun)
        
    elif isinstance(funs, str):
        first_fun = funs
        check_fun(first_fun)
    
    else:
        raise TypeError('Funs must be a list of strings or a string')
    
    #Check the arguments of the function, unpack the keyword arguments
    url = construct_args_url(fun = funs, **fun_args)