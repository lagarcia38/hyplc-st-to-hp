# Generated from IECSTGrammar.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IECSTGrammarParser import IECSTGrammarParser
else:
    from IECSTGrammarParser import IECSTGrammarParser

# This class defines a complete generic visitor for a parse tree produced by IECSTGrammarParser.

class IECSTGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IECSTGrammarParser#configurationfile.
    def visitConfigurationfile(self, ctx:IECSTGrammarParser.ConfigurationfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#program.
    def visitProgram(self, ctx:IECSTGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#configuration.
    def visitConfiguration(self, ctx:IECSTGrammarParser.ConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#resource_declaration.
    def visitResource_declaration(self, ctx:IECSTGrammarParser.Resource_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#single_resource_declaration.
    def visitSingle_resource_declaration(self, ctx:IECSTGrammarParser.Single_resource_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#task_configuration.
    def visitTask_configuration(self, ctx:IECSTGrammarParser.Task_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#task_initialization.
    def visitTask_initialization(self, ctx:IECSTGrammarParser.Task_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#interval_time.
    def visitInterval_time(self, ctx:IECSTGrammarParser.Interval_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#time_unit.
    def visitTime_unit(self, ctx:IECSTGrammarParser.Time_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#program_configuration.
    def visitProgram_configuration(self, ctx:IECSTGrammarParser.Program_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#var_block.
    def visitVar_block(self, ctx:IECSTGrammarParser.Var_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#simpleType.
    def visitSimpleType(self, ctx:IECSTGrammarParser.SimpleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#variable_declaration.
    def visitVariable_declaration(self, ctx:IECSTGrammarParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#program_block_body.
    def visitProgram_block_body(self, ctx:IECSTGrammarParser.Program_block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#statement_list.
    def visitStatement_list(self, ctx:IECSTGrammarParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#statement.
    def visitStatement(self, ctx:IECSTGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#assignment_statement.
    def visitAssignment_statement(self, ctx:IECSTGrammarParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#if_then_else_statement.
    def visitIf_then_else_statement(self, ctx:IECSTGrammarParser.If_then_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#variable.
    def visitVariable(self, ctx:IECSTGrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#expression.
    def visitExpression(self, ctx:IECSTGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#xor_expression.
    def visitXor_expression(self, ctx:IECSTGrammarParser.Xor_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#and_expression.
    def visitAnd_expression(self, ctx:IECSTGrammarParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#comparison.
    def visitComparison(self, ctx:IECSTGrammarParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#equ_expression.
    def visitEqu_expression(self, ctx:IECSTGrammarParser.Equ_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#comparison_operator.
    def visitComparison_operator(self, ctx:IECSTGrammarParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#add_expression.
    def visitAdd_expression(self, ctx:IECSTGrammarParser.Add_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#add_operator.
    def visitAdd_operator(self, ctx:IECSTGrammarParser.Add_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#term.
    def visitTerm(self, ctx:IECSTGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#multiply_operator.
    def visitMultiply_operator(self, ctx:IECSTGrammarParser.Multiply_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#power_expression.
    def visitPower_expression(self, ctx:IECSTGrammarParser.Power_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#unary_expression.
    def visitUnary_expression(self, ctx:IECSTGrammarParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#unary_operator.
    def visitUnary_operator(self, ctx:IECSTGrammarParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#primary_expression.
    def visitPrimary_expression(self, ctx:IECSTGrammarParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#literal.
    def visitLiteral(self, ctx:IECSTGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#boolean_literal.
    def visitBoolean_literal(self, ctx:IECSTGrammarParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#numeric_literal.
    def visitNumeric_literal(self, ctx:IECSTGrammarParser.Numeric_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IECSTGrammarParser#integer_literal.
    def visitInteger_literal(self, ctx:IECSTGrammarParser.Integer_literalContext):
        return self.visitChildren(ctx)



del IECSTGrammarParser