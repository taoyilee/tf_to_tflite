from pathlib import Path

import tensorflow as tf


def pb2tflite(export_dir):
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
    tflite_model = converter.convert()
    with open(output_dir / "mnist.tflite", "wb") as fptr:
        fptr.write(tflite_model)
