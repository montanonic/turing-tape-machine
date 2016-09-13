# From section 3: Examples of computing machines.
class Machine:
    def __init__(self):
        # Keep track of where we are in the tape
        self.pos = 0
        self.tape = [None]
        self.m_config = None

    def _final_pos(self):
        return len(self.tape) - 1

    def symbol(self):
        return self.tape[self.pos]

    def print(self, value):
        self.tape[self.pos] = value
        return self

    def erase(self):
        self.tape[self.pos] = None
        return self

    def left(self):
        if self.pos - 1 >= 0:
            self.pos -= 1
        else:
            raise 'end of tape reached'
        return self

    def right(self):
        self.pos += 1
        if self.pos > self._final_pos():
            self.tape.append(None)
        return self

# I'm not sure why Turing puts additional spaces between each element in this
# machine. It should only need a single Right operation between prints.
ex1 = Machine()
(ex1
    .print(0).right()
    .right()
    .print(1).right()
    .right())
print("ex1: ", ex1.tape)

##
# I can't get this to work. Lesson: having to embed both state along with
# instructions for how to traverse a one-dimensional array of states leads to...
# difficult code. Turing is a hero.
##
ex2 = Machine()
# The Behavior for this Turing machine
def ex2_b_op():
    '''
    results in 'e | e | 0 | None | 0'
      current symbol ---^---
    m-config == 'o'
    '''
    (ex2
        .print('e').right().print('e').right().print(0)
        .right().right().print(0).left().left())
    ex2.m_config = 'o'
def ex2_o_op():
    symbol = ex2.symbol
    if symbol == 1:
        ex2.right().print('x').left().left().left()
        ex2.m_config = 'o'
    elif symbol == 0:
        ex2.m_config = 'q'
def ex2_q_op():
    if ex2.symbol == None:
        ex2.print(1).left()
        ex2.m_config = 'p'
    else:
        ex2.right().right()
        ex2.m_config = 'q'
def ex2_p_op():
    symbol = ex2.symbol
    if symbol == 'x':
        ex2.erase().right()
        ex2.m_config = 'q'
    elif symbol == 'e':
        ex2.right()
        ex2.m_config = 'f'
    else:
        ex2.left().left()
        ex2.m_config = 'p'
def ex2_f_op():
    if ex2.symbol == None:
        ex2.print(0).left().left()
        ex2.m_config = 'o'
    else:
        ex2.print(0).right().right()
        ex2.m_config = 'f'
ex2_ops = {
    'b': ex2_b_op,
    'o': ex2_o_op,
    'q': ex2_q_op,
    'p': ex2_p_op,
    'f': ex2_f_op,
    }
# initial m-config
ex2.m_config = 'b'

# iterate 10 times
for _ in range(0, 10):
    # execute the operation corresponding to the current symbol and m-config
    ex2_ops[ex2.m_config]()

print("ex2: ", ex2.tape)
