def func_a(): 
    print('Func A started')
    func_b()
    print('Func A ended')

def func_b(): 
    print('Func B started')
    func_c()
    print('Func B ended')

def func_c(): 
    print('Func C started')
    result = 10 / 0 # Intentional error
    print('Func C ended')


# Main
func_a()
