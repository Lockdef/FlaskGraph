from io import BytesIO
import base64

from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

def img_format(byte):
    byte = base64.b64encode(byte.getvalue()).decode("utf-8") 
    img = "data:image/png;base64,{}".format(byte)
    return img

@app.route('/')
def index():
    byte = BytesIO()
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    sns.jointplot(x, y)
    plt.savefig(byte)
    graph = img_format(byte)
    return render_template('index.html',
        graph=graph)

if __name__=='__main__':
    app.run(host="127.0.0.1", debug=True)