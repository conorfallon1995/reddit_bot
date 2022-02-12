# Clean Code Development 


### 10 points - First 5 points contain examples of where I employed the relevant type of CCD

### Checklist

1. I tried to not commit the cardinal sin of using any magic number numbers.
    * For example, at the top of reddit_bot.py, the variable sleepTime = 10 was set up to avoid the use of a magic number later in the program, which - I am ashamed to say - I had initially left in before correcting the mistake.
2. The use of abstract classes is important in clean code development; not only just to have them, but also that the correct degree of abstraction is obtained in the project.
    * Vessel.java in the DSL folder is a good example of this. It allows one to make instances of a particular vessel, such as the boat I created, but also contains further scope for expansion. For example, by using the extends keyword in Java, I could create a class 'Submarine' which bore the elements of its parent class, as well as have its own additional characteristics.
3. The use of the following functional programming techniques are considered a part of CCD. The following have been deployed in my project, as outlined later in point 11 of README.md:
    * Functions as parameters and return values
    * No (or at least minimal) side effects
    * Higher Order functions
    * Anonymous functions
4. It is an aspect of CCD to keep comments to a minimum and write code that is itself self-explanatory to both yourself and other people.
    * I hope that my comments were limited to just the situation where I am explaining things in the context of the assignment, and that the code is self-explanatory.
5. Variables ought to be well-named, making their meaning and use clear
    * I hope that my variables were well-named; for example, in reddit_bot.py I would hope that it is clear what the following variables would mean, especially in the surrounding context:
    *       sql_string = ...
            json_string = ...
            url_string = ...

6. Only use positive conditionals (not negative conditionals), as these are more intuitive to a human reader, although equivalent for a computer. For example, "if a > b ..." is a lot clearer than "if a !<= b...", even though they both mean the same thing.
7. Your code should always be ready for when something goes wrong! Make use of try/catch/except type statements in order to manage such potential errors. These can be good for both the people designing the code, but also to allow a user to better understand what has gone wrong if something has indeed gone wrong.
8. Make good use of testing. Having a high level of test coverage and, if possible, automated unit tests is desirable.
9. Try not to repeat code = inefficient! Where possible, it is better to keep the code simple rather than make it more complicated, particularly as the code will be read much more often than it is written.
10. In a project, making use of continuous implementation, good build management, continuous delivery, and utilising suitable metrics are elements of CCD.
