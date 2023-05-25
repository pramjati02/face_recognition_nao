import time
from qibullet import SimulationManager
from qibullet import NaoVirtual
from qibullet import NaoFsr
from gtts import gTTS
import os

def wave_right_hand():
    # Initialize the simulation manager
    #simulation_manager = SimulationManager()
    #simulation_manager.launchSimulation(gui=True)

    # Load the NAO robot in the simulation
    #nao = simulation_manager.spawnNao(
    #    humanoid_robot=True,
    #    spawn_ground_plane=True
    #)

    # Enable the right arm control
    nao.setAngles("RShoulderPitch", -1.5, 0.05)
    nao.setAngles("RShoulderRoll", 0.5, 0.05)
    nao.setAngles("RElbowYaw", 0.2, 0.05)
    nao.setAngles("RElbowRoll", 1.0, 0.05)

    # Perform the waving motion
    nao.setAngles("RElbowRoll", -1.5, 0.2)
    time.sleep(1.0)
    nao.setAngles("RElbowRoll", 1.0, 0.2)
    time.sleep(1.0)
    nao.setAngles("RElbowRoll", -1.5, 0.2)
    time.sleep(1.0)
    nao.setAngles("RElbowRoll", 1.0, 0.2)

    # Close the simulation
    #simulation_manager.stopSimulation()

if __name__ == "__main__":
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    nao = simulation_manager.spawnNao(client, spawn_ground_plane=True)

    # Alternative solution, get the FsrHandler of the robot:
    # fsr_handler = nao.getFsrHandler
    

    try:
        while True:
            # Get the FSR value of the front left FSR of NAO's left foot
            value = nao.getFsrValue(NaoFsr.LFOOT_FL)
            # Get the FSR value of the rear right FSR of NAO's right foot
            value = nao.getFsrValue(NaoFsr.RFOOT_RR)

            # Get all of the values of the FSRs of NAO's left foot
            values = nao.getFsrValues(NaoFsr.LFOOT)

            # Get the total weight value on the FSRs of NAO's right foot
            total_weight = nao.getTotalFsrValues(NaoFsr.RFOOT)
            print("Total weight on the right foot: " + str(total_weight))

            # Alternative solution:
            # fsr_handler.getValue(NaoFsr.LFOOT_FL)
            # fsr_handler.getValue(NaoFsr.RFOOT_RR)
            # fsr_handler.getValues(NaoFsr.LFOOT)
            # fsr_handler.getTotalValue(NaoFsr.RFOOT)
            
            with open("output.txt", "r") as file:
            	value = int(file.readline().strip())  # Read the value from the text file and convert it to an integer

            if value == 0:  # Adjust the condition based on your requirements
# Play the audio file
		os.system("mpg321 0_people.mp3")  # On Linux
	    elif value == 1:  # Adjust the condition based on your requirements
            	wave_right_hand()
# Play the audio file
		os.system("mpg321 One_person.mp3")  # On Linux
	    elif value == 2:  # Adjust the condition based on your requirements
            	wave_right_hand()            	
# Play the audio file
		os.system("mpg321 pair_people.mp3")  # On Linux
	    elif value>=3 and value<6:  # Adjust the condition based on your requirements
            	wave_right_hand()
# Play the audio file
		os.system("mpg321 small_group.mp3")  # On Linux
	    elif value > 6:
	    	wave_right_hand()
# Play the audio file
		os.system("mpg321 large_group.mp3")  # On Linux


            		
            

    except KeyboardInterrupt:
        pass
    finally:
        simulation_manager.stopSimulation(client)
