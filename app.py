from flask import Flask, request, make_response
import numpy as np
import re

app = Flask(__name__)

# example input: (10,12),[(1.5,1.5),(4.0,1.5),(1.5,8.0),(4.0,8.0)]
@app.route('/pix-cords', methods=['POST'])
def pix_cords():
    """
    Performs a simple input check, then performs and returns the computations

    Note: if this was a production app I don't think using 'eval' would be safe
    """
    contType = request.headers.get('Content-Type')
    if (contType != 'text/plain'):
        return '''Sorry, that content type is not supported.
    Usage: curl -X POST -H "Content-type: text/plain" -d "<image dimensions>,<corner points>" 0.0.0.0:5000/pix-cords''', 400

    data = request.data.decode('utf-8')
    imgDims, cornPts = eval(data)

    response = make_response(str(calculate(imgDims, cornPts)), 200)
    response.mimetype = 'text/plain'
    return response


def calculate(imgDims, cornPts):
    """
    Calculates and returns x,y coordinates at which to plot evenly spaced pixels within the provided corner points.
    """
    cornPts = np.array(cornPts)

    # each rectangle isn't rotated, so we just need linearly spaced points
    resX = np.linspace(np.min(cornPts[:,0]), np.max(cornPts[:,0]), num=imgDims[0])
    resY = np.linspace(np.min(cornPts[:,1]), np.max(cornPts[:,1]), num=imgDims[1])

    # making sure to match the format from the spec: top left is sol[0,0,0]
    return [[[resX[i],resY[j-1]] for i in range(imgDims[0])] for j in range(imgDims[1], 0, -1)]


if __name__ == '__main__':
    app.run(host="0.0.0.0")

