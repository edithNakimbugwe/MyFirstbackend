from flask import Flask, request,render_template
import pickle

app = Flask(__name__)

# Load the trained model
loaded_model = pickle.load(open('savemodel','rb'))
@app.route('/')
def hpme():
   return render_template("index.html", **locals())

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        AGE= float(request.form["Age"]) 	
        ALB= float(request.form["ALB"])
        ALP= float(request.form["ALP"]) 	
        ALT= float(request.form["ALT"]) 	
        AST= float(request.form["AST"])	
        BIL= float(request.form["BIL"])	
        CHE= float(request.form["CHE"])
        CHOL= float(request.form["CHOL"])
        GGT=  float(request.form["GGT"])
        PROT= float(request.form["PROT"])
    except ValueError:
        return "Invalid value for Age field", 400
    except KeyError:
        return "Age field is missing from the form data", 400
    reuslt = loaded_model.predict([[AGE,ALB,ALP,ALT,AST,BIL,CHE,CHOL,GGT,PROT]])[0]
    return render_template("index.html", **locals())
if __name__ == '__main__':
    app.run(debug=True)
