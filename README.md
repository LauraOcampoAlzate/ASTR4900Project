# ASTR4900Project

Laura Ocampo & Wynter Broussard
Interactive Orbit Simulator README
ASTR 4900
December 9th 2020

The code is written in Python using Anaconda version 3.3.6. OrbitSimulation.py. The libraries used in the code, NumPy and Matplotlib, are automatically included with Anaconda, and will not need to be downloaded separately. We used ffmpeg to make our animation which is already installed on Macs but may need to be installed on a Windows machine. More instructions are available online for any troubleshooting with ffmpeg.

To test the code for correctness, we tested eccentricities of 0, 0.049, 0.5, and 0.99. These specific numbers were tested because eccentricities are between 0 and 1 and Jupiter's natural eccentricity is 0.049. However, 0.049 is still close to 0 and hard to see the difference between a perfect circle and an almost perfect circle. Therefore, 0.5 was chosen since it is halfway between 0 and 1 and would be a perfect oval. The test results showed exactly what we were expecting.

The first step when opening the code is to determine how many steps you’d like. The steps determine how many data points there are as well as how many .png files are saved for an animation. For our tests N = 500 was used.

The results that are generated are a figure of the final orbits and N number of .png files saved to the directory path as where the code is located. These .png files are automatically named in the code to make the animation step easier.

The last step for the animation is to go into Terminal (for a Mac) and use ffmpeg to make a movie. The command used is 

ffmpeg -r 100 -f image2 -s 1920x1080 -i frame%03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p Test.mp4

where the important parts are -r and Test.mp4. The -r determines the frames per second (which is set to 100 but can be changed) and “Test” is just a dummy name for what you want the movie file to be called. 
Here is a more detailed description of ffmpeg:http://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/ .
The movie file is then saved in the same directory as the files and code. The .png files are safe to trash after the movie is made.

