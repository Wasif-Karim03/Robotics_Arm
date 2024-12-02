class Planner:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plan(self):
        actions = []
        current_state = self.initial_state

        while current_state != self.goal_state:
            action = self.next_action(current_state)
            if action:
                actions.append(action)
                current_state = self.apply_action(current_state, action)
            else:
                raise Exception("No valid actions available!")
        
        return actions

    def next_action(self, state):
        # Determine the next valid action based on preconditions
        # and constraints. This could involve heuristics or STRIPS logic.
        pass

    def apply_action(self, state, action):
        # Apply the action to the current state and return the new state.
        pass
