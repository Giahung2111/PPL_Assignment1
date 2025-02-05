# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3J")
        buf.write("/\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\2\3\2\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6+\n\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3")
        buf.write("\4\2\65\65JJ\2+\2\17\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2\2")
        buf.write("\b\37\3\2\2\2\n*\3\2\2\2\f,\3\2\2\2\16\20\5\4\3\2\17\16")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22")
        buf.write("\23\3\2\2\2\23\24\7\2\2\3\24\3\3\2\2\2\25\30\5\6\4\2\26")
        buf.write("\30\5\b\5\2\27\25\3\2\2\2\27\26\3\2\2\2\30\5\3\2\2\2\31")
        buf.write("\32\7\f\2\2\32\33\7\65\2\2\33\34\7D\2\2\34\35\5\n\6\2")
        buf.write("\35\36\7E\2\2\36\7\3\2\2\2\37 \7F\2\2 !\7G\2\2!\"\5\n")
        buf.write("\6\2\"#\7H\2\2#$\7E\2\2$\t\3\2\2\2%&\5\f\7\2&\'\7I\2\2")
        buf.write("\'(\5\n\6\2(+\3\2\2\2)+\5\f\7\2*%\3\2\2\2*)\3\2\2\2+\13")
        buf.write("\3\2\2\2,-\t\2\2\2-\r\3\2\2\2\5\21\27*")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "<INVALID>", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<='", "'>='", "'<'", "'>'", "'&&'", "'||'", 
                     "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", "':='", 
                     "'='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOTEQUAL", "LE", "GE", "LT", "GT", 
                      "AND", "OR", "NOT", "PLUSEQ", "MINUSEQ", "MULEQ", 
                      "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", "DOT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", 
                      "OCTAL_LIT", "HEXADECIMAL_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BOOLEAN_LIT", "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "IllegalEscapeInString", 
                      "ASSIGNI", "COMCOMMA", "PRINT", "LP", "RP", "ADD", 
                      "INT_LIT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration_statement = 2
    RULE_call_statement = 3
    RULE_expression = 4
    RULE_expression1 = 5

    ruleNames =  [ "program", "statement", "declaration_statement", "call_statement", 
                   "expression", "expression1" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    PLUS=21
    MINUS=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    NOTEQUAL=27
    LE=28
    GE=29
    LT=30
    GT=31
    AND=32
    OR=33
    NOT=34
    PLUSEQ=35
    MINUSEQ=36
    MULEQ=37
    DIVEQ=38
    MODEQ=39
    COLONEQ=40
    ASSIGN=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACK=47
    RBRACK=48
    COMMA=49
    SEMI=50
    ID=51
    DECIMAL_LIT=52
    BINARY_LIT=53
    OCTAL_LIT=54
    HEXADECIMAL_LIT=55
    FLOAT_LIT=56
    STRING_LIT=57
    BOOLEAN_LIT=58
    NIL_LIT=59
    SINGLE_LINE_COMMENT=60
    MULTI_LINE_COMMENT=61
    WS=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    IllegalEscapeInString=65
    ASSIGNI=66
    COMCOMMA=67
    PRINT=68
    LP=69
    RP=70
    ADD=71
    INT_LIT=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.INT or _la==MiniGoParser.PRINT):
                    break

            self.state = 17
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declaration_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.state = 19
                self.declaration_statement()
                pass
            elif token in [MiniGoParser.PRINT]:
                self.state = 20
                self.call_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGNI(self):
            return self.getToken(MiniGoParser.ASSIGNI, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMCOMMA(self):
            return self.getToken(MiniGoParser.COMCOMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = MiniGoParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(MiniGoParser.INT)
            self.state = 24
            self.match(MiniGoParser.ID)
            self.state = 25
            self.match(MiniGoParser.ASSIGNI)
            self.state = 26
            self.expression()
            self.state = 27
            self.match(MiniGoParser.COMCOMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MiniGoParser.PRINT, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def COMCOMMA(self):
            return self.getToken(MiniGoParser.COMCOMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MiniGoParser.PRINT)
            self.state = 30
            self.match(MiniGoParser.LP)
            self.state = 31
            self.expression()
            self.state = 32
            self.match(MiniGoParser.RP)
            self.state = 33
            self.match(MiniGoParser.COMCOMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.expression1()
                self.state = 36
                self.match(MiniGoParser.ADD)
                self.state = 37
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = MiniGoParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





