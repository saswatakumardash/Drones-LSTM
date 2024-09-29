import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Attention
from tensorflow.keras.optimizers import Adam

def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        Attention(),
        LSTM(32),
        Dense(3)
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    return model

def train_model(X, y, epochs=50, batch_size=32):
    model = create_lstm_model((X.shape[1], X.shape[2]))
    
    history = model.fit(
        X, y,
        validation_split=0.2,
        epochs=epochs,
        batch_size=batch_size
    )
    
    return model, history
