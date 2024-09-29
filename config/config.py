class Config:
    # Data generation
    NUM_SAMPLES = 10000
    SEQ_LENGTH = 50

    # Model training
    EPOCHS = 50
    BATCH_SIZE = 32

    # AirSim
    MAX_STEPS = 1000
    DISTANCE_THRESHOLD = 2.0
    STEP_DELAY = 0.1  # Reduced for faster simulation
    SAFE_DISTANCE = 5.0  # Minimum safe distance from obstacles

    # Simulation
    NUM_OBSTACLES = 10
