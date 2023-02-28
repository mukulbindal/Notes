###########Javascript##############

###Fundamentals###

######Values #######
Can be 2 types of values – primitive or Object. Objects – we will see later
Primitives:
1.	Number (all floating points, integers etc)
2.	String
3.	Boolean
4.	undefined
5.	null
6.	Symbol (ES2015) – not used much
7.	BigInt (ES2020)
# typeof operator
# typeof false    # boolean
# typeof "hello"  # string
# typeof operator returns the type in 'string' format hence - 
# typeof typeof 123 === 'string'.

When we declare a variable, the default value is 'undefined'

# typeof null always returns 'object' which is a bug but ot fixed due to legacy reasons.

### Declaring Variables ####

# let and const are introduced from ES5 while var is legacy

Mutation: Mutation is a term used for reassigning values to a variable. Hence if we are 
not allowed to reassignm we call is immutable objects. 

example -
let a = 123;
a = 234;    // Is called mutation or reassignment

let : can be declared and mutated and its scope is block level
const: is immutable and block scoped 
var: must be avoided unless necessary and it allows mutation and supports hoisting.

If we declare any variable without let/const/var, JS will not throw any error 
but it is not a variable in this case. We are simply declaring a property 
on the global object which may result in potential bugs later. So best way is
to use let/const only and mostly const only.

Operators:
We can check the operators and precedence here -
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence

On high level, 
comma has lowest precedence and brackets () have highest
Can refer below order - 
()                                      Brackets 
., ?., new, function call etc, []       member access (res.data) & optional chaining
++ / --                                 Postfix increment 
!, ~, +, -, typeof, await               all unary operators 
**                                      exponentiation (has right to left association)
/,*,%                                   arithmetic
+,-                                     arithmetic
>>, <<, >>>                             bitwise shift 
>, <, >=, <=, in                        logical comparision
==, ===, !==                            Equality
&
^
|
&&
||
All assignment operators 
=, +=, /=,...
?:  (Ternary)
=> (Arrow)
yield
Spread (   ...   )
comma (,)

The thumb rule is -> whenever we have dependency on right term, eg: 
function, assignment, exponentiation etc, we have right-to-left association
else all have left-to-right association

Bracket > Access > Unary > Arithmetic > Shift > Logical > Equality > bitwise > Assignment 
#BAUA-SLEBA

# Template Literal 
We can form strings using backticks & variables ---
let age = 10;
let name = "Mukul";
let intro = `I am ${name} and I am ${age} years old.`;

## Type Coercion
# The implicit type conversion / type casting is known as Type Coercion in JS.
Examples - 
"Hello" + 123 = 'Hello123' 
'12' - '10' = 2
'23'+'3' = '233'
'23'*'2' = 46
'23'/2 = 11.5


####"Booleans"########

Truthy and falsy values - 
There are only 6 FALSY values :
1 - false
2 - 0
3 - ''
4 - undefined 
5 - null 
6 - NaN 

Everything else is treated as Truthy value 
eg 
->  {}
->  []
->  "  "

are all true values even if they contain nothing 

### Comparision / Equality Operator  

== is loose equality which will try to use coersion before actual comparision
=== is strict comparision which will directly compare.

# Always avoid '==' unless specially requried 

## Prompt
const result = prompt("Message");
# It always takes string from user 


# Explicit Typecasting 
We can use below to typecast like Python -->
Number()
String()
Boolean()

####   Switch Example:###

const day = 'Monday';

switch(day) {
    case 'Monday' :         // Will always use === for comparision
        // Code to be executed
        break;    // if not written , will execute everything till next break
    case 'Teusday':
    case 'Wednesday':
        // to handle multiple OR conditions
        break;
    default:
        // Purely optional, but if no match, execute this
}

### Expression vs Statement

Expression is anything that returns a value 
example - 
2+3
"Hellow"
true && false || true 
Statement is a way to perform actions and consists of expressions :
example - 
if else statements
for loop
function body etc 

#### JS Versions / Releases
ES6 - major release in 2015
All following updates were incremental (ES7/8/...) and follow the 
'dont break the web' principle for backward compatibilities.

# What if users are using old browsers that use older javascript
A simple solution is -
during development use the latest Chrome version (which is guarenteed to support
    the latest features)
But for production -> Always use transpiled/ polyfilled code using babel 
Converting all our new code back to ES5 conventions

ES5 is safe to be used by almost all the browser present on internet.


###########
'use strict' 
When we use it as the first statement of our code, it will show us the 
errors instead of silently failing in production.
It will show us errors for many things that may work but are not allowed 
as part of coding practice.

############
Functions 

#Declaration:
function fnName(...args) {

}

OR 

const fnName = function (...args) {

}

OR 
// the newer way
const fnName = () => expression

const fnName = args => expression 

const fnName = (arg1, arg2, ...) => {
    // statements 
    return result;
}

# Thumb rule is 
# 0 args = () , 1 arg = argName, more args = (arg1, arg2..)
# single line => skip return and {}
# multi-line => include return and {}

## We can not use 'this' keyword in Arrow functions 

##############Arrays####################

const arr = ['1', 'mukul', 4, 5, 'local'];
const arr_1 = new Array(1,2,3,4);

arr.length    // 5    the number of elements in array

### Array Methods #####
const len = arr.push(123); // will add at the end and return the new length
arr.unshift('john')  // adds at the start and returns the length
arr.pop()  // removes and returns the last element
arr.shift() // removes first element and returns it.
arr.indexOf(123) // index of first occurence OR -1
arr.includes(123) // true or false
arr.splice()


















