from flask import Flask, request, jsonify,render_template
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('stack_model.joblib')

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        # Extract input features from the request form
        AGE = float(request.form["Age"])
        ALB = float(request.form["ALB"])
        ALP = float(request.form["ALP"])
        ALT = float(request.form["ALT"])
        AST = float(request.form["AST"])
        BIL = float(request.form["BIL"])
        CHE = float(request.form["CHE"])
        CHOL = float(request.form["CHOL"])
        GGT = float(request.form["GGT"])
        PROT = float(request.form["PROT"])
         # Extract input features from the request form
        data = request.form.to_dict()
        input_features = [[float(value) for value in data.values()]]
    except ValueError:
        return "Invalid value for one or more fields", 400
    except KeyError:
        return "One or more fields are missing from the form data", 400
    
    # Combine input features into a single input vector
    input_features = [[AGE, ALB, ALP, ALT, AST, BIL, CHE, CHOL, GGT, PROT]]

    # Make predictions using the loaded model
    predictions = model.predict(input_features)
    
     # Determine diagnostic outcome
    results = predictions[0]
    if results == 0:
        diagnostic_outcome = 'Person is Negative'
    elif results == 1:
        diagnostic_outcome = 'Person is at high risk of attaining liver disease'
    elif results == 2:
        diagnostic_outcome = 'Person has Hepatitis'
    elif results == 3:
        diagnostic_outcome = 'Person has Fibrosis'
    else:
        diagnostic_outcome = 'Person has Cirrhosis'

    # Prepare the response
    response = {
            'predictions': predictions.tolist(),
            'diagnostic_outcome': diagnostic_outcome
        }


    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
