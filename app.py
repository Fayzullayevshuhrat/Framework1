class FrameworkApp:
    def __call__(self,environ,start_response):
        status = "200 Ok"
        headers = [("Content-type","text/html")]

        start_response(status,headers)
        return [b"assalomu aleykum mening ismim Shuhrat, Familiyam Fayzulloyev!!!!!!!!!!!"]