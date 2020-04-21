import tensorflow as tf


def load_pb(export_dir):
    model = tf.saved_model.load(export_dir)
    f = model.signatures["serving_default"]
    return f
