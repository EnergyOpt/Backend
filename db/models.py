from datetime import datetime
from pydantic import BaseModel, Field
from db.connection import db
## users

machine_collection = db['Machine']
machine_data_collection = db["MachineData"]

index_name = machine_data_collection.create_index([
    ('machine_id', 1),  # Ascending order
    ('timestamp', -1)   # Descending order
])
class Machine(BaseModel):
    name:str
    min_power:int
    max_power:int
    min_current:int
    max_current:int
    short_description:str
    manual:str
    active:bool

    created_at:datetime = Field(default=datetime.now())
    updated_at:datetime = Field(default=datetime.now())

    @classmethod
    def add_machine (cls,machine_data):
        machine = cls(**machine_data)
        result = machine_collection.insert_one(machine.model_dump())
        return result
        # return {"message": "The user was already added"}
    
    @classmethod
    def get_machine(cls, machine_id):
        machine_data = machine_collection.find_one({"_id":machine_id})
        if machine_data is not None:
            return machine_data
        

    @classmethod
    def get_all_machines(cls):
        all_data = machine_collection.find()
        if all_data is not None:
            return [
                {**data, '_id': str(data['_id'])} for data in all_data
            ]
        else:
            return []
        


class MachineData(BaseModel):
    machine_id:str
    timestamp:datetime
    power:int
    current:int
    prediction:int
    created_at:datetime = Field(default=datetime.now())


    @classmethod
    def add_stream_data (cls,machine_data):
        machine = cls(**machine_data)
        result = machine_data_collection.insert_one(machine.model_dump())
        return result
        # return {"message": "The user was already added"}
    
    @classmethod
    def get_machine_data(cls, machine_id):
        machine_data = machine_data_collection.find_one({"_id":machine_id})
        if machine_data is not None:
            return machine_data
        


        
