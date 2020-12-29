'''
PyInput module Version 1.3
This module creates advanced inputs for Python.
They help to generate user safe, specifice, inputs.
'''
__author__='Elijah Zeidler'
__contact__='GitHub "EloleMuum"'

#----------------------------------------------------------------------------------------
def intInput(overlay_info='',main_info='',traceback_info=''):
    '''
    intInput generates an user safe integer input.
        -Overlay_info (str) will be displayed the line above input line.
        -Main_info (str) will be displayed on the display line.
        -Traceback_info (str) will be displayed if the input fails due to ValueError, 
         the input will be repeated.
    '''
    if overlay_info!='':
        print(overlay_info)
    while True:
        try:
            int_result=int(input(main_info))
            break
        except:
            print(traceback_info)
    return(int_result)
#----------------------------------------------------------------------------------------
def floatInput(overlay_info='',main_info='',traceback_info=''):
    '''
    floatInput generates an user safe float input.
        -Overlay_info (str) will be displayed the line above input line.
        -Main_info (str) will be displayed on the display line.
        -Traceback_info (str) will be displayed if the input fails due to ValueError, 
         input will be repeated.
    '''
    if overlay_info!='':
        print(overlay_info)
    while True:
        try:
            float_result=float(input(main_info))
            break
        except:
            print(traceback_info)
    return(float_result)
#----------------------------------------------------------------------------------------
def strInput(overlay_info='',main_info='',traceback_info=''):
    '''
    strInput generates an user safe string input.
        -Overlay_info (str) will be displayed the line above input line.
        -Main_info (str) will be displayed on the display line.
        -Traceback_info (str) will be displayed if the input fails due to ValueError, 
         input will be repeated.
    '''
    if overlay_info!='':
        print(overlay_info)
    while True:
        try:
            str_result=str(input(main_info))
            break
        except:
            print(traceback_info)
    return(str_result)
#----------------------------------------------------------------------------------------
def intLimitInput(limit,overlay_info='',main_info='',traceback_info=''):
    '''
    intLimitInput generates an user save, limited integer input.
        -Limit (tuple of integers) takes a tuple wich contains the limitation values as integers.
        -Overlay_info (str) will be displayed the line above input line.
        -Main_info (str) will be displayed on the display line.
        -Traceback_info (str) will be displayed if the input fails due to ValueError
         or LimitError; the input will be repeated.
    '''
    for i in range(len(limit)):
        assert type(limit[i])==int,'function argument "limit" needs to be a list of integers'
    if overlay_info != '':
        print(overlay_info)
    while True:
        try:
            var_result = int(input(main_info))
        except:
            print(traceback_info)
            continue
        if var_result in limit:
            return(var_result)
        print(traceback_info)
#----------------------------------------------------------------------------------------
def floatLimitInput(limit, overlay_info='', main_info='', traceback_info=''):
    '''
    floatLimitInput generates an user save, limited integer input.
        -Limit (tuple of floats) takes a tuple wich contains the limitation values as floats.
        -Overlay_info (str) will be displayed the line above input line.
        -Main_info (str) will be displayed on the display line.
        -Traceback_info (str) will be displayed ifror the input fails due to ValueError
         or LimitError; the input will be repeated.
    '''
    for i in range(len(limit)):
        assert type(limit[i]) == float, 'function argument "limit" needs to be a list of integers'
    if overlay_info != '':
        print(overlay_info)
    while True:
        try:
            var_result = float(input(main_info))
        except:
            print(traceback_info)
            continue
        if var_result in limit:
            return(var_result)
        print(traceback_info)
#----------------------------------------------------------------------------------------
def strLimitInput(limit, overlay_info='', main_info='', traceback_info=''):
    '''
    strLimitInput generates an user save, limited integer input.
        -Limit (tuple of strings) takes a tuple, wich contains the limitation values as strings.
        -Overlay_info (str) will be displayed the line above input line.
        -Main_info (str) will be displayed on the display line.
        -Traceback_info (str) will be displayed if the input fails due to ValueError
         or LimitError; the input will be repeated.
    '''
    for i in range(len(limit)):
        assert type(
            limit[i]) == float, 'function argument "limit" needs to be a list of integers'
    if overlay_info != '':
        print(overlay_info)
    while True:
        try:
            var_result = float(input(main_info))
        except:
            print(traceback_info)
            continue
        if var_result in limit:
            return(var_result)
        print(traceback_info)
#----------------------------------------------------------------------------------------
def boolInput(overlay_info='', main_info='', traceback_info='', syn_true='True', syn_false='False'):
    '''
    boolInput generates an user save boolean input.
        -Overlay_info (str) will be displayed the line above input line.
        -Main_info (str) will be displayed on the display line.
        -Traceback_info (str) will be displayed if the input fails due to ValueError;
         input will be repeated.
        -Syn_true (str) is the synonym for the boolean value of "True", standard is "True".
        -Syn_false (str) is the synonym for the boolean value of "False", standard is "False".
    '''
    if overlay_info != '':
        print(overlay_info)
    while True:
        try:
            var_result = str(input(main_info))
            if var_result == syn_true:
                var_result = bool(True)
                break
            elif var_result == syn_false:
                var_result = bool(False)
                break
            print(traceback_info)
        except:
            print(traceback_info)
    return(var_result)
#----------------------------------------------------------------------------------------
