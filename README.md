# Tensorflow .pb to Tensorflow lite .tflite conversion

This repository contains an example which converts [Tensorflow](https://www.tensorflow.org/) 
[SavedModel](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md) 
(a.k.a. .pb format) to Tensorflow lite model (*.tflite) 

### Installing

```
git clone git@github.com:taoyilee/tf_to_tflite.git
cd mnist_to_tflite
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

```
source venv/bin/activate
python main.py
# Retreive .tflite file at output/mnist.tflite
```
The output tflite model is visualized below (using [Netron](https://lutzroeder.github.io/netron/))

![visualization](mnist.tflite.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
