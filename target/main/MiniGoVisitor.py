# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#bool_lit.
    def visitBool_lit(self, ctx:MiniGoParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit.
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typ.
    def visitTyp(self, ctx:MiniGoParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expr.
    def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elements.
    def visitList_elements(self, ctx:MiniGoParser.List_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elem.
    def visitList_elem(self, ctx:MiniGoParser.List_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statements_list.
    def visitStatements_list(self, ctx:MiniGoParser.Statements_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration_statement.
    def visitDeclaration_statement(self, ctx:MiniGoParser.Declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables.
    def visitVariables(self, ctx:MiniGoParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants.
    def visitConstants(self, ctx:MiniGoParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functions.
    def visitFunctions(self, ctx:MiniGoParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramaters_list.
    def visitParamaters_list(self, ctx:MiniGoParser.Paramaters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramaters.
    def visitParamaters(self, ctx:MiniGoParser.ParamatersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramater.
    def visitParamater(self, ctx:MiniGoParser.ParamaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methods.
    def visitMethods(self, ctx:MiniGoParser.MethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct.
    def visitStruct(self, ctx:MiniGoParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldname_list.
    def visitFieldname_list(self, ctx:MiniGoParser.Fieldname_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldname.
    def visitFieldname(self, ctx:MiniGoParser.FieldnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_instance.
    def visitStruct_instance(self, ctx:MiniGoParser.Struct_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#valueinstance_list.
    def visitValueinstance_list(self, ctx:MiniGoParser.Valueinstance_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#valueinstance_prime.
    def visitValueinstance_prime(self, ctx:MiniGoParser.Valueinstance_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#valueinstance.
    def visitValueinstance(self, ctx:MiniGoParser.ValueinstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#print_line.
    def visitPrint_line(self, ctx:MiniGoParser.Print_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#accessing_fields.
    def visitAccessing_fields(self, ctx:MiniGoParser.Accessing_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#modify_fields.
    def visitModify_fields(self, ctx:MiniGoParser.Modify_fieldsContext):
        return self.visitChildren(ctx)



del MiniGoParser