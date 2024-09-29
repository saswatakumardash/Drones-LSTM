import airsim
import numpy as np
import time
from src.safety_checker import SafetyChecker

class DroneMOAAPP:
    def __init__(self, model, config):
        self.model = model
        self.config = config
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

        self.state_history = []
        self.safety_checker = SafetyChecker(self.client, config)

    def get_state(self):
        state = self.client.getMultirotorState()
        position = state.kinematics_estimated.position
        velocity = state.kinematics_estimated.linear_velocity
        return np.array([
            position.x_val, position.y_val, position.z_val,
            velocity.x_val, velocity.y_val, velocity.z_val
        ])

    def predict_next_waypoint(self, goal):
        if len(self.state_history) < self.config.SEQ_LENGTH:
            return goal  # If not enough history, move towards the goal

        recent_states = np.array(self.state_history[-self.config.SEQ_LENGTH:])
        prediction = self.model.predict(recent_states.reshape(1, self.config.SEQ_LENGTH, 6))
        return prediction[0]

    def move_drone(self, waypoint):
        if self.safety_checker.is_safe_move(waypoint):
            self.client.moveToPositionAsync(waypoint[0], waypoint[1], waypoint[2], 5).join()
        else:
            print("Unsafe move detected. Executing collision avoidance.")
            self.safety_checker.avoid_collision()

    def is_waypoint_reached(self, current_position, waypoint):
        distance = np.linalg.norm(current_position - waypoint)
        return distance < self.config.DISTANCE_THRESHOLD

    def takeoff(self, location):
        print(f"Taking off at location: {location}")
        self.client.takeoffAsync().join()
        self.move_drone(location)

    def land(self, location):
        print(f"Landing at location: {location}")
        self.move_drone(location)
        self.client.landAsync().join()

    def run_mission(self, mission):
        self.takeoff(mission['takeoff'])

        for waypoint in mission['waypoints']:
            print(f"Moving to waypoint: {waypoint}")
            self.navigate_to_waypoint(waypoint)

        self.land(mission['landing'])
        print("Mission complete.")

    def navigate_to_waypoint(self, goal):
        for step in range(self.config.MAX_STEPS):
            current_state = self.get_state()
            self.state_history.append(current_state)
            current_position = current_state[:3]

            if self.is_waypoint_reached(current_position, goal):
                print(f"Waypoint reached in {step} steps!")
                break

            next_waypoint = self.predict_next_waypoint(goal)
            print(f"Moving to intermediate point: {next_waypoint}")
            self.move_drone(next_waypoint)

            time.sleep(self.config.STEP_DELAY)

    def cleanup(self):
        self.client.armDisarm(False)
        self.client.enableApiControl(False)
