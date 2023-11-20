from django.shortcuts import render
import joblib
import numpy as np  
import tensorflow as tf
#from tensorflow.keras.models import load_model 
from sklearn.preprocessing import StandardScaler
scaler  = StandardScaler()
scaler = joblib.load('scaler.pkl')
model = tf.keras.models.load_model('deepModel.h5')


def predictor(request):
    if request.method == 'POST':
        age = (int)(request.POST['age'])  
        gender = (int)(request.POST['gender'])  
        cptype = (int)(request.POST['cptype'])   
        trestbps = (int)(request.POST['trestbps'])  

        cholestrol = (int)(request.POST['cholestrol'])  
        fbs = (int)(request.POST['fbs'])   
        restecg = (int)(request.POST['restecg'])  
        thalch = (int)(request.POST['thalch']) 

        exang = (int)(request.POST['exang'])  
        stdepression = (float)(request.POST['stdepression'])   
        slope = (int)(request.POST['slope'])  
        vessels = (int)(request.POST['vessels']) 
        
        thal = (int)(request.POST['thal'])    

        input_data = np.array([[age,gender,cptype,trestbps,cholestrol,fbs,restecg,thalch,exang,stdepression,slope,vessels,thal]])

        test_data = input_data.reshape(1, -1)
        test_data = scaler.transform(test_data)
        predictions = model.predict(test_data)
        
        if predictions>0.5:
            predicted_class_name = "Presence"
        else:
            predicted_class_name = "Absence"

        return render(request, 'result.html', {'result': predicted_class_name})
    
    return render(request, 'main.html')



