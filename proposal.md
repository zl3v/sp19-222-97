  *<h1>Project Proposal: Tetris Score Analyzer</h1>*
  <br></br>
  For my project, I wish to make a small Raspberry Pi connected with an Adafruit PiTFT that, whenever a user completes a game, it will upload the data onto the REST server and calculate statistics. Over the course of several instances, it will use data aggregation and linear regression models in order to determine correlations between user play time, score, and difficulty levels.
  <br></br>
	The game that I wish to use is spin-off of the revolutionary video game Tetris. Created over thirty-five years ago in 1984, Tetris is a puzzle game in which players move four-block combinations of squares, called tetrominoes, into fit arrangements. When a full row of squares is filled, the row is deleted and the score increases. Tetrominoes are randomized and fall downwards automatically, but are allowed by the player to rotate it to better fit. The game is over when the user stacks too many tetrominoes to reach the top of the screen.
    <br></br>
	My hope with this project is to have the usage of a spin-off of Tetris developed by Michael Billington called Blocks. Blocks is a Tetris-style game that was developed in C++ for usage with a Raspberry Pi and a graphical user interface shield. My hope is that, by reverse engineering some of the code to store the user’s score, to not only store the data on a REST server, but also use accumulated data across multiple entries - and perhaps users - in order to create a linear regression model to predict how much and at what rate a person will increase their score over time.
    <br></br>
	It is perhaps expectant that as the player plays the game more, they are to improve. What I seek is to map out using linear regression modelling is to pinpoint the correlations between score improvement and play time. Is it a exactly linear? What is the general relation between them? Can we predict how much time a person has to spend on the game to improve using computer simulations? 
    <br></br>
	Several things need to be considered in the collection of data for the game. Most important perhaps is score and game time. Further experimentation within the C++ code of Blocks could pave the way for multiple users to log  and upload their statistics, individualizing models for each person. It would be very interesting to possibly map out predictable rates at which people improve in skill for the game and how long they have to play to get their score. There are many factors as to how a person will perform, a huge amount of it being environmental. The main correlation which I wish to experiment with is simply time and score.
    <br></br>
    **References and Links**
    <ul>
	<li> https://mike42.me/blog/2015-03-how-to-run-tetris-on-your-raspberry-pi </li>
	<li> https://github.com/mike42/blocks </li>
	<li> https://www.adafruit.com/product/1601 </li>
    </ul>
