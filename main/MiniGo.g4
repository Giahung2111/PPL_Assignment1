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

// ! -------------------------- Lexical structure ----------------------- ;

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
DECIMAL: '0' | [1-9][0-9]*;
BINARY: ('0b' [01]+) | ('0B' [01]+);
OCTAL: ('0o' [0-7]+) | ('0O' [0-7]+);
HEXADECIMAL: ('0x' [0-9a-fA-F]+) | ('0X' [0-9a-fA-F]+);

fragment EXP: [eE] [+-]? [0-9]+;
FLOAT: [0-9]+ '.' [0-9]* EXP? | '.' [0-9]+ EXP? | [0-9]+ EXP;

STRING: '"' (~["\\] | '\\' ["ntr"\\])* '"';
BOOLEAN: 'true' | 'false';
NIL: 'nil';

// TODO SKIP
COMMENTS: '##' ~[\n]* -> skip; // Comments
WS: [ \t\r\f\b\n]+ -> skip; // skip spaces, tabs

// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

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