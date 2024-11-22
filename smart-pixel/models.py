import tensorflow as tf
import qkeras

from tensorflow.keras.layers import Activation, Dense, Input, BatchNormalization
from qkeras.qlayers import QDense, QActivation
from fkeras.fdense import FQDense

NUM_CLASSES = 3


def dense_model(in_shape, dense_width=128):
    """
    Original float model
    """
    x = x_in = Input(in_shape, name="input")
    x = Dense(dense_width, name="dense1")(x)
    x = BatchNormalization()(x)
    x = Activation("relu", name="relu1")(x)
    x = Dense(NUM_CLASSES, name="dense2")(x)
    model = tf.keras.models.Model(inputs=x_in, outputs=x)
    return model


def qkeras_dense_model(
    in_shape,
    dense_width=58,
    logit_total_bits=4,
    logit_int_bits=0,
    activation_total_bits=8,
    activation_int_bits=0,
    alpha=1,
    logit_quantizer="quantized_bits",
    activation_quantizer="quantized_relu",
):
    """
    QKeras model
    """
    logit_quantizer = getattr(qkeras.quantizers, logit_quantizer)(
        logit_total_bits,
        logit_int_bits,
        alpha=alpha,
    )
    activation_quantizer = getattr(qkeras.quantizers, activation_quantizer)(
        activation_total_bits,
        activation_int_bits,
    )
    x = x_in = Input(in_shape, name="input1")
    x = QDense(
        dense_width,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
        name="dense1",
    )(x)
    x = BatchNormalization()(x)

    x = QActivation(activation=activation_quantizer)(x)
    x = QDense(
        NUM_CLASSES,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
        name="dense2",
    )(x)
    model = tf.keras.models.Model(inputs=x_in, outputs=x)
    return model


def fkeras_dense_model(
    in_shape,
    dense_width=58,
    logit_total_bits=3,
    logit_int_bits=0,
    activation_total_bits=6,
    activation_int_bits=1,
    alpha=1,
    logit_quantizer="quantized_bits",
    activation_quantizer="quantized_relu",
):
    """
    QKeras model
    """
    logit_quantizer = getattr(qkeras.quantizers, logit_quantizer)(
        logit_total_bits,
        logit_int_bits,
        alpha=alpha,
    )
    activation_quantizer = getattr(qkeras.quantizers, activation_quantizer)(
        activation_total_bits,
        activation_int_bits,
    )
    x = x_in = Input(in_shape, name="input1")
    x = FQDense(
        dense_width,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
    )(x)
    x = BatchNormalization()(x)
    x = QActivation(activation=activation_quantizer)(x)

    # x = FQDense(
    #     dense_width,
    #     kernel_quantizer=logit_quantizer,
    #     bias_quantizer=logit_quantizer,
    # )(x)
    # x = BatchNormalization()(x)
    # x = QActivation(activation=activation_quantizer)(x)

    # x = FQDense(
    #     dense_width,
    #     kernel_quantizer=logit_quantizer,
    #     bias_quantizer=logit_quantizer,
    # )(x)
    # x = BatchNormalization()(x)
    # x = QActivation(activation=activation_quantizer)(x)


    x = FQDense(
        NUM_CLASSES,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
    )(x)
    model = tf.keras.models.Model(inputs=x_in, outputs=x)
    return model

def fkeras_dense_model_large(
    in_shape,
    dense_width=58,
    logit_total_bits=3,
    logit_int_bits=0,
    activation_total_bits=6,
    activation_int_bits=1,
    alpha=1,
    logit_quantizer="quantized_bits",
    activation_quantizer="quantized_relu",
):
    """
    QKeras model
    """
    logit_quantizer = getattr(qkeras.quantizers, logit_quantizer)(
        logit_total_bits,
        logit_int_bits,
        alpha=alpha,
    )
    activation_quantizer = getattr(qkeras.quantizers, activation_quantizer)(
        activation_total_bits,
        activation_int_bits,
    )
    x = x_in = Input(in_shape, name="input1")
    x = FQDense(
        dense_width,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
    )(x)
    x = BatchNormalization()(x)
    x = QActivation(activation=activation_quantizer)(x)

    x = FQDense(
        dense_width,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
    )(x)
    x = BatchNormalization()(x)
    x = QActivation(activation=activation_quantizer)(x)

    x = FQDense(
        dense_width,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
    )(x)
    x = BatchNormalization()(x)
    x = QActivation(activation=activation_quantizer)(x)

    # x = FQDense(
    #     dense_width,
    #     kernel_quantizer=logit_quantizer,
    #     bias_quantizer=logit_quantizer,
    # )(x)
    # x = BatchNormalization()(x)
    # x = QActivation(activation=activation_quantizer)(x)

    # x = FQDense(
    #     dense_width // 2,
    #     kernel_quantizer=logit_quantizer,
    #     bias_quantizer=logit_quantizer,
    # )(x)
    # x = BatchNormalization()(x)
    # x = QActivation(activation=activation_quantizer)(x)

    x = FQDense(
        NUM_CLASSES,
        kernel_quantizer=logit_quantizer,
        bias_quantizer=logit_quantizer,
    )(x)
    # x = BatchNormalization()(x)
    # x = QActivation(activation=activation_quantizer)(x)
    model = tf.keras.models.Model(inputs=x_in, outputs=x)
    return model



def dense_model_large(
    in_shape,
    dense_width=32,
):
    """
    QKeras model
    """
    x = x_in = Input(in_shape, name="input1")
    x = Dense(dense_width)(x)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    x = Dense(dense_width)(x)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    x = Dense(dense_width)(x)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    x = Dense(NUM_CLASSES)(x)
    model = tf.keras.models.Model(inputs=x_in, outputs=x)
    return model