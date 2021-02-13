from urllib.parse import quote
import urllib3
import bs4 as BeautifulSoup
import requests
import pandas as pd
import geo_urls

#Define the function for scraping the geoservice function information/documentation
#This is probably best to be moved to a static file that is updated with each new release (if applicable)
def get_fun_info():
    url = geo_urls.base_url
    url = quote(url, safe = ':/?&=')
    
    try:
        doc = requests.get(url).text
    except:       
        print('exception!')
        
    content = BeautifulSoup.BeautifulSoup(doc, 'html.parser')
    table = content.find_all('table')
    df_list = [pd.read_html(str(t))[0] for t in table]
    dict_list = [d.to_dict(orient = 'records') for d in df_list]
    return dict_list

#Get the human readable description of the geoservice function
def get_fun_desc(fun):
    fun_desc = [f.get('Description') for f in get_fun_info()[0] if fun in f.values()]
    print(fun_desc[0])

#Validate that the geoservice function is valid
def check_fun(fun):
    funs = [f.get('Geosupport Function') for f in get_fun_info()[0]]
    check = [f for f in funs if f in [fun]]
    if len(check) > 0:
        return check[0]
    else:
        raise ValueError('The function defined, {}, does not exist.'.format(fun))

#Define the functions for getting the url for the specificed geoservice function
def substr_url(url, key, oldvalue, newvalue):
    url = url.get(key)
    new_url = url.replace(oldvalue, newvalue)
    return new_url

def get_fun_url(fun):
    funs = {u.get('Function'): geo_urls.svc_url + substr_url(u, 'Example', geo_urls.svc_url, '')[0:substr_url(u, 'Example', geo_urls.svc_url, '').find('?')] + '?'.strip() for u in get_fun_info()[1]}
    fun_url = funs.get(fun)
    return fun_url

#Define the function for getting the required arguments for each geoservice function
def get_fun_args(fun):
        oldvalue = get_fun_url(fun)
        
        funs = {u.get('Function'): substr_url(u, 'Example', oldvalue, '') for u in get_fun_info()[1] if u.get('Function') in [fun]}
        
        args = {fun: [i[0:i.find('=')] for i in str(funs.get(fun)).split('&')]}
        return args

#Get the geoservice function argument as a dictionary
def get_arg_dict(fun):
    args = get_fun_args(fun).values()
    args_dict = {k: '' for a in args for k in a}
    return args_dict

#Check that the keyword arguments supplied match those required for each geoservice
def check_fun_args(fun, **fun_args):

    fun1 = check_fun(fun)
        
    fun_url = get_fun_url(fun1)
    
    exp_arg = get_arg_dict(fun1)

    arg_diff = set(exp_arg) - set(fun_args)
    
    if len(arg_diff) > 0:
        missing_args = ', '.join([d for d in arg_diff])
        raise TypeError('Not all required arguments supplied. Missing: {}.'.format(missing_args))

#Create the function that gets the quoted and safe URL with arguments for the geoservice call
def construct_args_url(fun, **fun_args):
        check_fun_args(fun, **fun_args)
        
        args_url = '&'.join([str(k) + '=' + str(v) for k,v in fun_args.items()])
        call_url = quote(get_fun_url(fun) + args_url, safe = ':/?&=')

        return call_url