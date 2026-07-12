#global scopes
global_v = 10

def fn1():
    enclosed_v = 5
    def fn2():
        local_v = 15    #local scope: variable declared inside a func... only accessible inside the func
        print("access to local", local_v)
        print("access to enclosed", enclosed_v)
    fn2()

fn1()


