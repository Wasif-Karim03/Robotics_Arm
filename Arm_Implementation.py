class RobotArm:
    def __init__(self, world):
        self.world = world
        self.holding = None

    def hover(self, block_name):
        print(f"Hovering over {block_name}")

    def grab(self, block_name):
        block = self.world.blocks[block_name]
        if block.on_top_of:
            block.on_top_of = None
            print(f"Grabbed {block_name}")
            self.holding = block
        else:
            print(f"{block_name} is already on the ground")

    def release(self, target_name):
        if self.holding:
            target = self.world.blocks[target_name]
            if target.size >= self.holding.size:
                self.holding.on_top_of = target
                print(f"Released {self.holding.name} on {target_name}")
                self.holding = None
            else:
                print(f"Cannot place {self.holding.name} on {target_name} due to size constraints")
        else:
            print("No block in hand to release")


# Initialize the environment and the robot
world = BlocksWorld()
world.add_block("BlockA", size=3, color="Red")
world.add_block("BlockB", size=5, color="Blue")
world.add_block("BlockC", size=7, color="Green")
arm = RobotArm(world)

# Display initial state
print("Initial State:")
world.display_world()

# Move BlockA onto BlockB
print("\nPerforming Operations:")
arm.hover("BlockA")
arm.grab("BlockA")
arm.hover("BlockB")
arm.release("BlockB")

# Display final state
print("\nFinal State:")
world.display_world()




'''
#BlockA is on ground
BlockB is on ground
BlockC is on ground

Hovering over BlockA
Grabbed BlockA
Hovering over BlockB
Released BlockA on BlockB

BlockA is on BlockB
BlockB is on ground
BlockC is on ground
'''
