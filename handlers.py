from modules.res import ParcingResource as Res
from modules.items import Items
from connections import Connect 



def get_all_resources() -> list:
    db = Connect()
    return db.get_all_resourses()

def get_one_res(res_name) -> dict:
    db = Connect()
    return db.get_elements_for_res(res_name=res_name)



