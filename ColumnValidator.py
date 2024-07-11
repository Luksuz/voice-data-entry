import json

class ColumnValidator:
    def __init__(self) :
        self.columns = {
            'Time': None, 
            'Relative humidity': None, 
            'Temperature': None, 
            'Barometer': None, 
            'Wind': None, 
            'Present Weather': None, 
            'Sea scale': None, 
            'Ground track': None, 
            'Course steered': None, 
            'Helm Err': None, 
            'Magnetic compass heading': None, 
            'Swell': None, 
            'RPM': None, 
            'Log': None, 
            'Distance made good NM': None, 
            'Remarks': None
        }
        
    def is_complete(self):
        if None in self.columns.values:
            return False
        else: 
            return True
    
    def add_col_value(self, value_dict):
        print(json.loads(value_dict))
        key, value = json.loads(value_dict)
        self.columns[key] = value