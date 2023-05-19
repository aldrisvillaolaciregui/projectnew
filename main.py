from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from database import database

from schema import usuariosBasemodel

app = FastAPI()

templates=Jinja2Templates(directory="templates")#la ubicacion del directorio


app.mount("/static", StaticFiles(directory="static"), name="static")



@app.on_event("startup")#evento startup 
def startup():
    if database.is_closed():#si la base de datos esta desconectada ==>
        database.connect()#conectando la base de datos 
    print("conectado a la  base de datos ")  



#login 
@app.get("/")
async def login(request:Request):
    return templates.TemplateResponse("login.html", {"request":request})


@app.post("/")
async def login(request:Request, username:str=Form(...), password:str=Form(...)):
    user=usuariosBasemodel(username=username, password=password)
    cursor=database.cursor()
    print(user.username,user.password)
    query="SELECT password FROM usuarios WHERE username=%s"
    value=(user.username,)
    cursor.execute(query,value)
    response=cursor.fetchone()
    
    if response is None or response[0] != password:
        error="credenciales no validas"
        return templates.TemplateResponse("login.html", {"request":request, "message":error})
    response=RedirectResponse(url="/dashboard")
    response.set_cookie(key="user", value=username)



#fin login 