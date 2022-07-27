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
    for i in postfix_expression:
      


  def evaluate_postfix_expression(self, expression):
     for i in postfix_expression:
            if i.isdigit():
                self.push(i)
  
           
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str( eval(val2 + i + val1)))
  
        return int(self.pop())


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
