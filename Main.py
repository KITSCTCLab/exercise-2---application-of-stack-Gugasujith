class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    if (self.top == -1):
            return True
        else:
            return False


  def pop(self):
    if not self.is_empty():
            data = self.stack[self.top]
            self.top -= 1
            return data


  def push(self, operand):
     if not self.is_full():
            self.top += 1
            self.stack[self.top] = data

  def validate_postfix_expression(self, expression):
    a = 0
    b = 0
    for element in expression:
      if element.isnumeric():
        a = a + 1
      else:
        b = b + 1
    if b == a - 1:
      return True
    else:
      return False
      


  def evaluate_postfix_expression(self, expression):
     stack = []
    for i in expression:
      if i.isnumeric():
        stack.append(int(i))
      if len(stack) >= 2:
        if i == '+':
          stack[-2] = stack[-2] + stack[-1]
          stack.pop()
        elif i == '-':
          stack[-2] = stack[-2] - stack[-1]
          stack.pop()
        elif i == '*':
          stack[-2] = stack[-2] * stack[-1]
          stack.pop()
        elif i == '/':
          stack[-2] = stack[-2] / stack[-1]
          stack.pop()
        elif i == '^':
          stack[-2] = stack[-2] ^ stack[-1]
          stack.pop()
    return int(stack[-1])


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
