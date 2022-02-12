# Advanced Software Engineering
#  reddit bot

## Table of contents
* [General info](#general-info)
* [Checklist](#checklist)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a simple reddit bot that, upon using a specific keyword, will provide the user with information on a given movie retrieved from Wikipedia and recommend them further movies based on the most highly regarded work done by the director in question, based on the director's IMDB rankings.

To trigger this bot, simply comment the string "!film" followed by the name of the film you wish to know more about. For example, commenting:
   
&nbsp;&nbsp;&nbsp;&nbsp; !film goodfellas

will provide the user with a range of information and movie recommendations about Martin Scorsese's 1990 film _Goodfellas_.

Examples of the bots outputs (both successes and failures) can be seen at this test site I have been using, if you do not have time to run it yourself:

The main code for the bot can be find in reddit_bot.py and querier.py.

&nbsp;&nbsp;&nbsp;&nbsp; https://old.reddit.com/r/test/comments/ql1xai/testst/?sort=new 

## Checklist

1. This was my first experience with a software engineering module, and hence in using git. I found git and github to be a useful tool. I set up my own repository, made use of 'git clone' to get said repository onto my computer. I initially used commands like commit or push, but found it easier to just used the built-in integration which PyCharm has for git to manage my project. I also learned about branching and things like version control, although I admittedly just used a single master branch for this relatively simple project. I also learned how to integrate my github repository to Jenkins.
2. The three UML diagrams can be found in the ['UML_diagrams'](https://github.com/conorfallon1995/reddit_bot/tree/master/UML_diagrams) directory. A flow chart, a deployment diagram, and a class diagram are contained therein, respectively.
3. The diagram of my Domain Driven Design of the imagined future business 'MovieRecommenderGmbH' can be found in the file 'DDD.png'.
4. I tried to install Sonarqube on my Mac, but failed after trying a couple of times. Then I searched for an alternative to Sonarqube and found MetricsReloaded, which is a plugin for my preferred IDE, PyCharm. Admittedly it is not the most impressive tool in the world. Still, I got two metrics out of it.
   * Screenshots of the metrics produced by this plugin can be seen in ProjectMetrics.png and FileTypeMetrics.png . I will also compute two more metrics by-hand given the limited features of the plugin:
   * In the main project files, querier.py and reddit_bot.py, there are three methods, two of which are abstract (string_query() and run_bot()), which gives them together an 'abstractness' metric of 2/(1+2) = 0.67
   * I also tried to calculate my Average Component Density (ACD) for the above programs. I counted 8 components in my project, of which 4 were dependencies. This gives an ACD of 50%. By extension, the rACD could be calculated as 50%/8 = 6.25%
5. Please see CCC_CheatSheet.md for a full explanation
6. I used PyBuilder for Build Management, as it integrates nicely with my preferred IDE of PyCharm. According to PyBuilder themselves, they have borrowed many of their conventions from Apache Maven. However, I found it tricky to integrate with my project, because I had completed the coding part of my project first and then tried to tack on the build system after the fact. Successful console deployment of the tool can be viewed in the file 'BuildSumary.png"
   * However, I did use it to produce some documentation and run a basic unit test to show that I had used this as an opportunity to learn a build tool, creating some basic documentation and tests for a helloworld.py program (exists in venv/src/main/python). The output documentation of test unit coverage can be viewed in the file /venv/target/reports/helloworld_coverage.xml. A range of other documentation was produced which can be viewed, if desired, by going into the venv/target folder. The file TargetDirectoryTree.png also shows all of the directories that PyBuilder creates for when one wants to correctly “build” a python project.
7. I deployed unit-tests with the Python "unittest" Unit testing framework. These tests are available in the following files:
   * test_reddit_bot.py: Here, my first test simply checked that the project itself was well set up. i.e. does the config.py actually lead to the correct login credentials being passed into reddit’s API.
   * test_querier.py: Here, the second two tests check that a secure SQLite connection has been made with the movies.db database, by checking that Cursor objects and Connection objects had successfully been established.
   * It was also mentioned that we should integrate unit-tests in our build management tool. Therefore, I also tried to learn how to make a Unit-Test with my chosen build management system, PyBuilder. Here I ran a rudimentary test under this system in venv/src/unittest/python/helloworld_tests.py
8. I got Jenkins running using the relevant password running on localhost 80.80. (I used the brew install method outlined on the jenkins website). 
I created the file ‘reddit-bot-jenkins-pipeline’ on my local host which is available on this repository, and made use of ‘pipeline Syntax’ in order to connect the pipeline to my git repository. This produced a pipeline script which allowed me to integrate the two. Pipeline has three stages: Checkout, build, and a test stage. The image "jenkins_localhost_setup.png" has also been included to demonstrate that I did indeed have Jenkins installed and working on my computer.

9. The IDE I use, as already mentioned, was PyCharm, developed by JetBrains. I like it first of all as it already takes care of my virtual environment in the 'venv' folder, allowing me not to worry about things like dependencies (or at least not worry too much!). A screenshot of my workflow is shown in "IDE.png". The following keyboard shortcuts were used:
    * Cmd z and Cmd Shift z for undo and redo were a great help to me...
    * As were Cmd c and Cmd v for copy and paste related reasons
    * I also forced myself to learn the git commands for Push and Commit which were Cmd K and Cmd Shift K respectively.
10. My DSL demo is available in the directory "DSL" which contains the following files: ‘Vessel.java’ and ‘runVesselDSL.java’, which define a vessel in my own "boat-related domain specific language", and then implement a given vessel. In Vessel.java, a vessel is defined as a class which possesses a name, a year of creation, a length, and a make, as we would expect of a vessel in real life. By running ‘java runVesselDSL’, the following is outputted:
    * Name of vessel is The Flying Sheep.
    * The vessel has a length of 182.0 metres.
    * Its make is Harland & Wolff and its year of manufacture was 1642.

I hope this covers the basics, perhaps in a silly way, of domain specific language. The (already compiled) code can be tested by executing the command "java runVesselDSL" in the relevant directory.

11. I tried to ensure I covered the required aspects of functional programming by adapting my DSL demo as required. The following points are met:
    * In my main project I tried not to change the variables where possible once they had been declared. To illustrate an understanding of finals, I employed ‘final String name;' in runVesselDSL.java. In the file Vessel.java, there is also extensive use of getters and setters, and private variables are also used.
    * The functions I have used provide no unwanted side effects (as far as I have tested!), and in cases where something may arise, I have tried to account for this fact. To give an example, in the run_bot() method in reddit_bot.py, I use a try/except which raises a key error if there is no Wikipedia data for the movie they have searched for, and this information is relayed to the reddit user, mitigating any potential side-effects should they occur.
    * An example of the use of higher order functions occurs at the end of the reddit_bot.py file. Here, I pass the parameter bot_login() as an argument to the method run_bot(). As bot_login returns an object which is essentially a PRAW object which allows us to interact with the reddit API, this amounts to a functional programming style of deploying the run_bot() method.
    * I used an anonymous lambda function in the demo file functionalExample.py. This also features the use of functions as a return and as a parameter.


## Technologies
Project is created with:
* Python version: 3.9
* PRAW: The Python Reddit API Wrapper
* JSON
* SQLite version: 3.36.0
* Java version 11.0.1
	
## Setup
To run this project, simply run the following from the repository's base directory:

```
$ python reddit_bot
```
This will start the bot, and commenting "!film [INSERT FILM NAME HERE]" anywhere on the r/test subreddit will produce the behaviour outlined above. 