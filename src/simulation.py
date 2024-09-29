import airsim
import time
import numpy as np

class Simulation:
    def __init__(self, config):
        self.config = config
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()

    def setup_environment(self):
        print("Setting up simulation environment...")
        # Add obstacles
        self.add_obstacles()
        # Set weather conditions
        self.set_weather()

    def add_obstacles(self):
        # Add some random obstacles in the environment
        for _ in range(self.config.NUM_OBSTACLES):
            position = np.random.uniform(-50, 50, 3)
            self.client.simSpawnObject(f"obstacle_{_}", "Cube", {"Rotation": "0, 0, 0", "Scale": "1, 1, 1"}, position.tolist())

    def set_weather(self):
        # Set random weather conditions
        weather = airsim.WeatherParameter(
            rain=np.random.uniform(0, 0.5),
            fog=np.random.uniform(0, 0.5),
            wind=airsim.Vector3r(np.random.uniform(-5, 5), np.random.uniform(-5, 5), 0)
        )
        self.client.simSetWeatherParameter(weather)

    def run_simulation(self, drone):
        print("Starting simulation...")
        mission_planner = MissionPlanner(self.config)
        mission = mission_planner.plan_mission()

        try:
            drone.run_mission(mission)
        except Exception as e:
            print(f"Simulation error: {e}")
        finally:
            drone.cleanup()

        print("Simulation complete.")
