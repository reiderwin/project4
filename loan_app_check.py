import numpy as np        
import pickle


model = pickle.load(open('Resources/lr_classifier.pkl', 'rb'))       
chance=0     

# input = [250,70,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0]
# what format is web form info arriving in? will have to be converted to array        
def get_score()      
    data = np.array(WEB_FORM_ARRAY)[np.newaxis, :]  # converts shape for model test
    predict = model.predict(data)  # runs model on the data
    prob= model.predict_proba(data)

    if predict == [1]:
        prediction = "We predict success, congratulations!"
    else:
        prediction = "Sorry, you will likely not qualify."

    prob= model.predict_proba(data)

    if predict == [1]:
        chance = prob[0][1]
    else:
        chance = prob[0][0]

    return render_template("WHATEVER_PAGE_WE_USE.html",  prediction= prediction, probability=prob)
    # print(prediction)
    # print(f'Probability {chance: .2%}')
