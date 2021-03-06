> בס״ד

# C Programming Examples

### Content
- [Variables](#variables)
  - [Assign Values to Variables](#assign-values-to-variables)
  - [Declare and Assign Value together](#declare-and-assign-value-together)
  - [Print Variables](#print-variables)
  - [Print double Variables](#print-double-variables)
  - [Character Variables](#character-variables)
  - [Assign Value to double and char Variables](#assign-value-to-double-and-char-variables)
  - [Change Variable Values](#change-variable-values)
  - [Value of One Variable to Another](#value-of-one-variable-to-another)
  - [Create Multiple Variables Together](#create-multiple-variables-together)

- [Problem Description](#problem-description)
  - [Create a program to print the variable.](#create-a-program-to-print-the-variable)
  - [Create a program to change the value of a variable.]()


---
# Variables

# Assign Values to Variables
- Once we declare a variable, we can assign a value to it. 
> Let's see how to do that.
```c
// declare the variable
int age;

// assign the data 25 to it
age = 25;
```

- Here, we have used the `=` operator to assign the value `25` to the `age` variable.

---

# Declare and Assign Value together
- We can also assign values to variables during their declaration. 
> Let's see how:
```c
int age = 25;
```

- Here, we have created a variable and assigned a value to it in a single statement.

---

# Print Variables
- We use the `printf()` function to print variables in C programming.
> For now, let's just see an example to print variables.
```c
#include <stdio.h>
 
int main() {
 
  // create a variable
  int age = 25;
 
  // print the variable
  printf("%d", age);
  
  return 0;
}
```

- The `printf()` function prints anything present inside the quotation marks. 
- However, instead of `%d`, we are getting `25` (value of the age variable).
- This is because, in C, we use format specifiers to print variables. 
- Here, `%d` is a format specifier which is replaced by the value of the age variable (`25`).

![image](https://user-images.githubusercontent.com/51442719/179797020-57d3d026-8cff-4e74-a976-8febf72b8ea0.png)

> 💡 Note: The `%d` format specifier can only be used to print int variables. <br> To print double variables, we use `%lf`, which we will see next.



---

# Print double Variables
- Now that we know how to print variables, let's use the same concept to print a `double` variable.
```c
#include <stdio.h>
 
int main() {
 
  // create double type variable
  double number= 36.43;
 
  // print the variable
  printf("%lf ", number);
  
  return 0;
}
 
// Output: 36.430000
```

- Here, we have used `%lf` to print number (a `double` variable).


---

# Character Variables
- A character variable can only store a single character data. 
- We use the `char` keyword to create char type variables. 
> For example:
```c 
char alphabet = 's';
```
- Here, `alphabet` is a character variable with data `'s'`. In C programming, we use single quotes to denote characters.
- Similar to `int` and `double` variables, we can also print character variables using the `printf()` function. 
> Let's see an example:
```c
#include <stdio.h>
 
int main() {
 
  // create a char variable
  char alphabet = 's';
 
 // to print char variable, we use %c
  printf("%c", alphabet);
 
  return 0;
}
 
// Output: s
```
- Notice that we have used the `%c` format specifier to print character variables.

---

# Assign Value to double and char Variables
- Problem Description
  - Create a program to assign values to double and char variables.
    - Create a `double` variable named `number` with value `86.99`.
    - Create a `character` variable named `letter` with value `'z'`.
    - Print both variables `with two spaces` between them.
```c
#include <stdio.h>
 
int main() {
 
  // create double type variable
  double number = 86.99;
 
  // create a char variable
  char letter = 'z';

  // print the variable
  printf("%lf ", number);

  // to print char variable, we use %c
  printf(" %c", letter);

  return 0;
}
  
 ```

---

# Change Variable Values
- As suggested by the name variable, we can change the value stored in a variable. 
> Let's see an example:
```c
#include <stdio.h>
 
int main() {
 
  // create a variable 
  int age = 25;
  printf("%d ", age);
 
  // assign new value to age
  age = 31;
  printf("%d", age);
 
  return 0;
}
```
- Here,
  - The initial value of age is `25`. 
  - So, we get `25` as output.
  - The line `age = 31;` changed the value to `31`. 
  - So, we get `31` when we print age again.
> 💡 Note: When we change the value of a variable, the type of value and variable must match. <br>
> For example, `age` is an `int` variable, so we cannot store decimal numbers to it.

---

# Value of One Variable to Another
- It's also possible to assign the value of one variable to another. 
> Let's take an example:
```c
#include <stdio.h>
 
int main() {
 
  int number1 = 33;
  printf("%d", number1);
 
  int number2 = 87;
 
  // assign value stored in number2 to number1
  number1 = number2;
  printf("  %d", number1);
 
  return 0;
}
 
// Output: 33  87
```
- Here, we have assigned the value of the `number2` variable to the `number1` variable.
> 💡 Tip: Always read the error message carefully. It may help us fix the error.

---

# Create Multiple Variables Together
- We can also create multiple variables together in a single line. 
> Let's see an example,
```c
#include <stdio.h>
 
int main() {
 
  // create two variables together
  int age = 25, id = 132;
  
  printf("%d ", age);
  printf("%d", id);
  
  return 0;
}
```
- Here, we have created two variables `age` and `id` together in the same line with values `25` and `132` respectively.





---

# Problem Description

### Create a program to print the variable.
- Create two variables `number1` with value `34` and `number2` with value `78.32`.
- Print `number1` and `number2` with a space in between.
```c
#include <stdio.h>

int main() {
  
  int number1 = 34;
  double number2 = 78.32;

  printf("%d", number1);
  printf(" %lf", number2);

  return 0;
}
``` 

### Create a program to change the value of a variable.
- Create an integer variable `number` with value `31`.
- Print the variable.
- Change the value of the variable to `99`.
- Print the variable again with a space before it.

```c
#include <stdio.h>

int main() {
  
    // create and print an integer variable
    int number = 31;
    printf("%d", number);

    // change the value of variable
    number = 99;

    // print the variable
    printf(" %d", number);

    return 0;
}
```

### Assign One Variable to Other
- Create a program to assign the value of one variable to another.
  - Create an integer variable named `distance` with value `135`.
  - Print the `distance` variable.
  - Create another integer variable named `newDistance` with value `429`.
  - Assign the `newDistance` variable to the `distance` variable.
  - Print the `distance` variable again with two spaces before it.
```c
// Replace ___ with your code

#include <stdio.h>

int main() {

    // create and print the distance variable
    int distance = 135;
    printf("%d", distance);
    
    // create the newDistance variable
    int newDistance = 429;

    // assign newDistance to distance and print distance
    distance = newDistance;
    printf("  %d", distance);

    return 0;
}
```

---





- [Learn C Programming](https://app.programiz.pro/course/learn-c-programming)


