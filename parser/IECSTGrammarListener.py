# Generated from IECSTGrammar.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IECSTGrammarParser import IECSTGrammarParser
else:
    from IECSTGrammarParser import IECSTGrammarParser

# This class defines a complete listener for a parse tree produced by IECSTGrammarParser.
class IECSTGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by IECSTGrammarParser#configurationfile.
    def enterConfigurationfile(self, ctx:IECSTGrammarParser.ConfigurationfileContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#configurationfile.
    def exitConfigurationfile(self, ctx:IECSTGrammarParser.ConfigurationfileContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#program.
    def enterProgram(self, ctx:IECSTGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#program.
    def exitProgram(self, ctx:IECSTGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#configuration.
    def enterConfiguration(self, ctx:IECSTGrammarParser.ConfigurationContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#configuration.
    def exitConfiguration(self, ctx:IECSTGrammarParser.ConfigurationContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#resource_declaration.
    def enterResource_declaration(self, ctx:IECSTGrammarParser.Resource_declarationContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#resource_declaration.
    def exitResource_declaration(self, ctx:IECSTGrammarParser.Resource_declarationContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#single_resource_declaration.
    def enterSingle_resource_declaration(self, ctx:IECSTGrammarParser.Single_resource_declarationContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#single_resource_declaration.
    def exitSingle_resource_declaration(self, ctx:IECSTGrammarParser.Single_resource_declarationContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#task_configuration.
    def enterTask_configuration(self, ctx:IECSTGrammarParser.Task_configurationContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#task_configuration.
    def exitTask_configuration(self, ctx:IECSTGrammarParser.Task_configurationContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#task_initialization.
    def enterTask_initialization(self, ctx:IECSTGrammarParser.Task_initializationContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#task_initialization.
    def exitTask_initialization(self, ctx:IECSTGrammarParser.Task_initializationContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#interval_time.
    def enterInterval_time(self, ctx:IECSTGrammarParser.Interval_timeContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#interval_time.
    def exitInterval_time(self, ctx:IECSTGrammarParser.Interval_timeContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#time_unit.
    def enterTime_unit(self, ctx:IECSTGrammarParser.Time_unitContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#time_unit.
    def exitTime_unit(self, ctx:IECSTGrammarParser.Time_unitContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#program_configuration.
    def enterProgram_configuration(self, ctx:IECSTGrammarParser.Program_configurationContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#program_configuration.
    def exitProgram_configuration(self, ctx:IECSTGrammarParser.Program_configurationContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#var_block.
    def enterVar_block(self, ctx:IECSTGrammarParser.Var_blockContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#var_block.
    def exitVar_block(self, ctx:IECSTGrammarParser.Var_blockContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#simpleType.
    def enterSimpleType(self, ctx:IECSTGrammarParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#simpleType.
    def exitSimpleType(self, ctx:IECSTGrammarParser.SimpleTypeContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#variable_declaration.
    def enterVariable_declaration(self, ctx:IECSTGrammarParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#variable_declaration.
    def exitVariable_declaration(self, ctx:IECSTGrammarParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#program_block_body.
    def enterProgram_block_body(self, ctx:IECSTGrammarParser.Program_block_bodyContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#program_block_body.
    def exitProgram_block_body(self, ctx:IECSTGrammarParser.Program_block_bodyContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#statement_list.
    def enterStatement_list(self, ctx:IECSTGrammarParser.Statement_listContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#statement_list.
    def exitStatement_list(self, ctx:IECSTGrammarParser.Statement_listContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#statement.
    def enterStatement(self, ctx:IECSTGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#statement.
    def exitStatement(self, ctx:IECSTGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#assignment_statement.
    def enterAssignment_statement(self, ctx:IECSTGrammarParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#assignment_statement.
    def exitAssignment_statement(self, ctx:IECSTGrammarParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#if_then_else_statement.
    def enterIf_then_else_statement(self, ctx:IECSTGrammarParser.If_then_else_statementContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#if_then_else_statement.
    def exitIf_then_else_statement(self, ctx:IECSTGrammarParser.If_then_else_statementContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#variable.
    def enterVariable(self, ctx:IECSTGrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#variable.
    def exitVariable(self, ctx:IECSTGrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#expression.
    def enterExpression(self, ctx:IECSTGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#expression.
    def exitExpression(self, ctx:IECSTGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#xor_expression.
    def enterXor_expression(self, ctx:IECSTGrammarParser.Xor_expressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#xor_expression.
    def exitXor_expression(self, ctx:IECSTGrammarParser.Xor_expressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#and_expression.
    def enterAnd_expression(self, ctx:IECSTGrammarParser.And_expressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#and_expression.
    def exitAnd_expression(self, ctx:IECSTGrammarParser.And_expressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#comparison.
    def enterComparison(self, ctx:IECSTGrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#comparison.
    def exitComparison(self, ctx:IECSTGrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#equ_expression.
    def enterEqu_expression(self, ctx:IECSTGrammarParser.Equ_expressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#equ_expression.
    def exitEqu_expression(self, ctx:IECSTGrammarParser.Equ_expressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#equ_operator.
    def enterEqu_operator(self, ctx:IECSTGrammarParser.Equ_operatorContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#equ_operator.
    def exitEqu_operator(self, ctx:IECSTGrammarParser.Equ_operatorContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#comparison_operator.
    def enterComparison_operator(self, ctx:IECSTGrammarParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#comparison_operator.
    def exitComparison_operator(self, ctx:IECSTGrammarParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#add_expression.
    def enterAdd_expression(self, ctx:IECSTGrammarParser.Add_expressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#add_expression.
    def exitAdd_expression(self, ctx:IECSTGrammarParser.Add_expressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#add_operator.
    def enterAdd_operator(self, ctx:IECSTGrammarParser.Add_operatorContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#add_operator.
    def exitAdd_operator(self, ctx:IECSTGrammarParser.Add_operatorContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#term.
    def enterTerm(self, ctx:IECSTGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#term.
    def exitTerm(self, ctx:IECSTGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#multiply_operator.
    def enterMultiply_operator(self, ctx:IECSTGrammarParser.Multiply_operatorContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#multiply_operator.
    def exitMultiply_operator(self, ctx:IECSTGrammarParser.Multiply_operatorContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#power_expression.
    def enterPower_expression(self, ctx:IECSTGrammarParser.Power_expressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#power_expression.
    def exitPower_expression(self, ctx:IECSTGrammarParser.Power_expressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#unary_expression.
    def enterUnary_expression(self, ctx:IECSTGrammarParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#unary_expression.
    def exitUnary_expression(self, ctx:IECSTGrammarParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#unary_operator.
    def enterUnary_operator(self, ctx:IECSTGrammarParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#unary_operator.
    def exitUnary_operator(self, ctx:IECSTGrammarParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#primary_expression.
    def enterPrimary_expression(self, ctx:IECSTGrammarParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#primary_expression.
    def exitPrimary_expression(self, ctx:IECSTGrammarParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#literal.
    def enterLiteral(self, ctx:IECSTGrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#literal.
    def exitLiteral(self, ctx:IECSTGrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#boolean_literal.
    def enterBoolean_literal(self, ctx:IECSTGrammarParser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#boolean_literal.
    def exitBoolean_literal(self, ctx:IECSTGrammarParser.Boolean_literalContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#numeric_literal.
    def enterNumeric_literal(self, ctx:IECSTGrammarParser.Numeric_literalContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#numeric_literal.
    def exitNumeric_literal(self, ctx:IECSTGrammarParser.Numeric_literalContext):
        pass


    # Enter a parse tree produced by IECSTGrammarParser#integer_literal.
    def enterInteger_literal(self, ctx:IECSTGrammarParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by IECSTGrammarParser#integer_literal.
    def exitInteger_literal(self, ctx:IECSTGrammarParser.Integer_literalContext):
        pass


