from src.lstm_model import train_model
from src.airsim_integration import DroneMOAAPP
from src.data_generation import generate_training_data
from src.simulation import Simulation
from config.config import Config

def main():
    config = Config()

    # Generate training data
    print("Generating training data...")
    X, y = generate_training_data(config.NUM_SAMPLES, config.SEQ_LENGTH)

    # Train the LSTM model
    print("Training the LSTM model...")
    trained_model, _ = train_model(X, y, epochs=config.EPOCHS, batch_size=config.BATCH_SIZE)

    # Save the model
    trained_model.save("moaapp_lstm_model.h5")
    print("Model saved as 'moaapp_lstm_model.h5'")

    # Initialize simulation
    simulation = Simulation(config)
    simulation.setup_environment()

    # Initialize drone
    drone = DroneMOAAPP(trained_model, config)

    # Run simulation
    simulation.run_simulation(drone)

if __name__ == "__main__":
    main()
