from key_words import *
import string

# Key Words
key_words = ["array", "boolean", "break", "char", "continue", "do", "else", "false", "function", "if", "integer", "of", "string", "struct", "true", "type", "var", "while"]


# type indentif

def isdigit(c):
<<<<<<< HEAD
    return '0' <= c <= '9'

def isalpha(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')
=======
     return c in "0123456789"

def isalpha(c):
    return c in string.ascii_letters
>>>>>>> 9c8d659f327a9c5344238bbe34ac3b9ac09b97e1

def isspace(c):
    return c in [chr(10), chr(13), "\f", "\v", "\t"," "]

class Lexical_Analysis:
    lexicalError = False
    next_Char = "\f"
    arq = None
    # Literals (x,y,z,name)
    v_Ctes = []
    # Identifiers
    identifiers = {}
    count = 0

    secondary_Token = None
    line = 1
    ch = 1

    def __init__(self, file):
        file.seek(0)
        self.arq = file

    def searchKeyWord(self, keyword): #como key_words é uma lista ordenada podemos usar a busca binária
        left = 0
        right = len(key_words) - 1
        while left <= right:
            middle = (left + right) // 2
            if key_words[middle] == keyword:
                return middle
            elif key_words[middle] > keyword:
                right = middle - 1
            else:
                left = middle + 1
        return ID

    def addCharConst(self, c):
        self.v_Ctes.append(c)
        return len(self.v_Ctes)-1

    def getCharConst(self, c):
        return self.v_Ctes[c]

    def searchName(self, name): 
        if name not in self.identifiers:
            self.identifiers[name] = self.count
            self.count += 1
        return self.identifiers[name]



    def next_Token(self):
        sep = ""
        while isspace(self.next_Char):
            if self.next_Char == "\n" or self.next_Char == "\r":
                self.line+=1
            self.next_Char = self.arq.read(1)
            self.ch+=1
        
        if self.next_Char == "":
            token = EOF 
        
        elif isdigit(self.next_Char):#é um numero? tem . ? acho q tem q implementar com o . => fica no sintatico n?
            num_Aux = []
            while isdigit(self.next_Char):
                num_Aux.append(self.next_Char)
                self.next_Char = self.arq.read(1)
                self.ch+=1
            num = sep.join(num_Aux)
            token = NUMERAL
            self.secondary_Token = self.addCharConst(num)
        
        elif isalpha(self.next_Char):
            text_Aux = []
            while isalpha(self.next_Char) or self.next_Char == '_':
                text_Aux.append(self.next_Char)
                self.next_Char = self.arq.read(1)
                self.ch+=1
            text = sep.join(text_Aux)
            token = self.searchKeyWord(text)
            if token == ID:
                self.secondary_Token = self.searchName(text)
        
        
        elif self.next_Char == "\"": #a barra é um caso mais complicado para representar string
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
            self.secondary_Token = self.addCharConst(string)
        
        else:
            #char
            if self.next_Char == "\'":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = CHARACTER
                self.secondary_Token = self.addCharConst(self.next_Char)
                self.next_Char = self.arq.read(2) 
                self.ch+=2
            #operations
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
            
            elif self.next_Char == "*":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = TIMES

            elif self.next_Char == "/":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = DIVIDE
            #symbols
            elif self.next_Char == ":":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = COLON
            
            elif self.next_Char == ";":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = SEMI_COLON
            elif self.next_Char == ",":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = COMMA

            elif self.next_Char == ".":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = DOT  

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
                    token = UNKNOWN 

            elif self.next_Char == "|":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "|":
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                    token = OR
                else:
                    token = UNKNOWN

            elif self.next_Char == "=":
                self.next_Char = self.arq.read(1)
                self.ch+=1
                if self.next_Char == "=":
                    token = EQUAL_EQUAL
                    self.next_Char = self.arq.read(1)
                    self.ch+=1
                else:
                    token = EQUALS

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

      

            else: #default => don't have char => unknown
                self.next_Char = self.arq.read(1)
                self.ch+=1
                token = UNKNOWN
        return token

    def Lexical_error(self, token): #print err default
        if token == UNKNOWN:
            self.lexicalError = True

    def run(self):
        print("start")
        self.next_Char = self.arq.read(1)
        token_Aux = self.next_Token()
        while token_Aux != EOF: 
            if token_Aux == UNKNOWN:
<<<<<<< HEAD
                print("Character "+str(self.ch+1)+" UNKNOWN ")
            token_Aux = self.next_Token()
=======
                print("Character "+str(self.ch+1)+" UNKOWN ")
            token_Aux = self.next_Token() #sempre analizamos o proximo token
>>>>>>> 9c8d659f327a9c5344238bbe34ac3b9ac09b97e1
        if not self.lexicalError:
            print ("Lexical correct.")


if __name__ == "__main__":
   file = open("input.txt",'r')
   lexical =  Lexical_Analysis(file)
   lexical.run()