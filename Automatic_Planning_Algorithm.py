class Planner:
    def __init__(self, world, arm):
        self.world = world
        self.arm = arm

    def plan_to_stack(self, blocks_order, target):
        for block_name in blocks_order:
            self.arm.hover(block_name)  # Move the arm to the block's location
            self.arm.grab(block_name)  # Pick up the block
            self.arm.hover(target)  # Move to the target location
            self.arm.release(target)  # Place the block on the target stack
