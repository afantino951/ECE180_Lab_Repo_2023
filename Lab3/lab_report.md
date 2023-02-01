# Lab 3 GUI Tutorial

## Task 1

Before fully implementing the multiplayer rock paper scissors game, we made a simple single player version with an 'AI' that picks a random move. The output from that game is below.

|![Simple AI RPS](lab_report_files\simple_ai_rps.jpg)|
|:--:|
|*CLI output of rock, paper, scissors vs. simple AI*|

We then used the game logic from that code to make a multiplayer version using MQTT. Our game used a client server model where the publisher was acting as a central server and multiple subscribers were acting as the clients. The subscribers would connect to the same topic as the publisher and listen for the commands from the publisher.

Below are the images from the output of the CLI publisher and the CLI subscriber respectively.

|![rps publisher](lab_report_files\rps_publisher.jpg)|
|:--:|
|*CLI Output of rock, paper, scissors publisher script*|

|![rps subscriber](lab_report_files\rps_subscriber.png)|
|:--:|
|*CLI Output of rock, paper, scissors subscriber script*|


## Task 2

I looked through the listed GUI tools in the tutorial, but I did not find an alternative that would fit our project as well as Pygame except for Unity. However, Unity is a much more complex and, since I am not responsible for the GUI portion of the project, I will leave the decision to my teammate.

I personally would choose to not use Unity since I feel that we should be able to do all portions of the game with pygame at a slightly lower visual quality. I doubt that it would affect the playability of the final product game.

## Task 3

Here is where we implement our GUI implementation of rock paper scissors and add our multiplayer implementation on top of it.

|![rps AI](lab_report_files\rps_pygame_ai.jpg)|
|:--:|
|*GUI Output of rock, paper, scissors single player*|

I had trouble with the implementation of the gui myself, so I used my teammate's implementation. Since I am not responsible to the game implementation, I did not have any issues adapting my teammate's code.

|![rps Multiplayer](lab_report_files\rps_pygame_multiplayer.jpg)|
|:--:|
|*GUI Output of rock, paper, scissors multiplayer*|

## Task 4

Code was submitted to github [here](https://github.com/afantino951/ECE180_Lab_Repo_2023)