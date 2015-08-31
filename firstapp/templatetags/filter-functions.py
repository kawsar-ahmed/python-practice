from django import template

register = template.Library()

def check_number(value, arg):
	lenth=len(value)
	if lenth is 11:
		return value
	else:
		return arg
	

register.filter('check_number', check_number)

def empty_check(value, arg):
    lenth = len(value)
    
    if lenth is 0:
        return arg
    else:
        return value
       

register.filter('empty_check', empty_check)