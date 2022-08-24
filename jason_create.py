from distutils.log import info
import json
from tokenize import Name
from unicodedata import name
data = {}

def set_emp(name, add, phone, imp_id, sex,city):
d = dict(
    Name=name,
    address=add,
    phone_no=phone,
    imp_id=imp_id,
    sex=sex,
    city=city,
)
return d

def create_json_file(file_name):
    info = json.dumps(data,indent=4)
    with open(file_name, "w") as f:
        f.write(info)


        def load_json(file_name):
            with open(file_name)
    return json.loads(info)    