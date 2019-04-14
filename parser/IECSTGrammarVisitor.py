# Generated from IECSTGrammar.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IECSTGrammarParser import IECSTGrammarParser
else:
    from IECSTGrammarParser import IECSTGrammarParser

#Added imports 
from typing import List, TypeVar, Dict
from IECSTExpressions import *

# This class defines a complete generic visitor for a parse tree produced by IECSTGrammarParser.

class IECSTGrammarVisitor(ParseTreeVisitor):

    program : Program = None
    config : Configuration = None
    varDecs: Dict[str, Variable] = {}

    # Visit a parse tree produced by IECSTGrammarParser#configurationfile.
    def visitConfigurationfile(self, ctx:IECSTGrammarParser.ConfigurationfileContext):
        self.visitChildren(ctx)
        return ConfigurationFile(self.program, self.config)


    # Visit a parse tree produced by IECSTGrammarParser#program.
    def visitProgram(self, ctx:IECSTGrammarParser.ProgramContext):
        nameStr : str = ctx.name.text
        varBlocks : List[VarBlock] = []
        for varBlock in ctx.var_block():
            varBlocks.append(self.visitVar_block(varBlock))
        programBlockBody : List[Statement] = self.visitProgram_block_body(ctx.program_block_body())
        self.program = Program(nameStr, varBlocks, programBlockBody)


    # Visit a parse tree produced by IECSTGrammarParser#configuration.
    def visitConfiguration(self, ctx:IECSTGrammarParser.ConfigurationContext):
        name : str = ctx.name.text
        resourceDeclarations : List[ResourceDeclaration] = []
        for resourceDeclaration in ctx.resource_declaration():
            resourceDeclarations.append(self.visitResource_declaration(ctx.resource_declaration()))
        self.config = Configuration(name, resourceDeclarations)


    # Visit a parse tree produced by IECSTGrammarParser#resource_declaration.
    def visitResource_declaration(self, ctx:IECSTGrammarParser.Resource_declarationContext):
        #We're only considering a single resource at a time.
        name : str = ctx[0].name.text
        resourceTypeName: str = ctx[0].resource_type_name.text
        tmpResource : Resource = self.visitSingle_resource_declaration(ctx[0].single_resource_declaration())
        return Resource(tmpResource.taskConfiguration, tmpResource.programConfiguration, name, resourceTypeName)


    # Visit a parse tree produced by IECSTGrammarParser#single_resource_declaration.
    def visitSingle_resource_declaration(self, ctx:IECSTGrammarParser.Single_resource_declarationContext):
        taskConfiguration : TaskConfiguration = self.visitTask_configuration(ctx.task_configuration())
        programConfiguration : ProgramConfiguration = self.visitProgram_configuration(ctx.program_configuration())
        return Resource(taskConfiguration, programConfiguration)


    # Visit a parse tree produced by IECSTGrammarParser#task_configuration.
    def visitTask_configuration(self, ctx:IECSTGrammarParser.Task_configurationContext):
        name : str = ctx.name.text
        taskInitialization : TaskInitialization = self.visitTask_initialization(ctx.task_initialization())
        return TaskConfiguration(name, taskInitialization)


    # Visit a parse tree produced by IECSTGrammarParser#task_initialization.
    def visitTask_initialization(self, ctx:IECSTGrammarParser.Task_initializationContext):
        intervalTime : TimeInterval = self.visitInterval_time(ctx.interval_time())
        single : int = None
        priority : int = None
        if len(ctx.Decimal_literal()) > 1:
            single: int = int(str(ctx.Decimal_literal()[0].getText()))
            priority: int = int(str(ctx.Decimal_literal()[1].getText()))
        else:
            priority: int = int(str(ctx.Decimal_literal()[0].getText()))

        return TaskInitialization(intervalTime, priority, single)


    # Visit a parse tree produced by IECSTGrammarParser#interval_time.
    def visitInterval_time(self, ctx:IECSTGrammarParser.Interval_timeContext):
        value : int = int(ctx.Decimal_literal().getText())
        timeUnit : str = self.visitTime_unit(ctx.time_unit())
        return TimeInterval(value, timeUnit)


    # Visit a parse tree produced by IECSTGrammarParser#time_unit.
    def visitTime_unit(self, ctx:IECSTGrammarParser.Time_unitContext):
        return ctx.getText()


    # Visit a parse tree produced by IECSTGrammarParser#program_configuration.
    def visitProgram_configuration(self, ctx:IECSTGrammarParser.Program_configurationContext):
        instName : str = ctx.inst_name.text
        taskName : str = ctx.task_name.text
        progName : str = ctx.prog_name.text
        return ProgramConfiguration(instName, taskName, progName)


    # Visit a parse tree produced by IECSTGrammarParser#var_block.
    def visitVar_block(self, ctx:IECSTGrammarParser.Var_blockContext):
        varList : List[Variable] = []
        for varDec in ctx.variables:
            # Each variable dec could have multiple variables declared in a line
            varList = varList + self.visitVariable_declaration(varDec)
        if (ctx.output and ctx.input):
            raise ValueError('visitVar_block: Variable cannot be input AND output')
        if (ctx.input):
            return VarInputBlock(varList)
        elif (ctx.output):
            return VarOutputBlock(varList)
        else:
            return VarBlock(varList)


    # Visit a parse tree produced by IECSTGrammarParser#simpleType.
    def visitSimpleType(self, ctx:IECSTGrammarParser.SimpleTypeContext):
        return ctx.name.text


    # Visit a parse tree produced by IECSTGrammarParser#variable_declaration.
    def visitVariable_declaration(self, ctx:IECSTGrammarParser.Variable_declarationContext):
        variables : List[Variable] = []
        varType : str = self.visitSimpleType(ctx.var_type)
        # Each variable dec could have multiple variables declared in a line
        for varName in ctx.names:
            newVar = Variable(varName.text, varType)
            variables.append(newVar)
            self.varDecs[varName.text] = newVar
        return variables


    # Visit a parse tree produced by IECSTGrammarParser#program_block_body.
    def visitProgram_block_body(self, ctx:IECSTGrammarParser.Program_block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#statement_list.
    def visitStatement_list(self, ctx:IECSTGrammarParser.Statement_listContext):
        statementList : List[Statement] = []
        for statement in ctx.statement():
            statementList.append(self.visitStatement(statement))
        return statementList


   # Visit a parse tree produced by IECSTGrammarParser#statement.
    def visitStatement(self, ctx:IECSTGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#assignment_statement.
    def visitAssignment_statement(self, ctx:IECSTGrammarParser.Assignment_statementContext):
        variable = self.visitVariable(ctx.variable())
        expr = self.visitExpression(ctx.expression())
        return AssignmentStatement(variable, expr)


    # Visit a parse tree produced by IECSTGrammarParser#if_then_else_statement.
    def visitIf_then_else_statement(self, ctx:IECSTGrammarParser.If_then_else_statementContext):
        ifExpressions : List[Expression] = []
        thenStatementLists: List[List[Statement]] = []
        elseStatementList: List[Statement] = None

        for i  in range(len(ctx.expression())):
            ifExpressions.append(self.visitExpression(ctx.expression()[i]))
            thenStatementLists.append(self.visitStatement_list(ctx.statement_list()[i]))
        if(len(ctx.expression()) < len(ctx.statement_list())):
            elseStatementList = self.visitStatement_list(ctx.statement_list()[-1])

        return IfThenElseStatement(ifExpressions, thenStatementLists, elseStatementList)


    # Visit a parse tree produced by IECSTGrammarParser#variable.
    def visitVariable(self, ctx:IECSTGrammarParser.VariableContext):
        if ctx.name.text not in self.varDecs.keys():
            raise ValueError('Could not find variable')
        return self.varDecs[ctx.name.text]


    # Visit a parse tree produced by IECSTGrammarParser#expression.
    def visitExpression(self, ctx:IECSTGrammarParser.ExpressionContext):
        xorExpressions : List[XORExpression] = []
        for xorExpression in ctx.xor_expression():
            xorExpressions.append(self.visitXor_expression(xorExpression))
        return Expression(xorExpressions)


    # Visit a parse tree produced by IECSTGrammarParser#xor_expression.
    def visitXor_expression(self, ctx:IECSTGrammarParser.Xor_expressionContext):
        andExpressions : List[ANDExpression] = []
        for andExpression in ctx.and_expression():
            andExpressions.append(self.visitAnd_expression(andExpression))
        return XORExpression(andExpressions)


    # Visit a parse tree produced by IECSTGrammarParser#and_expression.
    def visitAnd_expression(self, ctx:IECSTGrammarParser.And_expressionContext):
        comparisons : List[Comparison] = []
        for comparison in ctx.comparison():
            comparisons.append(self.visitComparison(comparison))
        return ANDExpression(comparisons)


    # Visit a parse tree produced by IECSTGrammarParser#comparison.
    def visitComparison(self, ctx:IECSTGrammarParser.ComparisonContext):
        equExpressions : List[EQUExpression] = []
        equOperators : List[EQUOperator] = []
        for i in range(len(ctx.equ_expression())):
            equExpressions.append(self.visitEqu_expression(ctx.equ_expression()[i]))
            # Only add operator if more than one expression exists.
            if i > 0:
                equOperators.append(self.visitEqu_operator(ctx.equ_operator()[(i-1)]))
        return Comparison(equExpressions, equOperators)


    # Visit a parse tree produced by IECSTGrammarParser#equ_expression.
    def visitEqu_expression(self, ctx:IECSTGrammarParser.Equ_expressionContext):
        addExpressions : List[ADDExpression] = []
        comparisonOperators : List[ComparisonOperator] = []
        for i in range(len(ctx.add_expression())):
            addExpressions.append(self.visitAdd_expression(ctx.add_expression()[i]))
            # Only add operator if more than one expression exists.
            if i > 0:
                comparisonOperators.append(self.visitComparison_operator(ctx.comparison_operator()[(i-1)]))
        return EQUExpression(addExpressions, comparisonOperators)


    # Visit a parse tree produced by IECSTGrammarParser#equ_operator.
    def visitEqu_operator(self, ctx:IECSTGrammarParser.Equ_operatorContext):
        if ctx.getText() == "=":
            return EqualsOperator()
        elif ctx.getText() == "<>":
            return NotEqualOperator()
        else:
            raise ValueError('Invalid equ_operator')


    # Visit a parse tree produced by IECSTGrammarParser#comparison_operator.
    def visitComparison_operator(self, ctx:IECSTGrammarParser.Comparison_operatorContext):
        if ctx.getText() == ">":
            return GreaterThanOperator()
        elif ctx.getText() == "<":
            return LessThanOperator()
        elif ctx.getText() == ">=":
            return GreaterThanOrEqualOperator()
        elif ctx.getText() == "<=":
            return LessThanOrEqualOperator()
        else:
            raise ValueError('Invalid add_operator')


    # Visit a parse tree produced by IECSTGrammarParser#add_expression.
    def visitAdd_expression(self, ctx:IECSTGrammarParser.Add_expressionContext):
        terms : List[Term] = []
        addOperators : List[ADDOperator] = []
        for i in range(len(ctx.term())):
            terms.append(self.visitTerm(ctx.term()[i]))
            # Only add operator if more than one expression exists.
            if i > 0:
                addOperators.append(self.visitAdd_operator(ctx.add_operator()[(i-1)]))
        return ADDExpression(terms, addOperators)


    # Visit a parse tree produced by IECSTGrammarParser#add_operator.
    def visitAdd_operator(self, ctx:IECSTGrammarParser.Add_operatorContext):
        if ctx.getText() == "+":
            return PlusOperator()
        elif ctx.getText() == "-":
            return MinusOperator()
        else:
            raise ValueError('Invalid add_operator')


    # Visit a parse tree produced by IECSTGrammarParser#term.
    def visitTerm(self, ctx:IECSTGrammarParser.TermContext):
        powerExpressions : List[PowerExpression] = []
        multiplyOperators : List[MultiplyOperator] = []
        for i in range(len(ctx.power_expression())):
            powerExpressions.append(self.visitPower_expression(ctx.power_expression()[i]))
            # Only add operator if more than one expression exists.
            if i > 0:
                multiplyOperators.append(self.visitMultiply_operator(ctx.multiply_operator()[(i-1)]))
        return Term(powerExpressions, multiplyOperators)


    # Visit a parse tree produced by IECSTGrammarParser#multiply_operator.
    def visitMultiply_operator(self, ctx:IECSTGrammarParser.Multiply_operatorContext):
        if ctx.getText() == "*":
            return MultiplyOperator()
        elif ctx.getText() == "/":
            return DivideOperator()
        else:
            raise ValueError('Invalid add_operator')


    # Visit a parse tree produced by IECSTGrammarParser#power_expression.
    def visitPower_expression(self, ctx:IECSTGrammarParser.Power_expressionContext):
        unaryExpressions : List[UnaryExpression] = []
        for unaryExpression in ctx.unary_expression():
            unaryExpressions.append(self.visitUnary_expression(unaryExpression))
        return PowerExpression(unaryExpressions)


    # Visit a parse tree produced by IECSTGrammarParser#unary_expression.
    def visitUnary_expression(self, ctx:IECSTGrammarParser.Unary_expressionContext):
        unaryOperator : UnaryOperator = self.visitUnary_operator(ctx.unary_operator())
        primaryExpression : PrimaryExpression = self.visitPrimary_expression(ctx.primary_expression())
        return UnaryExpression(unaryOperator, primaryExpression)


    # Visit a parse tree produced by IECSTGrammarParser#unary_operator.
    def visitUnary_operator(self, ctx:IECSTGrammarParser.Unary_operatorContext):
        if ctx is None:
            return None
        if ctx.getText() == "-":
            return  NegateOperator()
        elif ctx.getText() == "NOT":
            return LogicalNegateOperator()
        else:
            raise ValueError('Invalid unary operator')


    # Visit a parse tree produced by IECSTGrammarParser#primary_expression.
    def visitPrimary_expression(self, ctx:IECSTGrammarParser.Primary_expressionContext):
        if ctx.expression() is not None:
            expr : Expression = self.visitExpression(ctx.expression())
            return PrimaryExpressionExpression(expr)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#literal.
    def visitLiteral(self, ctx:IECSTGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#boolean_literal.
    def visitBoolean_literal(self, ctx:IECSTGrammarParser.Boolean_literalContext):
        if ctx.getText() == "TRUE":
            return TRUE()
        elif ctx.getText() == "FALSE":
            return FALSE()
        else:
            raise ValueError('Invalid boolean literal')

    # Visit a parse tree produced by IECSTGrammarParser#numeric_literal.
    def visitNumeric_literal(self, ctx:IECSTGrammarParser.Numeric_literalContext):
        if ctx.Floating_point_literal() is not None:
            return FloatingPointLiteral(float(ctx.FloatingPointLiteral().getText()))
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#integer_literal.
    def visitInteger_literal(self, ctx:IECSTGrammarParser.Integer_literalContext):
        return IntegerLiteral(int(ctx.getText()))



del IECSTGrammarParser