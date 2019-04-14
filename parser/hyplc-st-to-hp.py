import sys
from antlr4 import *
from IECSTGrammarLexer import IECSTGrammarLexer
from IECSTGrammarParser import IECSTGrammarParser
from IECSTGrammarVisitor import IECSTGrammarVisitor
from IECSTExpressions import *
from IECSTtoHPPrettyPrinter import *
from typing import List

# Read a number of ST configuration files into this list
configs: List[ConfigurationFile] = []


def process_st_file(st_file):
    input = FileStream(st_file)
    lexer = IECSTGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = IECSTGrammarParser(stream)
    configFile = parser.configurationfile()
    configVisitor= IECSTGrammarVisitor()
    configFile : ConfigurationFile = configVisitor.visit(configFile)
    print("Generated ConfigurationFile: ",configFile)
    configs.append(configFile)


# TODO: Incorporate continuous dynamics (currently only generates discrete state transitions from ST code)
#       This would require an auxiliary file with the continuous plant

if __name__ == '__main__':
    # Currently only process one ST file with one Program defined at a time
    process_st_file(sys.argv[1])
    # Iterate through all structured text programs and generate a hybrid program
    # (for this implementation, we are only generating one):
    for config in configs:
    	printer = IECSTtoHPPrettyPrinter(config)
    	print(printer.configuration_file_to_string())