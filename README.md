# Battleship OMEGA
  

**Welcome to [Battleship OMEGA](https://battleshipomega.herokuapp.com/)!**
  

Battleship OMEGA is a single player game against the AI. This python terminal small game gives you 5 minutes of fun for people who like guessing and luck. Try to find your opponent's ships before it finds yours. The game is simple and enjoyable. Good luck!

![responsive_pic](/assets/images/battleship_omega.png)

## Features

I explain the website features below.

### **Existing features**
  

- **Tutorial**
  - The tutorial understands the game well for the users.
  - If the users knows the rules, they can skip this part by answering no.
  - Any other response will ask the question again.

  ![tutorial](/assets/images/tutorial_battleship.png)
 

- **4 choices**
  - You can choose four different answers, and the active answer works the same as the main menu buttons.

![choices](assets/images/choices.png)

  - If you choose the good answer, the background of the answer will be green.
  
![correctanswer](assets/images/correctanswer.png)

  - But if you choose the wrong answer, it will be red.

![wronganswer](assets/images/wronganswer.png)

- **Score**
  - The user receives 100 points for each correct answer. Wrong answers don't give you points, and you can't get more than 1000 points.

![score](assets/images/score.png)

- **Game Over page**
  - At the end of the quiz, the users can save their high score and enter their name, play again, or go back to the main menu. The form is easy to use and the placeholder helps the users.  

![gameover](assets/images/gameover.png)

- **Leaderboard**
  - This part shows the saved usernames with their scores. The lowest points are at the bottom of the page, and the highest points are at the top.

![leaderboard2](assets/images/leaderboard.png)

### **Features left to implement**
- I think a timer or a countdown would be a good idea to add to this quiz
- I want to add a progress bar next to the score

## Testing

  - The game works as intended. 
  - The scoring system is okay, it gives you 100 points for each correct answer. 
  - I tested each button and answers.
  - You have to fill out the username if you want to save your result. 
  - Responsiveness is good enough for every platform. 

#### **Validator Testing**

- **HTML**
  - First time running the html validator I got 1 error, 1 info and 1 warning message: 

  ![imagespace](assets/images/htmlimagespace.png)
  - I renamed the image that fixed the issue.
  ![inputslash](assets/images/htmlinputslash.png)
  - deleted the slash end of the input
  ![htmlsection](assets/images/htmlsection.png)
  - and deleted the section, because it was unnecessary.

  - After these mistakes were fixed, no errors were returned when passing through the official [W3c validator](https://validator.w3.org/)

- **PYTHON**
  - I tested my codes continuously with the JS validator during my work. I made many mistakes. For example, I often used the wrong keyword when I defined variables(let and const).
  - I forgot to call the function
  - missing or unnecessary semicolons
  - The quiz has 10 questions, but after a couple of questions the game froze. 
  ```
  questionInde
  ```
  - After i 

  ```
  question
  ```


![jsvalidator](assets/images/jsvalidator.png)
  - After these mistakes were fixed, no errors were returned when passing through the official [JS validator](https://jshint.com/)

## Bugs

- If the users 
- Unfortunately, I 

## Deployment  

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  1. In the GitHub repository, navigate to the Settings tab.
  2. From the source section drop-down menu, select the Master Branch.
  3. Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
  4. The live link can be found here: https://luinen.github.io/Halloweenquiz/

- If you want to clone the repository:
  1. In the GitHub repository, click on the 'Code'.
  2. Click 'Open with GitHub Desktop' to clone and open the repository with GitHub Desktop.
  3. Click 'Choose...' and, using the Finder window, navigate to a local path where you want to clone the repository. 
  4. Click Clone.  


## Credits

#### Content

- The questions for the ... were taken from [P]().
- Instructions of the ... were taken from  [W]()
- The idea of the rules ...was taken from [C]()
