from fastapi import FastAPI
from db.models import Machine
from pydantic import BaseModel



app = FastAPI()




@app.get("/")
def welcome():
    return {"data":"Welcome to the EnergyOpt Backend"}



@app.get("/machine/")
def get_one_machine(id:str):
    machine_data = Machine.get_machine(id)

    return machine_data



@app.post("/machine/")
def add_one_machine(machine_data:Machine):
    print(Machine.add_machine(machine_data.model_dump()))
    return {"response":"Successfully Added a machine"}



@app.get("/machine/all/")
def get_all_machines():
    all_machines = Machine.get_all_machines()
    print(all_machines)
    return {"response":all_machines}


@app.post("/machine/input/")
def machine_input():
    pass


@app.get("/machine/data/")
def machine_data():
    pass




