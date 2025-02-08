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
DECIMAL_LIT: ('0' | [1-9] [0-9]*) ;
BINARY_LIT: '0' [bB] BIN_DIGIT+ { self.text = str(int(self.text, 2)) };
OCT_LIT: '0' [oO] OCTAL_DIGIT+ { self.text = str(int(self.text, 8)) };
HEXA_LIT: '0' [xX] HEX_DIGIT+ { self.text = str(int(self.text, 16)) };
fragment HEX_DIGIT: [0-9a-fA-F];
fragment OCTAL_DIGIT: [0-7];
fragment BIN_DIGIT: [01];

fragment EXP: [eE] [+-]? ('0' | [1-9] [0-9]*);
FLOAT_LIT: DECIMALS '.' [0-9]* EXP? | '.' [0-9]+ EXP? | [0-9]+ EXP;
fragment DECIMALS: ('0' | [1-9] [0-9]*) ;

STRING_LIT: '"' (~["\\\n] | '\\' [ntr"\\] | '\'"')* '"' {self.text = self.text[1:-1]};
BOOLEAN_LIT: 'true' | 'false';
NIL_LIT: 'nil';

// TODO SKIP
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' (MULTI_LINE_COMMENT | .)*? '*/' -> skip;
WS: [ \t\r\n\f]+ -> skip;

// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\n\\"] | '\\' [ntr"\\] | '\'"')* (EOF | '\n') 
{
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2]) 
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1]) 
    else:
        raise UncloseString(self.text[1:])
};


VALID_ESCAPES: 'n' | 't' | 'r' | '"' | '\\';
ILLEGAL_ESCAPE: '"' (~["\\\n] | '\\' [ntr"\\] | '\'"')* '\\' ~[rnt'\\]
{
    VAL_ESCAPES = ['n', 't', 'r', '"', '\\']
    for i in range(1, len(self.text)-1):
        if self.text[i] == '\\' and self.text[i+1] not in VAL_ESCAPES:
            raise IllegalEscape(self.text[1:i+2])
};

//!  -------------------------- end Lexical structure ------------------- //

//! --------------------------  parser structure ----------------------- //


// declared
program: EOF;

// Literal
array_lit: '[' DECIMAL_LIT ']' typ_array '{' list_expression '}';
typ_array: 'int' | 'float' | 'boolean' | 'string' | 'struct';
list_expression: list_expr | ;
list_expr: expression COMMA list_expr | expression;

struct_lit: ID '{' list_elements '}';
list_elements: list_elem | ;
list_elem: element COMMA list_elem | element;
element: ID ':' expression;

//  Statements
// statement: (declaration_statement | call_statement);
// declaration_statement: INT ID ASSIGNI expression COMCOMMA;
// call_statement: PRINT LP expression RP COMCOMMA;

// Expression
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NOTEQUAL | LT | LE | GT | GE) expression3 | expression3;
expression3: expression3 (PLUS | MINUS ) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: expression6 (NOT | MINUS) expression5 | expression6;
expression6: expression6 (LBRACE | RBRACE | DOT) expression7 | expression7;
expression7: DECIMAL_LIT | FLOAT_LIT | STRING_LIT | BOOLEAN_LIT | NIL_LIT;


// //! -------------------------- end  parser structure -----------------------