
from flask import Flask, jsonify, request
from osutils import getOperatingSystemVersion
#from temperature import getTemperature
from dht11_lib import getTemperatureHumidity

app=Flask(__name__)

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'Os version is '+getOperatingSystemVersion()})


@app.route('/getTemperature',methods=['GET'])
def getTemperature():
    """
    temperatureVal=-99
    if getOperatingSystemVersion=="Linux":
        return jsonify({'message':'temperature is '+str(dht112.getTemperature())})
    else:
        return jsonify({'message':'temperature is '+str(getOperatingSystemVersion)})    
    """

    return jsonify({'message':'temperature is '+getTemperatureHumidity()})


if __name__== '__main__':
    app.run(debug='True',host='0.0.0.0',port=3000)
