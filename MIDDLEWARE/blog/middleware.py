def mymiddleware(get_response):
    print("initilization first")
    def myfun(request):
        print("this is before view")
        response=get_response(request)
        print("this is after view")
        return response
    return myfun

def momiddleware(get_response):
    print("initilization second")
    def myfun(request):
        print("this is before view")
        response=get_response(request)
        print("this is after view")
        return response
    return myfun