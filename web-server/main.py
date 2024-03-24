import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def grt_list():
    return [1,2,3,4]

@app.get("/contact", response_class=HTMLResponse)
def grt_list():
    return """ 
            <h1> hola Soy un h1 </h1> 
            <p> Hola soy un parrafo </p>

           """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()
