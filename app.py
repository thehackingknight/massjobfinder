from flask import Flask, render_template, request
from scraper import Jobs, GetFullDesc

app = Flask(__name__)


@app.route("/",methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')

   
@app.route("/jobs", methods=["GET", "POST"])
def jobs_router():

    if request.method == "GET":
        search_string = request.args.get("q")
        return render_template("index.html",jobs= Jobs().jobs(search_string), search=search_string)

    if request.method == "POST":

        url = request.get_json()["url"]
        site = request.get_json()['site']

        gfd = GetFullDesc()
        gfd_methods = [gfd.indeed, gfd.linkedin,gfd.careers24]
        for method in gfd_methods:

            if site.lower() == method.__name__:
                desc = method(url)
                return str(desc)

if __name__ == "__main__":
    app.run()