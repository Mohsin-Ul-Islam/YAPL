# Yet Another Programming Language

This simple programming language is part of a Computer Science course **Theory of Automata** at **Lahore University of Management Sciences**. Following is the comprehensive documentation of the programming language and its features.


## Data Types

**YAPL** has three atomic data types yet. These data types include

 - **Integers**
 - **Floating point numbers**
 - **Strings**

## Expressions

**YAPL** can evaluate simple mathematical expressions. These include simple **addition**, **subtraction**, **division**, **multiplication** and **modulus** operations. If you want to write multiple expressions on the same line, they end with a semicolon otherwise single expression can be written per line.

### Addition
In **YAPL** expressions can be added using '**+**' operator.

    YAPL >>> 1 + 2
    3
### Subtraction

Subtraction can be done using '**-**' operator.

    YAPL >>> 1 - 2
    -1

### Division

Division can be performed using the '**/**' operator.

    YAPL >>> 10 / 2
    5
  If division contains at least one floating point value, then the resulting value will be floating point value.


    YAPL >>> 1 / 2.0
    0.5

### Multiplication

Multiplication between two expressions can be performed using the '**\***' operator.

    YAPL >>> 12 * 2
    24

### Modulus
The remainder of integer division can be obtained using '**%**' operator.

    YAPL >>> 7 % 3
    1

### Precedence Shifting

 Multiplication, Division and Modulus operators have highest precedence in an expression by default.


    YAPL >>> 1 + 2 * 3
    7
   However, the precedence of expressions can be changed by using **paranthesis**.


    YAPL >>> (1 + 2) * 3
    9


## Variables

All programming languages need some kind of data storage mechanism to efficiently perform memory extensive tasks. **YAPL** can provide such functionality by storing fundamental data types in variables. A variable in **YAPL** can store any one of integers, floating point values and strings at a time.

### Naming Convention

In **YAPL** variables can be represented by names. Variable names always need to obey the following rules.

 - Variable names cannot start with a number, special or non alphabetic character.
 - Variable names must start with either an underscore or letters.
 - Variable names can have more than one underscores or letters.
 - Variable names cannot have spaces.

### Variable Declaration

Variables in **YAPL** can be defined in two fundamental ways. The first method is type loose, which means that the data type for the variable is not fixed.

    let number = 10

Here '**let**' is a special keyword which defines a new variable called **number**. The **number** variable can now store any kind of value beyond this point. The **let** keyword declares a loosley type variable which can store any type of data during the course of execution and its scope. For example, after integer value of 10, the **number** can store a string value as well.

    number = "hello world"

A variable can be declared without using the '**let**' keyword but we have to specify a type specifier this time. This method will bound the variable to a specific data type and the variable can store only that kind of data over the course of execution and its scope.

    int books = 10

The fundamental data types in **YAPL** are *int, float, string, and char.*

    string message = "I love programming"

### Variable Assignment

A variable can be assigned different values based on the type of the variable (either loose or fixed to a certian data type) many times as long as it is live in its scope.

    int books = 0
    books = 10

   This statement puts a value of **10** in variable **books** which was already declared. Trying to put a data in variable which does not match its data type will create an error.


    int price = 100
    price = "ten" // this is an error

  However, a loosley typed variable can store any kind of data.
  A more descriptive way of assigning a value to a variable in **YAPL** can be


    put 100 in price

As such, any valid data can be inserted in a variable.

    put (price - 50) in books // books now contain 50

## Loops
Any good programming language gives the functionality of loops and so is **YAPL**. In **YAPL** we have three different kinds of loops each with several syntax types.

 - For loop
 - While loop
 - Do While loop

### For Loop
In **YAPL** a for loop loops a certain (fixed) amount of time over a block of code. The syntax for it looks like

    for (let counter = 0; counter < 10; counter++) { }

Here, the keyword **for** initializes the loop where the header cotains loop counter initiation, conditional checking at each iteration and increment of the counter. The body of loop that gets executed many times goes in braces. The paranthesis after **for** are optional. The above for loop can also be written like this

    for let counter = 0; counter < 10; counter++; { }

But watch for the additional **;** after increment statement. The counter can be incremented or decremented in any way.

    for let counter = 0; counter < 10; counter += 2; { }

Another way to write a for loop in **YAPL** can be

    for (1 to 10) { }
Again the paranthesis are optional. This kind of loop can take step as an additional argument.

    for 1 to 10 step 2 { }
Loops can also go from high value to low value

    for 10 to 1 step -2 { }
Here the numbers can take place of any valid variables

    let counter = 0;
    for counter to counter + 100 step 1 { }
### While Loop
While loops in **YAPL** are very simple. They contain a keyword **while** followed by some condition and then a body of loop.

    while (counter < 5) { }
  Again the paranthesis in conditional statement are optional.
### Do While Loop
Do while loop differ from while loops in a sense that they run at least one time. The **YAPL** syntax for do while loops look like

    do { } while (counter < 5);

  Here the paranthesis and semicolon are both optional.

## Conditional Statements
In **YAPL** there is a support for conditional statements. The type of conditional statements supported by **YAPL** are

 - If statements
 - If Else statements
 - If Else If statements
