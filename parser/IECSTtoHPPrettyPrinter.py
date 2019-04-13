from IECSTExpressions import *
from typing import List, TypeVar

################################################################
# HP Pretty Printer functions
################################################################
class IECSTtoHPPrettyPrinter:

	globalTimeInterval : TimeInterval = None
	stConfigFile : ConfigurationFile = None

	def __init__(stConfigFile:ConfigurationFile, hpFile=None):
		self.stConfigFile = stConfigFile

	################################################################
	# Operator translations
	################################################################
	def unary_operator_to_string(unaryOperator: UnaryOperator):
		if isinstance(unaryOperator, NegateOperator):
			return "-"
		elif isinstance(unaryOperator, LogicalNegateOperator):
			return "!"
		else:
			raise ValueError('PrettyPrinter: Invalid unary operator')

	def multiply_operator_to_string(multiplyOperator: MultiplyOperator):
		if isinstance(multiplyOperator, DivideOperator):
			return "/"
		elif isinstance(multiplyOperator, MultiplyOperator):
			return "*"
		else:
			raise ValueError('PrettyPrinter: Invalid multiply operator')

	def add_operator_to_string(addOperator: ComparisonOperator):
		if isinstance(addOperator, PlusOperator):
			return "+"
		elif isinstance(addOperator, MinusOperator):
			return "-"
		else:
			raise ValueError('PrettyPrinter: Invalid add operator')

	def comparison_operator_to_string(comparisonOperator: ComparisonOperator):
		if isinstance(comparisonOperator, GreaterThanOperator):
			return ">"
		elif isinstance(comparisonOperator, GreaterThanOrEqualOperator):
			return ">="
		elif isinstance(comparisonOperator, LessThanOperator):
			return "<"
		elif isinstance(comparisonOperator, LessThanOrEqualOperator):
			return "<="
		else:
			raise ValueError('PrettyPrinter: Invalid comparison operator')

	################################################################
	# Expression translations
	################################################################

	def literal_to_string(literal : Literal):
		if isInstance(literal, TRUE):
			return "true"
		elif isInstance(literal, FALSE):
			return "false"
		elif isInstance(literal, NumericLiteral):
			return str(literal.value)
		else:
			raise ValueError('PrettyPrinter: invalid literal expression.')

	def primary_expression_to_string(primaryExpression: PrimaryExpression):
		if isInstance(primaryExpression, PrimaryExpressionExpression):
			return "(" + self.expression_to_string((PrimaryExpressionExpression)(primaryExpression).expr) + ")"
		elif isInstance(primaryExpression, Literal):
			return self.literal_to_string(primaryExpression)
		elif isInstance(primaryExpression, Variable):
			return self.variable_to_string(primaryExpression)
		else:
			raise ValueError('PrettyPrinter: invalid primary expression')

	def unary_expression_to_string(unaryExpr: UnaryExpression):
		unaryExprString = self.primary_expression_to_string(unaryExpr.primaryExpression)
		if unaryExpr.unaryOperator not None:
			unaryExprString = self.unary_operator_to_string(unaryExpr.unaryOperator) + "( "+ unaryExprString+ " )"
		return unaryExprString

	def power_expression_to_string(powerExpr: PowerExpression):
		powerExprString = self.unary_expression_to_string(powerExpr.unaryExpressions[0])
		for i in range(len(powerExpr.unaryExpressions)-1):
			powerExprString = "( " +powerExprString + ")^ " + self.unary_expression_to_string(powerExpr.unaryExpressions[i+1])
		return powerExprString

	def term_to_string(termExpr: Term):
		termExprString = self.power_expression_to_string(termExpr.powerExpressions[0])
		for i in range(len(termExpr.powerExpressions)-1):
			termExprString = termExprString + multiply_operator_to_string(termExpr.multiplyOperators[i]) + self.power_expression_to_string(termExpr.powerExpressions[i+1])
		return termExprString

	def term_to_string(termExpr: Term):
		termExprString = self.power_expression_to_string(termExpr.powerExpressions[0])
		for i in range(len(termExpr.powerExpressions)-1):
			termExprString = termExprString + multiply_operator_to_string(termExpr.addOperators[i]) + self.power_expression_to_string(termExpr.powerExpressions[i+1])
		return termExprString

	def add_expression_to_string(addExpr: ADDExpression):
		addExprString = self.term_to_string(addExpr.terms[0])
		for i in range(len(addExpr.terms)-1):
			addExprString = addExprString + add_operator_to_string(addExpr.addOperators[i]) + self.term_to_string(addExpr.terms[i+1])
		return addExprString

	def equ_expression_to_string(equExpr: EQUExpression):
		equExprString = self.add_expression_to_string(equExpr.addExpressions[0])
		for i in range(len(equExpr.addExpressions)-1):
			equExprString = equExprString + comparison_operator_to_string(equExpr.comparisonOperators[i]) + self.add_expression_to_string(equExpr.addExpressions[i+1])
		return equExprString


	def comparison_to_string(comparisonExpr: Comparison):
		comaprisonExprString = self.equ_expression_to_string(comparisonExpr.equExpressions[0])
		for i in range(len(comparisonExpr.equExpressions)-1):
			comaprisonExprString = comaprisonExprString + " = " + self.equ_expression_to_string(comparisonExpr.equExpressions[i+1])
			# If it is a NotEquals Operator ("<>"), we need to add a negation before:
			if isInstance(comparisonExpr.equOperators[i], NotEqualOperator): 
				comparisonExprString = "!( " + comparisonExprString + ")"
		return comaprisonExprString

	def and_expression_to_string(andExpr : ANDExpression):
		andExprString = self.comparison_to_string(andExpr.comparisons[0])
		for i in range(len(andExpr.comparisons)-1):
			# Translation of "AND" expression: &
			andExprString = andExprString + " & " + self.comparison_to_string(andExpr.comparisons[i+1])
		return andExprString

	def xor_expression_to_string(xorExpr : XORExpression):
		xorExprString = self.and_expression_to_string(xorExpr.andExpressions[0])
		for i in range(len(xorExpr.andExpressions)-1):
			# Translation of "XOR" expression: negation of bi-implication
			xorExprString = "!( " + xorExprString + " <-> " + self.and_expression_to_string(xorExpr.andExpressions[i+1])+")"
		return xorExprString

	def expression_to_string(expr : Expression):
		exprString = self.xor_expression_to_string(expr.xorExpressions[0])
		for i in range(len(expr.xorExpressions)-1):
			# Translation of OR expression: "|"
			exprString = exprString + " | " + self.xor_expression_to_string(expr.xorExpressions[i+1])
		return exprString

	def variable_to_string(variable : Variable):
		return variable.name

	################################################################
	# Statement translations
	################################################################
	def assignment_statement_to_string(assignmentStatement: AssignmentStatement):
		return self.variable_to_string(assignmentStatement.variable) + " := " + self.expression_to_string(assignmentStatement.expr)


	def if_then_else_statement_to_string(ifThenElseStatement: IfThenElseStatement):
		stmtString = ""
		tabLevel = 0;
		# Process all if and elif-then else statements
		for i in range(len(ifThenElseStatement.ifExpressions)):
			exprString : str = self.expression_to_string(ifThenElseStatement.ifExpressions[i])
			thenStmtString : str = self.statement_to_string(ifThenElseStatement.thenStatements[i])
			stmtString = stmtString + "\n{\t"*(tabLevel) +"\n"+"\t"*(tabLevel+1) + "?("+exprString+"); "+ thenStmtString+"; ++"
			stmtString = stmtString + "\n"+"\t"*(tabLevel+1)+"?!("+exprString+"); "
		# Process final else statement if it exists:
		if ifThenElseStatement.elseStatement not None:
			stmtString = stmtString + self.statement_to_string(ifThenElseStatement.elseStatement)
		for i in tabLevel:
			stmtString = stmtString + "\n"+(tabLevel-i)*"\t" + "}"

		return stmtString


	def statement_to_string(statement: Statement):
		if isInstance(statement, NilStatement):
			return ""
		elif isInstance(statement, AssignmentStatement):
			return self.assignment_statement_to_string(statement)
		elif isInstance(statement, IfThenElseStatement):
			return self.if_then_else_statement_to_string(statement)
		else:
			raise ValueError('Invalid statement')

	################################################################
	# Configuration elements
	################################################################
	def program_to_string(program: Program):
		#For delaring sensor input values for HP scan cycle nomral form
		inputString = ""
		progBlockBody = ""
		for varBlock in program.varBlocks:
			if isInstance(varBlock, VarInputBlock):
				#Set non-deterministic value to sensor inputs
				for variable in varBlock.variables:
					inputString = inputString + self.variable_to_string(variable.name) + " := *; " 
		programBlockBody = ""
		for statement in program.programBlockBody:
			programBlockBody = programBlockBody + self.statement_to_string(statement) + ";\n"
		return inputString + "\n" + programBlockBody

	def configuration_file_to_string():
	    configString = self.program_to_string(self.stConfigFile.program) + "\n" + self.configuration_to_string(stConfigFile.config)
	    return configString