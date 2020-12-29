
from flask import Flask, jsonify, request
from osutils import getOperatingSystemVersion
from temperature import getTemperature

app=Flask(__name__)

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'Os version is '+getOperatingSystemVersion()})


@app.route('/getTemperature',methods=['GET'])
def getTemperature():

    temperatureVal=-99
    if getOperatingSystemVersion=="Linux":
        return jsonify({'message':'temperature is '+str(temperature.getTemperature())})
    else:
        return jsonify({'message':'temperature is '+str(temperatureVal)})    
    

if __name__== '__main__':
    app.run(debug=True,port=3000)