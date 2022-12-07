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
 

- **Grid**
  - The users can decide the board size. There are 2 options. 5x5 or 10x10.

![board](/assets/images/grid_battleship.png)

- **Placing the ships**
  - After the grid selection, the users can decide where they want to place their ships.
  - The users don't see the the computer choices.
  - The AI randomly generates ships on the board.

- **Target system**
  - Everything is ready to play. The users start and then select the first target and after that the AI does the same.

![target_system](/assets/images/target_battleship.png)

- **End game**
  - The game ends if the user or the computer lose all of their ships.

![game_over](/assets/images/game_over_battleship.png)

### **Features left to implement**
- 2nd board for a longer gameplay
- Multiplayer mode

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
- Solved Bugs
  - The AI choose the same location and started the game with only 3 or 4 ships.
- Unsolved Bugs
  - If the users enter nothing when they want to shoot, an error message pop up. 

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
