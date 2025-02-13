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
STR         : 'str';
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
ARRAY: 'array';

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
ASSIGN_OPERATOR: COLONEQ | PLUSEQ | MINUSEQ | MULEQ | DIVEQ | MODEQ;

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
DECIMAL_LIT: (MINUS | ) ('0' | [1-9] [0-9]*) ;
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
program: statements_list EOF;


// Literal
literal: array_lit | struct_lit | DECIMAL_LIT | FLOAT_LIT | STRING_LIT | bool_lit | NIL_LIT;
bool_lit: TRUE | FALSE;
array_lit: dimension_dec_list typ LBRACE list_expression RBRACE;
dimension_dec_list: dimension_dec dimension_dec_list | dimension_dec;
dimension_dec: LBRACK DECIMAL_LIT RBRACK;

typ: INT | FLOAT | BOOLEAN | STRING | STR | STRUCT | ARRAY;
list_expression: list_expr | ;
list_expr: expression COMMA list_expr | expression;
access_array_elm: ID LBRACK DECIMAL_LIT RBRACK;

struct_lit: ID LBRACE list_elements RBRACE;
list_elements: list_elem | ;
list_elem: element COMMA list_elem | element;
element: ID ':' expression;

// // //  Statements
statements_list: statement statements_list | statement;
statement: declaration_statement | call_statement | assignment_statement | if_statement | for_statement | break_statement | continue_statement | return_statement;
//---
// Declaration statement
declaration_statement: variables | constants ;
assignment_statement: lhs ASSIGN_OPERATOR expression;
lhs: expression | access_array_elm; 

// If Statement
if_statement: ((IF | ELSE IF) expression | ELSE) LBRACE statements_list RBRACE;

// For Statement
for_statement: basic_loop | ini_con_upd_loop | range_loop;
basic_loop: FOR expression LBRACE statements_list RBRACE;
ini_con_upd_loop:FOR assignment_statement SEMI expression SEMI assignment_statement LBRACE statements_list RBRACE;
range_loop: FOR expression COMMA expression COLONEQ RANGE expression LBRACE statements_list RBRACE;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI;

call_statement: ID LPAREN list_expression RPAREN SEMI;

return_statement: RETURN expression;

// Expression
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NOTEQUAL | LT | LE | GT | GE) expression3 | expression3;
expression3: expression3 (PLUS | MINUS ) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: expression6 (NOT | MINUS) expression5 | expression6;
expression6: expression6 DOT expression7 | expression6 LBRACK expression RBRACK | expression7;
expression7: ID | literal | function_call | LPAREN expression RPAREN | access_array_elm;

// Function Call
function_call: ID LPAREN list_expression RPAREN;

// Method Call
method_call: expression DOT expression;

// // // DECLARED
// 5.1 Variables -- checked --
variables: VAR expression (typ ASSIGN expression | ASSIGN  expression  | typ) SEMI;

// 5.2 Constants
constants: CONST ID ASSIGN expression SEMI;

// 5.3 Functions 
functions: FUNC ID LPAREN paramaters_list RPAREN typ LBRACE statements_list RBRACE;
paramaters_list: paramaters | ;
paramaters: paramater COMMA paramaters | paramater;
paramater: ID typ;

// 5.4 Methods
methods: FUNC LPAREN expression expression RPAREN expression LPAREN paramaters_list RPAREN typ LBRACE statements_list RBRACE;

// // 4.6 Struct
struct: TYPE expression STRUCT LBRACE fieldname_list RBRACE;
fieldname_list: fieldname fieldname_list | fieldname;
fieldname: expression typ SEMI ;

struct_instance: ID COLONEQ ID LBRACE valueinstance_list RBRACE;
valueinstance_list: valueinstance_prime | ;
valueinstance_prime: valueinstance COMMA valueinstance_prime | valueinstance;
valueinstance: expression ':' expression;

// Accessing the fields of a struct
print_line: PUTINTLN | PUTSTRINGLN;
accessing_fields: expression;

// Modify the fields of a truct
modify_fields: expression COLONEQ expression;

// Define method for struct
define_method: FUNC LPAREN expression expression RPAREN expression LPAREN RPAREN typ LBRACE statements_list RBRACE ;

// Call method on an instance
call_instancemethod: expression;

// // 4.7 Interface type
interface: TYPE expression INTERFACE LBRACE statements_list RBRACE ;



// //! -------------------------- end  parser structure -----------------------