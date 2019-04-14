import sys
import argparse
from antlr4 import *
from IECSTGrammarLexer import IECSTGrammarLexer
from IECSTGrammarParser import IECSTGrammarParser
from IECSTGrammarVisitor import IECSTGrammarVisitor
from IECSTExpressions import *
from IECSTtoHPPrettyPrinter import *
from typing import List


# Read an ST configuration file into this structure
config: ConfigurationFile = None


def process_st_file(st_file):
	global config
	input = FileStream(st_file)
	lexer = IECSTGrammarLexer(input)
	stream = CommonTokenStream(lexer)
	parser = IECSTGrammarParser(stream)
	configFile = parser.configurationfile()
	configVisitor= IECSTGrammarVisitor()
	config  = configVisitor.visit(configFile)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='HyPLC ST to HP translation tool.')
	parser.add_argument('-STFile','--STFile', help='Input ST file to be translated', required=True)
	parser.add_argument('-HPFile','--HPFile', help='HP file where ctrl will be replaced with translation', required=False)

	args = vars(parser.parse_args())

    # Currently only process one ST file with one Program defined at a time
	process_st_file(args['STFile'])

	# Iterate through all structured text programs and generate a hybrid program
	# (for this implementation, we are only generating one):
	printer = IECSTtoHPPrettyPrinter(config)
	ctrl = printer.configuration_file_to_string()

	#If the user specified an input HP file to replace the ctrl: 
	if args['HPFile'] is not None:
		hpStr = ""
		#Add clk info
		ctrl = ctrl + "\n\tt:= 0; {t'=1&t<e}"
		with open(args['HPFile'], "rt") as fin:
			for line in fin:
				hpStr = hpStr + line.replace('ctrl', ctrl)

		print(hpStr)
	else:
		print(ctrl)

