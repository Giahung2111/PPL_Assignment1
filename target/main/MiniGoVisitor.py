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


    # Visit a parse tree produced by MiniGoParser#type_array.
    def visitType_array(self, ctx:MiniGoParser.Type_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit.
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_dec_list.
    def visitDimension_dec_list(self, ctx:MiniGoParser.Dimension_dec_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_dec.
    def visitDimension_dec(self, ctx:MiniGoParser.Dimension_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_struct.
    def visitType_struct(self, ctx:MiniGoParser.Type_structContext):
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


    # Visit a parse tree produced by MiniGoParser#access_array_elm.
    def visitAccess_array_elm(self, ctx:MiniGoParser.Access_array_elmContext):
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


    # Visit a parse tree produced by MiniGoParser#nullable_statements_list.
    def visitNullable_statements_list(self, ctx:MiniGoParser.Nullable_statements_listContext):
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


    # Visit a parse tree produced by MiniGoParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_loop.
    def visitBasic_loop(self, ctx:MiniGoParser.Basic_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ini_con_upd_loop.
    def visitIni_con_upd_loop(self, ctx:MiniGoParser.Ini_con_upd_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_loop.
    def visitRange_loop(self, ctx:MiniGoParser.Range_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
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


    # Visit a parse tree produced by MiniGoParser#typ_list.
    def visitTyp_list(self, ctx:MiniGoParser.Typ_listContext):
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


    # Visit a parse tree produced by MiniGoParser#struct_elements_list.
    def visitStruct_elements_list(self, ctx:MiniGoParser.Struct_elements_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_elements.
    def visitStruct_elements(self, ctx:MiniGoParser.Struct_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_list.
    def visitMethod_list(self, ctx:MiniGoParser.Method_listContext):
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


    # Visit a parse tree produced by MiniGoParser#accessing_struct_fields.
    def visitAccessing_struct_fields(self, ctx:MiniGoParser.Accessing_struct_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#modify_fields.
    def visitModify_fields(self, ctx:MiniGoParser.Modify_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#define_method.
    def visitDefine_method(self, ctx:MiniGoParser.Define_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_instancemethod.
    def visitCall_instancemethod(self, ctx:MiniGoParser.Call_instancemethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface.
    def visitInterface(self, ctx:MiniGoParser.InterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_list.
    def visitInterface_method_list(self, ctx:MiniGoParser.Interface_method_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return self.visitChildren(ctx)



del MiniGoParser