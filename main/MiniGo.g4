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
PUTSTRINGLN : 'PutStringLn';
PUTINTLN    : 'PutIntLn';

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
program: statement EOF;


// Literal
literal: array_lit | struct_lit | DECIMAL_LIT | FLOAT_LIT | STRING_LIT | bool_lit | NIL_LIT;
bool_lit: TRUE | FALSE;
array_lit: LBRACK DECIMAL_LIT RBRACK typ LBRACE list_expression RBRACE;
ARRAY: 'array';
typ: INT | FLOAT | BOOLEAN | STRING | STRUCT | ARRAY;
list_expression: list_expr | ;
list_expr: expression COMMA list_expr | expression;

struct_lit: ID LBRACE list_elements RBRACE;
list_elements: list_elem | ;
list_elem: element COMMA list_elem | element;
element: ID ':' expression;

//  Statements
statements_list: ;
statement: (declaration_statement | call_statement);
declaration_statement: variables | constants ;
call_statement: ID LPAREN expression RPAREN SEMI;

// Expression
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NOTEQUAL | LT | LE | GT | GE) expression3 | expression3;
expression3: expression3 (PLUS | MINUS ) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: expression6 (NOT | MINUS) expression5 | expression6;
expression6: expression6 (LBRACE | RBRACE | DOT) expression7 | expression7;
expression7: ID | literal | function_call | LPAREN expression RPAREN;



// Function Call
function_call: ID LPAREN list_expression RPAREN;

// Method Call
method_call: ID DOT function_call;

// DECLARED
// 5.1 Variables
variables: VAR ID (typ ASSIGN expression | ASSIGN  expression  | typ) SEMI;
// 5.2 Constants
constants: CONST ID ASSIGN expression SEMI;
// 5.3 Functions and Methods
functions: FUNC ID LPAREN paramaters_list RPAREN typ LBRACE statements_list RBRACE;
paramaters_list: paramaters | ;
paramaters: paramater COMMA paramaters | paramater;
paramater: ID typ;

methods: FUNC LPAREN ID ID RPAREN ID LPAREN paramaters_list RPAREN typ LBRACE statements_list RBRACE;

// // 5.4 Struct
struct: TYPE ID STRUCT LBRACE fieldname_list RBRACE;
fieldname_list: fieldname fieldname_list | fieldname;
fieldname: ID typ SEMI ;

struct_instance: ID COLONEQ ID LBRACE valueinstance_list RBRACE;
valueinstance_list: valueinstance_prime | ;
valueinstance_prime: valueinstance COMMA valueinstance_prime | valueinstance;
valueinstance: ID ':' expression;

// Accessing the fields of a struct
print_line: PUTINTLN | PUTSTRINGLN;
accessing_fields: print_line LPAREN expression  RPAREN;

// Modify the fields of a truct
modify_fields: expression COLONEQ expression;



// //! -------------------------- end  parser structure -----------------------