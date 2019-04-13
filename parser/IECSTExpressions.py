from typing import List, TypeVar
from abc import abstractmethod


'''
    Instance of an ST Configuration file
'''
class ConfigurationFile:
	program = None
	config  = None
    
    def __init__(self, program, config):
        self.program : Program = program
        self.config: Configuration = config

'''
    Instance of an ST Program 
'''
class Program:

	name = None
	varBlocks = None
	programBlockBody = None

	def __init__(self, name, varBlocks, programBlockBody):
		self.name : str = name
		self.varBlocks : List[VarBlock] = varBlocks
		self.programBlockBody : List[Statement] = programBlockBody

'''
    Instance of an ST Configuration that defines the program, resource,
    and task configurations. Currently, HyPLC only supports a single
    program with a single task running on a single resource. 
'''
class Configuration:

	name = None
	resourceDeclarations = None 

	def __init__(self, name, resourceDeclarations):
		self.name : str = name
		self.resourceDeclarations : List[Resource] = resourceDeclarations

class Resource:

	name = None # Not required if single resource
	resourceTypeName = None # Not required if single resource
	taskConfiguration = None
	programConfiguration = None

	def __init__(self, taskConfiguration, programConfiguration, name = None, resourceTypeName = None):
		self.name : str = name
		self.resourceTypeName : str = resourceTypeName
		self.taskConfiguration : TaskConfiguration = taskConfiguration
		self.programConfiguration : TaskConfiguration = programConfiguration

class TaskConfiguration:

	name = None
	single = None # Boolean if it is a single task; Not required
	interval = None # Task execution scan cycle time
	priority = None # Priority of task; Currently not relevant

	def __init__(self, name, interval, priority, single = None):
		self.name : str = name
		self.interval : TimeInterval = interval
		self.priority : int = priority
		self.single: int = single

class TimeInterval: 

	value = None
	timeUnit = None

	def __init__(self, value, timeUnit):
		self.value : int = value
		self.timeUnit : str = timeUnit

########################################################################
# VarBlock Classes
########################################################################
'''
    Instance of an ST Variable Block that declares a variable type 
    and I/O configuration for a program. This is the base class
    for variable declarations and actually represents a local variable.
    There will be subclass iomplementations for the VAR_INTPUT and 
    VAR_OUTPUT cases.
'''
class VarBlock: 

	ioconfig = 'VAR' # Local variable by default
	variables = None # List of declared variables

	def __init__(self, variables):
		self.variables : List[Variable] = variables
'''
    VAR_INPUT block
'''
class VarInputBlock(VarBlock):

	ioconfig = 'VAR_INPUT'

'''
    VAR_OUTPUT block
'''
class VarOutputBlock(VarBlock):

	ioconfig = 'VAR_OUTPUT'


########################################################################

class Variable:

	name = None
	varType = None

	def __init__(self, name, varType):
		self.name : str = name
		self.varType : str = varType

########################################################################
# Statement Classes
########################################################################
class Statement:
	pass

class NilStatement(Statement):
	pass

class AssignmentStatement(Statement):

	variable = None
	expr = None

	def __init__(self, variable, expr):
		self.variable : Variable = variable
		self.expr : Expression = expr

class IfThenElseStatement(Statement):

	# List of expressions should be same size as list of then statements
	ifExpressions = None
	thenStatements = None
	elseStatement = None

	def __init__(self, ifExpressions, thenStatements, elseStatement = None):
		self.ifExpressions : List[Expression] = ifExpressions
		self.thenStatements : List[Statement] = thenStatements
		self.elseStatement : Statement = elseStatement


########################################################################
# Expression Classes (adhering to ST Grammar)
########################################################################
class Expression:

	# List of "XORExpressions" that are OR'd together
	xorExpressions= None

	def __init__(self, xorExpressions):
		self.xorExpressions : List[XORExpression] = xorExpressions


class XORExpression(Expression):

	# List of "ANDExpressions" that are XOR'd together
	andExpressions = None

	def __init__(self, andExpressions):
		self.andExpressions : List[ANDExpression] = andExpressions

class ANDExpressions(Expression):

	# List of "Comparisons" that are AND'd together
	comparisons = None

	def __init__(self, comparisons):
		self.comparisons : List[Comparison] = comparisons


