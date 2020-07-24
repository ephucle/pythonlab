from card import *
hand = Hand()

#obj.mro(...) method of builtins.type instance
#    mro() -> list
#    return a type's method resolution order

#>>> type(hand).mro()
#[<class 'card.Hand'>, <class 'card.Deck'>, <class 'object'>]


def find_defining_class(obj, method_name):
    ''' Tim class tuong ung cua obj.medtho_name '''
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty

#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$ python3 class_debug.py
#<class 'card.Deck'>

print (find_defining_class(hand, 'shuffle')) #<class 'card.Deck'>


def find_all_class(obj):
    ''' Tim tat ca class cua obj '''
    list_of_class_name = []
    for classname in type(obj).mro():
        if classname not in list_of_class_name:
            list_of_class_name.append(classname)
    return list_of_class_name

print (find_all_class(hand)) #[<class 'card.Hand'>, <class 'card.Deck'>, <class 'object'>]