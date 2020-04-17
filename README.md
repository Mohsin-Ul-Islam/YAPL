# Yet Another Programming Language

This simple programming language is part of a Computer Science course **Theory of Automata** at **Lahore University of Management Sciences**. Following is the comprehensive documentation of the programming language and its features.


## Data Types

**YAPL** has three atomic data types yet. These data types include

 - **Integers**
 - **Floating point numbers**
 - **Strings**

## Expressions

**YAPL** can evaluate simple mathematical expressions. These include simple **addition**, **subtraction**, **division**, **multiplication** and **modulus** operations. Expressions must always end with a semicolon.

### Addition
In **YAPL** expressions can be added using '**+**' operator.

    YAPL >>> 1 + 2;
    3
### Subtraction

Subtraction can be done using '**-**' operator.

    YAPL >>> 1 - 2;
    -1

### Division

Division can be performed using the '**/**' operator.

    YAPL >>> 10 / 2;
    5
  If division contains at least one floating point value, then the resulting value will be floating point value.


    YAPL >>> 1 / 2.0;
    0.5

### Multiplication

Multiplication between two expressions can be performed using the '**\***' operator.

    YAPL >>> 12 * 2;
    24

### Modulus
The remainder of integer division can be obtained using '**%**' operator.

    YAPL >>> 7 % 3;
    1

### Precedence Shifting

 Multiplication, Division and Modulus operators have highest precedence in an expression by default.


    YAPL >>> 1 + 2 * 3;
    7
   However, the precedence of expressions can be changed by using **paranthesis**.


    YAPL >>> (1 + 2) * 3;
    9


## Variables

All programming languages need some kind of data storage mechanism to efficiently perform memory extensive tasks. **YAPL** can provide such functionality by storing fundamental data types in variables. A variable in **YAPL** can store any one of integers, floating point values and strings at a time.

### Naming Convention

In **YAPL** variables can be represented by names. Variable names always need to obey the following rules.

 - Variable names cannot start with a number, special or non alphabetic character.
 - Variable names must start with either an underscore or letters.
 - Variable names can have more than one underscores or letters.
 - Variable names cannot have spaces.

### Variable Assignment

Variables in **YAPL** can be defined in the following different valid ways.

    let number = 10;

Here '**let**' is a special keyword which defines a new variable called **number**. In **YAPL** variables can store different data types. For example, the variable from above can store a string value in a next statement.


    number = "hello world";
A variable can be declared without using the '**let**' keyword.

    books = 10;
A more descriptive way of declaring a variable in **YAPL** can be:

    put 10 in books;
The data type literals like 10,"hello world" in variable declaration or assigment can be replaced by any valid expression.

    put (number - 2) in books;
    books = number - 2;
 both of these statements are equivalent.
