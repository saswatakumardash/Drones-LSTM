 UAV Path Planning with Multi-Objective Reinforcement Learning

This project implements a UAV path planning system using LSTM-based neural networks and the AirSim simulator. It combines **Multi-Objective Reinforcement Learning (MORL)** with dynamic attention mechanisms to improve adaptability, efficiency, and safety during UAV navigation in complex environments.

## Key Features

- **LSTM-Based Path Prediction**: Uses Long Short-Term Memory networks to predict the next waypoint based on past UAV states.
- **Multi-Objective Optimization**: Simultaneously optimizes for path length, energy efficiency, safety, and mission goals.
- **Dynamic Attention Mechanism**: The system adapts its focus on the most relevant environmental features.
- **Simulation with AirSim**: Utilizes Microsoft's AirSim platform to simulate the UAV mission in a dynamic, obstacle-rich environment.
- **Safety Checking & Collision Avoidance**: A built-in safety checker monitors potential collisions and makes real-time adjustments to the UAV's path.

## Project Structure

```
project_root/
│
├── src/
│   ├── lstm_model.py           # LSTM model and training functions
│   ├── airsim_integration.py   # Integration with AirSim for UAV control
│   ├── data_generation.py      # Generate training data for LSTM model
│   ├── mission_planner.py      # User input for mission planning
│   ├── simulation.py           # Simulation setup and mission execution
│   └── safety_checker.py       # Safety checks and collision avoidance
│
├── config/
│   └── config.py               # Configuration settings for training and simulation
│
├── main.py                     # Main script to run the entire system
├── requirements.txt            # Python dependencies
└── README.md                   # Project information and setup instructions
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install dependencies**:
   Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up AirSim**:
   - Follow the official [AirSim documentation](https://microsoft.github.io/AirSim/) to install and set up an AirSim simulation environment.

## Running the Project

1. **Prepare your AirSim environment**:
   - Open your AirSim environment and ensure it's running correctly.

2. **Run the main script**:
   Execute the following command to start the training, simulation, and mission planning process:
   ```bash
   python main.py
   ```

3. **Mission planning**:
   - You will be prompted to input takeoff location, waypoints, and landing location.

4. **Observe simulation**:
   - The UAV will navigate through the simulated environment, avoiding obstacles and completing the mission.

## Configuration

Adjust the parameters in `config/config.py` to suit your needs:
- **NUM_SAMPLES**: Number of training samples to generate.
- **SEQ_LENGTH**: Length of the sequence for LSTM training.
- **EPOCHS**: Number of training epochs.
- **BATCH_SIZE**: Batch size during training.
- **MAX_STEPS**: Maximum number of steps the UAV takes to reach a waypoint.
- **SAFE_DISTANCE**: Minimum distance from obstacles.

## Future Enhancements

- **Real-world Testing**: Extend the model for real-world UAV navigation scenarios.
- **Improved Dynamic Attention**: Enhance the attention mechanism for better adaptation in highly dynamic environments.
- **Swarm UAV Integration**: Develop collaborative path planning for multiple UAVs.

## Authors


- **Saswata Kumar Dash**
-  **Geoffrey Anto Ignatius E**

---

This project is part of ongoing research in adaptive UAV navigation using Multi-Objective Reinforcement Learning.
