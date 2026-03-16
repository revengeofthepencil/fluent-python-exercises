registry = set()

def register(active=True):
    def decorate_that_thing(func):
        print(f'running register({func}). active = {active}')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate_that_thing

@register()
def f1():
    print('do the f1 thing')

@register(active=False)
def f2():
    print('do the f2 thing')

def f3():
    print('do the f3 thing')

def main():
    print('check the registry decorator')
    print('registry -> ', registry)
    
    register()(f3)
    print('registry -> ', registry)

    register(active=False)(f1)
    print('registry -> ', registry)

if __name__ == '__main__':
    main()