// 2211363
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

// ! -------------------------- Lexical structure ----------------------- 

// TODO KeyWord
IF          : 'if' ;
ELSE        : 'else' ;
FOR         : 'for' ;
RETURN      : 'return' ;
FUNC        : 'func' ;
TYPE        : 'type' ;
STRUCT      : 'struct' ;
INTERFACE   : 'interface' ;
STRING      : 'string' ;
INT         : 'int' ;
FLOAT       : 'float' ;
BOOLEAN     : 'boolean' ;
CONST       : 'const' ;
VAR         : 'var' ;
CONTINUE    : 'continue' ;
BREAK       : 'break' ;
RANGE       : 'range' ;
NIL         : 'nil' ;
TRUE        : 'true' ;
FALSE       : 'false' ;

// TODO Operators
PLUS       : '+' ;
MINUS      : '-' ;
MUL        : '*' ;
DIV        : '/' ;
MOD        : '%' ;
EQUAL      : '==' ;
NOTEQUAL   : '!=' ;
LE         : '<=' ;
GE         : '>=' ;
LT         : '<' ;
GT         : '>' ;
AND        : '&&';
OR         : '||';
NOT        : '!' ;
PLUSEQ     : '+=' ;
MINUSEQ    : '-=' ;
MULEQ      : '*=' ;
DIVEQ      : '/=' ;
MODEQ      : '%=' ;
COLONEQ    : ':=' ; 
ASSIGN     : '=' ;
DOT        : '.' ;

// TODO Separators
LPAREN     : '(' ;
RPAREN     : ')' ;
LBRACE     : '{' ;
RBRACE     : '}' ;
LBRACK     : '[' ;
RBRACK     : ']' ;
COMMA      : ',' ;
SEMI       : ';' ;

// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// TODO Literal 
DECIMAL_LIT: '0' | [1-9][0-9]*;
BINARY_LIT: ('0b' [01]+) | ('0B' [01]+);
OCTAL_LIT: ('0o' [0-7]+) | ('0O' [0-7]+);
HEXADECIMAL_LIT: ('0x' [0-9a-fA-F]+) | ('0X' [0-9a-fA-F]+);

fragment EXP: [eE] [+-]? [0-9]+;
FLOAT_LIT: [0-9]+ '.' [0-9]* EXP? | '.' [0-9]+ EXP? | [0-9]+ EXP;

STRING_LIT: '"' (~["\\] | '\\' ["ntr"\\])* '"';
BOOLEAN_LIT: 'true' | 'false';
NIL_LIT: 'nil';

// TODO SKIP
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' (MULTI_LINE_COMMENT | .)*? '*/' -> skip;
WS: [ \t\r\n\f]+ -> skip;

// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~["\\] | '\\' ["ntr"\\])* (EOF | '\n')
{
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

fragment VALID_ESCAPES: 'n' | 't' | 'r' | '"' | '\\';

IllegalEscapeInString: '"' (~["\\] | '\\' ~[VALID_ESCAPES])*
{
    for i in range(1, len(self.text)-1):
        if self.text[i] == '\\' and self.text[i+1] not in VALID_ESCAPES:
            raise IllegalEscapeInString(self.text[1:i+2])
};
//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: statement+ EOF;

//  Statements
statement: (declaration_statement | call_statement);
declaration_statement: INT ID ASSIGNI expression COMCOMMA;
call_statement: PRINT LP expression RP COMCOMMA;

// Expression
expression: expression1 ADD expression | expression1;
expression1: ID | INT_LIT;

// //! -------------------------- end  parser structure ----------------------- //