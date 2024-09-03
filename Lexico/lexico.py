from Lexico.key_words import *
import string

# Key Words
key_words = ["array", "boolean", "break", "char", "continue", "do", "else", "false", "function", "if", "integer", "of", "string", "struct", "true", "type", "var", "while"]


# type indentif

def is_Digit(c):
    if c in "0123456789":
        return True
    return False

def is_Alnum(c):
    if c in string.ascii_letters:
        return True
    return False

def is_Space(c):
    if c in [chr(10), chr(13), "\f", "\v", "\t"," "]:
        return True
    return False

# Lexical_Finite_Automaton
class Lexical_Analysis:
    lexicalError = False
    next_Char = "\f"
    arq = None

    def __init__(self, file):
        file.seek(0)
        self.arq = file

    def search_Key_Word(self, name): #como é uma lista ordenada podemos usar a busca binária
        left = 0
        right = len(key_words) - 1
        while left <= right:
            middle = (left + right) // 2
            if key_words[middle] == name:
                return middle
            elif key_words[middle] > name:
                right = middle - 1
            else:
                left = middle + 1
        return ID

    # Literals (x,y,z,name)
    v_Ctes = []

    def add_Cte(self, c):
        self.v_Ctes.append(c)
        return len(self.v_Ctes)-1

    def get_Cte(self, c):
        return self.v_Ctes[c]

    # Identifiers
    identifiers = {}
    count = 0

    def search_Name(self, name): 
        if name not in self.identifiers:
            self.identifiers[name] = self.count
            self.count += 1
        return self.identifiers[name]

    secondary_Token = None
    line = 1
    ch = 1

    def next_Token(self):
        sep = ""
        while is_Space(self.next_Char):
            if self.next_Char == "\n" or self.next_Char == "\r":
                self.line+=1
            self.next_Char = self.arq.read(1)
            self.ch+=1
        
        if self.next_Char == "":
            token = EOF #end of file
        
        elif is_Alnum(self.next_Char):
            text_Aux = []
            while is_Alnum(self.next_Char) or self.next_Char == '_':
                text_Aux.append(self.next_Char)
                self.next_Char = self.arq.read(1)
                self.ch+=1
            text = sep.join(text_Aux)
            token = self.search_Key_Word(text)
            if token == ID:
                self.secondary_Token = self.search_Name(text)
        
        elif is_Digit(self.next_Char):#é um numero? tem . ? acho q tem q implementar com o . => fica no sintatico n?
            num_Aux = []
            while is_Digit(self.next_Char):
                num_Aux.append(self.next_Char)
                self.next_Char = self.arq.read(1)
                self.ch+=1
            num = sep.join(num_Aux)
            token = NUMERAL
            self.secondary_Token = self.add_Cte(num)
        
        elif self.next_Char == "\"":
            string_Aux = []
            string_Aux.append(self.next_Char)
            self.next_Char = self.arq.read(1)
            self.ch+=1
            if self.next_Char != "\"":
                while(self.next_Char!="\""):
                    string_Aux.append(self.next_Char)
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
            string_Aux.append(self.next_Char)
            self.next_Char = self.arq.read(1)
            self.ch+=1
            string = sep.join(string_Aux)
            token = STRING
            self.secondary_Token = self.add_Cte(string)
        
        else:
            if self.next_Char == "\'":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = CHARACTER
                self.secondary_Token = self.add_Cte(self.next_Char)
                self.next_Char = self.arq.read(2) 
                self.ch+=2
            elif self.next_Char == ":":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = COLON
            elif self.next_Char == "+":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "+":
                    token = PLUS_PLUS
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                else:
                    token = PLUS
            elif self.next_Char == "-":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "-":
                    token = MINUS_MINUS
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                else:
                    token = MINUS
            elif self.next_Char == ";":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = SEMI_COLON
            elif self.next_Char == ",":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = COMMA
            elif self.next_Char == "=":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "=":
                    token = EQUAL_EQUAL
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                else:
                    token = EQUALS
            elif self.next_Char == "[":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = LEFT_SQUARE
            elif self.next_Char == "]":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = RIGHT_SQUARE
            elif self.next_Char == "{":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = LEFT_BRACES
            elif self.next_Char == "}":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = RIGHT_BRACES
            elif self.next_Char == "(":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = LEFT_PARENTHESIS
            elif self.next_Char == ")":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = RIGHT_PARENTHESIS

            elif self.next_Char == "&":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "&":
                    self.next_Char=self.arq.read(1)
                    self.ch+=1
                    token = AND
                else:
                    token = UNKNOWN #Comparação bit a bit? n vamos implementar

            elif self.next_Char == "|":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "|":
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                    token = OR
                else:
                    token = UNKNOWN

            elif self.next_Char == ">":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "=":
                    token = GREATER_OR_EQUAL
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                else:
                    token = GREATER_THAN
            elif self.next_Char == "<":
                self.next_Char=self.arq.read(1)
                self.ch+=1
                if self.next_Char == "=":
                    token = LESS_OR_EQUAL
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                else:
                    token=LESS_THAN
            elif self.next_Char == "!":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "=":
                    token = NOT_EQUAL
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                else:
                    token = NOT 
            elif self.next_Char == "*":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = TIMES
            elif self.next_Char == ".":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = DOT        
            elif self.next_Char == "/":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = DIVIDE
            else: #default => don't have char => unknown
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = UNKNOWN
        return token

    def Lexical_error(self, token): #print err default
        if token == UNKNOWN:
            self.lexicalError = True
            print("Character "+str(self.ch+1)+" not expected in the line " + str(self.line))

    def run(self):
        self.next_Char = self.arq.read(1)
        token_Aux = self.next_Token()
        while token_Aux != EOF: 
            if token_Aux == UNKNOWN:
                print("Character "+str(self.ch+1)+" not expected in the line " + str(self.line))
                self.lexicalError = True
            token_Aux = self.next_Token()
        if not self.lexicalError:
            print ("No lexical errors.")
