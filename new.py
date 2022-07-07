 

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "619fc045",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28\n",
      "<class 'float'>\n",
      "<class 'str'>\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "#printing types of variables\n",
    "a=28\n",
    "b=34.44\n",
    "c=\"shibu\"\n",
    "d=45\n",
    "print(a)\n",
    "print(type(b))\n",
    "print(type(c))\n",
    "print(type(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "02f7b5f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the value of 5+6 is 11\n",
      "the value of 5+6 is 30\n",
      "the value of 5+6 is -1\n",
      "the value of 5+6 is 0.8333333333333334\n"
     ]
    }
   ],
   "source": [
    "#operators in python\n",
    "a=5\n",
    "b=6\n",
    "print(\"the value of 5+6 is\",5+6)\n",
    "print(\"the value of 5+6 is\",5*6)\n",
    "print(\"the value of 5+6 is\",5-6)\n",
    "print(\"the value of 5+6 is\",5/6)th\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5e10e7b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "#Assiment operators\n",
    "a=6\n",
    "a=3\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "02c0bfa7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "#Assiment operators\n",
    "a=6\n",
    "a+=3\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1841b82e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "#Assiment operators\n",
    "a=6\n",
    "a-=3\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bd204838",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18\n"
     ]
    }
   ],
   "source": [
    "#Assiment operators\n",
    "a=6\n",
    "a*=3\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a961461b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22.0\n"
     ]
    }
   ],
   "source": [
    "a=34\n",
    "a-=12\n",
    "a*=12\n",
    "a/=12\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2155fcb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "#comparison operators\n",
    "a=43\n",
    "b=42\n",
    "print(a==b)\n",
    "print(a>b)\n",
    "print(a>=b)\n",
    "print(a<b)\n",
    "print(a!=b)\n",
    "#comparison operators return boolun value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8be7bc5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the value of bool1 and bool2 is False\n",
      "the value of bool1 or bool2 is True\n",
      "the value of not bool2 is True\n"
     ]
    }
   ],
   "source": [
    "#logical operators\n",
    "bool1=True\n",
    "bool2=False\n",
    "print(\"the value of bool1 and bool2 is\",(bool1 and bool2))\n",
    "print(\"the value of bool1 or bool2 is\",(bool1 or bool2))\n",
    "print(\"the value of not bool2 is\",(not bool2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f20f7e93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "#typecasting in python\n",
    "a=\"543\"\n",
    "a=int(a)\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f346a840",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "546\n"
     ]
    }
   ],
   "source": [
    "a=\"543\"\n",
    "a=int(a)\n",
    "print(type(a))\n",
    "print(a+3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "67875a19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number:54\n",
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "#input_function.py\n",
    "a=input(\"Enter the number:\")\n",
    "a=int(a)\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f050e1cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the value of a and b is 11\n"
     ]
    }
   ],
   "source": [
    "#1write a python program to add two numbers\n",
    "a=6\n",
    "b=5\n",
    "print(\"the value of a and b is\",a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f1f37cba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the remainder when a is divided by b is 0\n"
     ]
    }
   ],
   "source": [
    "#2write a python program to find remainder when a number is diveded by 2\n",
    "a=45\n",
    "b=15\n",
    "print(\"the remainder when a is divided by b is\",a%b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f1370be6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number:45\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "#3check the type of the variable assinged using input function\n",
    "a=input(\"Enter the number:\")\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2268fdfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "#4use comparison operators to find out whether a given variable a is greter than 'b'not.take a=34 and b=80\n",
    "a=34\n",
    "b=80\n",
    "print(b>a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bb54ccba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the first number:5\n",
      "enter the second number:5\n",
      "the average a and b is 5.0\n"
     ]
    }
   ],
   "source": [
    "#write a python program to find average of two numbers entered by the user\n",
    "a=input(\"enter the first number:\")\n",
    "b=input(\"enter the second number:\")\n",
    "a=int(a)\n",
    "b=int(b)\n",
    "average=(a+b)/2\n",
    "print(\"the average a and b is\",average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5069d539",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number:5\n",
      "3125\n"
     ]
    }
   ],
   "source": [
    "#6write a python program to calculate square of a number entered by the user\n",
    "a=input(\"enter the number:\")\n",
    "a=int(a)\n",
    "print(a**a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5496994c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "4+5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f3f1d299",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "4+4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2b13e190",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3*6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "56cd5336",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "8*4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "89fb35fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "390"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "78*5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8bca7f8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "a=4\n",
    "b=6\n",
    "c=a+b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3995d5ed",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

