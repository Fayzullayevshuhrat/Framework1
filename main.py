from app import FrameWorkApp

app = FrameWorkApp()

@app.route("/home")
def home(request,response):
    response.text = "About pagedan alangali salom!"


@app.route("/about")
def about (request,response):
    response.text = "about pageidan alangali salom!"

@app.route("/contact")
def contact (request,response):
    response.text = "91 336 2084"