#Create and return a dictionary for function chaining validation, this dictionary represent a list of functions that can follow the keyed function
def get_all_chains():
    chain_dict = {'1A': ['1B', '1E', '1L', '1N', 'AP', 'BL', 'BN', 'D', 'N'],
                  '1B': ['1A', '1E', '1L', '1N', 'AP', 'BL', 'BN', 'D', 'N'],
                  '1E': ['1A', '1B', '1L', '1N', 'AP', 'BL', 'BN', 'D', 'N'],
                  'AP': ['1A', '1B', '1E', '1L', '1N', 'BL', 'BN', 'D', 'N'],
                  '2': [None],
                  '3': [None],
                  '3S': [], #Fill in
                  'BL': ['1A', '1B', '1E', '1L', '1N', 'AP', 'BN', 'D', 'N'],
                  'BN': ['1A', '1B', '1E', '1L', '1N', 'AP', 'BL', 'D', 'N'],
                  '1N': [], #Fill in
                  'D': [], #Fill in
                  'N': ['1A', '1B', '1E', '1L', '1N', 'AP', 'BL', 'BL', 'D'],
                  '1L': ['1A', '1B', '1E', '1N', 'AP', 'BL', 'BN', 'D', 'N'],
                  'BF': ['D']}
 
    return chain_dict

#Get the valid chains for the current function (fun) 
def get_valid_chains(fun):
    valid_chain = get_all_chains()[fun]
    return valid_chain

#Check if the next function (next_fun) is valid to follow the current function (fun)
def is_chain_valid(fun, next_fun):
    if next_fun in get_valid_chains(fun):
        pass
    else:
        raise ValueError('Geoservice function {} is not a valid function to chain to function {}!'.format(next_fun, fun))