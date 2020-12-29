# PyInput
PyInput module for Python 3.0 version 1.3

This module provides you with various types of _user safe input functions_ for Python 3.0:

  intInput(overlay_info='',main_info='',traceback_info='')                                     
  floatInput(overlay_info='',main_info='',traceback_info='')                              
  strInput(overlay_info='',main_info='',traceback_info='')

  intLimitInput(limit,overlay_info='',main_info='',traceback_info='')
  floatLimitInpup(limit,overlay_info='',main_info='',traceback_info='')
  strLimitInput(limit,overlay_info='',main_info='',traceback_info='')

  boolInput(overlay_info='', main_info='', traceback_info='', syn_true='True', syn_false='False')

/further help on the functions and their attributes can be found using the help() function

To import this as extern module use                                                                           
  from <path> import <function>     #import one or more functions                                                  
  from <path> import *              #import every function

To import this as global module, include this module under                                              
  [...]\Python\Lib                                                                                  
After then you can import this module as global module                                                
  from PyInput import <function>  #import one or more functions                                                        
  from PyInput import *           #import every function