class Comparison(Expression):

	#List of "EQUExpressions" that are compared together
	equExpressions = None
	equOperators = None

	def __init__(self, equExpressions, equOperators):
		self.equExpressions : List[EQUExpression] = equExpressions
		self.equOperators : List[EQUOperator] = equOperators

class EQUExpression(Expression):

	#List of "ADDExpressions" that are compared using a given operator
	addExpressions = None
	#List of associated comparison operators
	comparisonOperators - None

	def __init__(self, addExpressions, comparisonOperators):
		self.addExpressions : List[ADDExpression] = addExpressions
		self.comparisonOperators : List[ComaprisonOperator] = comparisonOperators

class ADDExpression(Expression):

	#List of terms with a subsequent list of add operators applied
	terms = None
	addOperators = None

	def __init__(self, terms, addOperators):
		self.terms : List[Term] = terms
		self.addOperators : List[ADDOperator] = addOperators


class PowerExpression(Expression):

	#List of unary expressions which to apply subsequent exponents
	unaryExpressions  = None

	def __init__(self, unaryExpressions)
		self.unaryExpressions : List[UnaryExpression] = unaryExpressions


class UnaryExpression(Expression):

	unaryOperator = None
	primaryExpression = None

	def __init__(self, unaryOperator, primaryExpression):
		self.unaryOperator : UnaryOperator = unaryOperator
		self.primaryExpression : PrimaryExpression = primaryExpression

class Term(Expression):

	# List of power expressions and  their subsequent mulitply operators
	powerExpressions = None
	multiplyOperators = None

	def __init__(self, powerExpressions, multiplyOperators):
		self.powerExpressions : List[PowerExpression] = powerExpressions
		self.multiplyOperators : List[MultiplyOperator] = multiplyOperators

########################################################################
# Primary Expression Classes (adhering to ST Grammar)
########################################################################

class PrimaryExpression(Expression):
	pass

# Just an expression in parentheses
class PrimaryExpressionExpression(PrimaryExpression):
	expr = None

	def __init__(self, expr):
		self.expr : Expression = expr

class Literal(PrimaryExpression):
	value = None

class BooleanLiteral(Literal):
	pass

class TRUE(BooleanLiteral):
	value = "TRUE"

class FALSE(BooleanLiteral):
	value = "FALSE"

class NumericLiteral(Literal):
	pass

# For generating HPs, we convert everything to ints or floats
class IntegerLiteral(NumericLiteral):

	def __init__(self, value):
		self.value : int = int(value)

class FloatingPointLiteral(NumericLiteral):

	def __init__(self, value):
		self.value : float = float(value)


########################################################################
# Operator Classes (adhering to ST Grammar)
########################################################################
class Operator:
	operatorStr = None

########################################################################
# Equal Comparison Operator Classes (adhering to ST Grammar)
########################################################################
class EquOperator(Operator):
	pass

class EqualsOperator(EquOperator):
	operatorStr = "="

class NotEqualOperator(EquOperator):
	oepratorStr = "<>"

########################################################################
# Comparison Operator Classes (adhering to ST Grammar)
########################################################################
class ComparisonOperator(Operator):
	pass

class GreaterThanOperator(ComparisonOperator):
	operatorStr = ">"

class LessThanOperator(ComparisonOperator):
	operatorStr = "<"

class GreaterThanOrEqualOperator(ComparisonOperator):
	operatorStr = ">="

class LessThanOrEqualOperator(ComparisonOperator):
	operatorStr = "<="


########################################################################
# Add Operator Classes (adhering to ST Grammar)
########################################################################
class ADDOperator(Operator):
	pass

class PlusOperator(ADDOperator):
	operatorStr = "+"

class MinusOeprator(ADDOperator):
	operatorStr = "-"


########################################################################
# Multiply Operator Classes (adhering to ST Grammar)
########################################################################
class MultiplyOperator(Operator):
	operatorStr = "*"

class DivideOperator(MultiplyOperator):
	operatorStr = "/"

########################################################################
# Unary Operator Classes (adhering to ST Grammar)
########################################################################
class UnaryOperator(Operator):
	pass

class NegateOperator(UnaryOperator):
	operatorStr = "-"

class LogicalNegateOperator(UnaryOperator):
	operatorStr = "NOT"









