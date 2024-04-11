import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 800, 600
# below we intizlae all our variables
rocket_x = 0
rocket_y = 570
#below is the angle of launcg this decides how its highest point will be 
launch_angle_deg = random.randint(-40, -25)
print(launch_angle_deg)
# velocity willd ecide how fast it will go and how far it will go
# *** remeber velocity is how fast it will go initally upward ***
velocity = 1.6
# below we calculate radians, the reason for this is sumn to do with it being better for ciricles and physics shi idrk
# below we can make the ball reach a  higher vertex by subtracting sumn for ex: adding -0.2 to the end 
launch_angle_rad = math.radians(launch_angle_deg) 
# below is intial velocity it takes yr speed times the sin of yr angle radian
# below we can make the ball go a further distnace by subtracting sumn for ex: adding -0.2 to the end 
intial_velocity = velocity * math.sin(launch_angle_rad)
gravity = 9.81
#below is gravity and time
time_elapsed = 0
# image to the circle
image_path = "rocket n stuff/download-removebg-preview.png"
freindly_path = "rocket n stuff\\freindly rocket launcher.png"
freindly_x = 670
freindly_y = 500
freindly_rocket_x = 670
freindly_rocket_y = 500
load_image = pygame.image.load(image_path)
load_image2 = pygame.image.load(freindly_path)
rocketx_velcoity = rocket_x + random.uniform(0.001, 0.024)
rocketyVelocity = rocket_y + ( intial_velocity * time_elapsed + 0.5 * gravity *time_elapsed **2)


# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")
image = pygame.transform.scale(load_image, (30,30))
image2 = pygame.transform.scale(load_image2, (140,140))
image3 = pygame.transform.scale(load_image, (30,30))
transparent = (255,255,255)
Launched = 1 
resting = 0
state = Launched

# Main game loop
while True:
    window.fill((255, 255, 255))  # Fill with white color
    # displaying yellow circle roket below
   
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # below the rocket trajectory stuff
    future_x_position = rocket_x + rocketx_velcoity * time_elapsed
    future_y_position =  rocket_y + ( intial_velocity * time_elapsed + 0.5 * gravity *time_elapsed **2)
    dist_y = freindly_rocket_y - rocket_y
    dist_x = freindly_rocket_x - rocket_x

    if state == Launched:

        # define what launched mean, (ball is moving)
        rocket_y += ( intial_velocity * time_elapsed + 0.5 * gravity *time_elapsed **2)
        rocket_x += rocketx_velcoity
    # below we define what happens when ball touches ground
    if rocket_y > HEIGHT:
         rocket_x = 0
         rocket_y = 550
        # reset state to resting
         state = resting
    # below we deifne resting To a a state of moving x and moving y than when it touches ground the loop resets
    elif state == resting:
        rocketx_velcoity = rocket_x + random.uniform(0.01, 0.024)

        rocket_x += rocketx_velcoity
        launch_angle_deg = random.randint(-40, -25)
        launch_angle_rad = math.radians(launch_angle_deg) 

        time_elapsed = 0
        intial_velocity = velocity * math.sin(launch_angle_rad)

        state = Launched
    if state == Launched and time_elapsed > 0.15271000000004195 :
        freindly_rocket_x -= dist_x * 0.001
        freindly_rocket_y -= dist_y * 0.001

        window.blit(image3, (freindly_rocket_x, freindly_rocket_y))

    if dist_x < -3 :
        rocket_x = 0
        rocket_y = 550
        freindly_rocket_x = 670
        freindly_rocket_y = 500
        state = Launched
        
        time_elapsed = 0

    #print(time_elapsed)

        


        



       

    # Update the display
    window.blit(image, (rocket_x,rocket_y))
    window.blit(image2, (freindly_x, freindly_y))


    pygame.display.update()
    # below we decide how fast or slow we want the ball to mvoe the higehr the number the faster
    time_elapsed += 0.00001