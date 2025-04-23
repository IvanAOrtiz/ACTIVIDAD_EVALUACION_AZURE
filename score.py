
import json
import joblib
import numpy as np
import pandas as pd
from azureml.core.model import Model

def init():
  global model
  model_path = Model.get_model_path('model')
  model = joblib.load(model_path)



def run(raw_data):
  try: ## Try la predicción.
    data = json.loads(raw_data)['data'][0]
    data = pd.DataFrame(data)
    
    #Realizar prediccion
    result = model.predict(data).tolist()

    return json.dumps(result_finals)
  except Exception as e:
    return json.dumps(str(e))
