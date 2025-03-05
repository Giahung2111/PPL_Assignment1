// 2211363
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
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

DECIMAL_LIT: (MINUS | ) ('0' | [1-9] [0-9]*) ;
BINARY_LIT: '0' [bB] BIN_DIGIT+ ;
OCT_LIT: '0' [oO] OCTAL_DIGIT+ ;
HEXA_LIT: '0' [xX] HEX_DIGIT+;
fragment HEX_DIGIT: [0-9a-fA-F];
fragment OCTAL_DIGIT: [0-7];
fragment BIN_DIGIT: [01];


fragment EXP: [eE] [+-]? [0-9]+;
FLOAT_LIT: [0-9]+ '.' [0-9]* EXP? | '.' [0-9]+ EXP? | [0-9]+ EXP;
fragment DECIMALS: ('0' | [1-9] [0-9]*) ;

STRING_LIT: '"' (~["\\\n] | '\\' [ntr"\\] | '\'"')* '"';
BOOLEAN_LIT: 'true' | 'false';
NIL_LIT: 'nil';

// TODO SKIP
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' (MULTI_LINE_COMMENT | .)*? '*/' -> skip;
WS: [ \t\f\r]+ -> skip;
SEMICOLON_NEWLINE:
    '\r'? '\n' {
    if self.preType in {self.ID, self.DECIMAL_LIT, self.BINARY_LIT, self.OCT_LIT, self.HEXA_LIT, self.TRUE,self.FALSE, self.STRING_LIT, self.FLOAT_LIT, 
                self.RETURN, self.CONTINUE, self.BREAK,
                self.RPAREN, self.RBRACK, self.RBRACE, self.NIL }:
        self.text = ';'
    else:
        self.skip()
};

// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\n\\"] | '\\' [ntr"\\] | '\'"')* (EOF | '\n') 
{
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[0:-2]) 
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[0:-1]) 
    else:
        raise UncloseString(self.text[0:])
};


VALID_ESCAPES: 'n' | 't' | 'r' | '"' | '\\';
ILLEGAL_ESCAPE: '"' (~["\\\n] | '\\' [ntr"\\] | '\'"')* '\\' ~[rnt'\\]
{
    VAL_ESCAPES = ['n', 't', 'r', '"', '\\']
    for i in range(1, len(self.text)-1):
        if self.text[i] == '\\' and self.text[i+1] not in VAL_ESCAPES:
            raise IllegalEscape(self.text[0:])
};

//!  -------------------------- end Lexical structure ------------------- //

//! --------------------------  parser structure ----------------------- //


// declared
program: statements_list EOF;
// program: (CONST ID ASSIGN expression SEMI) EOF;


// Literal
literal: array_lit | struct_lit | DECIMAL_LIT | HEXA_LIT | OCT_LIT | BINARY_LIT | FLOAT_LIT | STRING_LIT | bool_lit | NIL;
bool_lit: TRUE | FALSE;
type_array:  dimension_dec_list typ;
array_lit: type_array LBRACE list_expression RBRACE ;
list_expression: list_expr | ;
list_expr: element_expr COMMA list_expr 
         | element_expr ;
element_expr: expression 
       | LBRACE list_expr RBRACE ;

dimension_dec_list: dimension_dec dimension_dec_list | dimension_dec;
dimension_dec: LBRACK (DECIMAL_LIT | ID) RBRACK;
type_struct: ID;
typ: INT | FLOAT | BOOLEAN | STRING | STR | type_struct | type_array;

struct_lit: ID LBRACE list_elements RBRACE;
list_elements: list_elem | ;
list_elem: element COMMA list_elem | element;
element: ID ':' expression;



// Expression
expression:  expression OR expression1 | expression1 ;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NOTEQUAL | LT | LE | GT | GE) expression3 | expression3;
expression3: expression3 (PLUS | MINUS) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (NOT | MINUS) expression5 | expression6;
expression6: expression6 LBRACK expression RBRACK | expression6 DOT ID | expression6 DOT ID LPAREN list_expression? RPAREN | expression7;
expression7: (ID | literal | function_call | LPAREN expression RPAREN);

// Function Call
function_call: ID LPAREN list_expression RPAREN;

// Method Call
method_call: expression DOT expression;

// // //  Statements
nullable_statements_list: statement nullable_statements_list | ;
statements_list: statement statements_list | statement;
statement: declaration_statement | call_statement | assignment_statement | if_statement | for_statement | break_statement | continue_statement | return_statement;
//---
// Declaration statement
declaration_statement: (variables | constants | functions | methods | struct | interface ) (SEMICOLON_NEWLINE | SEMI | );

// Assignment Statement
assignment_statement: lhs (COLONEQ | PLUSEQ | MINUSEQ | MULEQ | DIVEQ | MODEQ) expression (SEMICOLON_NEWLINE | SEMI );
// lhs: expression | access_array_elm | accessing_struct_fields; 
lhs: lhs LBRACK expression RBRACK | lhs DOT ID | ID;

// If Statement
// if_statement: ((IF | ELSE IF) expression | ELSE) LBRACE nullable_statements_list RBRACE (SEMICOLON_NEWLINE | SEMI |);
if_statement: IF LPAREN expression RPAREN LBRACE nullable_statements_list RBRACE list_else_if? else_statement? (SEMICOLON_NEWLINE | SEMI |);
list_else_if: else_if list_else_if | else_if;
else_statement: ELSE LBRACE nullable_statements_list RBRACE (SEMICOLON_NEWLINE | SEMI |);
else_if: ELSE IF LPAREN expression RPAREN LBRACE nullable_statements_list RBRACE (SEMICOLON_NEWLINE | SEMI |);

// For Statement
for_statement: basic_loop | ini_con_upd_loop | range_loop;
basic_loop: FOR expression LBRACE nullable_statements_list RBRACE (SEMICOLON_NEWLINE | SEMI |);
ini_con_upd_loop:FOR (assignment_statement | variables SEMI) expression SEMI lhs (COLONEQ | PLUSEQ | MINUSEQ | MULEQ | DIVEQ | MODEQ) expression LBRACE nullable_statements_list RBRACE (SEMICOLON_NEWLINE | SEMI |);
range_loop: FOR ID COMMA ID COLONEQ RANGE (expression) LBRACE nullable_statements_list RBRACE (SEMICOLON_NEWLINE | SEMI |);

break_statement: BREAK (SEMICOLON_NEWLINE | SEMI);

continue_statement: CONTINUE (SEMICOLON_NEWLINE | SEMI );

call_statement: (lhs DOT)? ID LPAREN list_expression? RPAREN (SEMICOLON_NEWLINE | SEMI ) ;

return_statement: RETURN (expression | ) (SEMICOLON_NEWLINE | SEMI );

// // // DECLARED
// 5.1 Variables -- checked --
variables: VAR ID (typ ASSIGN expression | ASSIGN  expression  | typ);

// 5.2 Constants
constants: CONST ID ASSIGN expression;

// 5.3 Functions 
functions: FUNC ID LPAREN paramaters_list RPAREN (typ | ) LBRACE nullable_statements_list RBRACE;
paramaters_list: paramaters | ;
paramaters: paramater COMMA paramaters | paramater;
paramater: associated_param | basic_param;
associated_param: id_list typ;
id_list: ID COMMA id_list | ID;
basic_param: ID typ;

// 5.4 Methods
methods: FUNC LPAREN ID ID RPAREN ID LPAREN paramaters_list RPAREN (typ | ) LBRACE statements_list RBRACE;

// // 4.6 Struct
struct: TYPE ID STRUCT LBRACE struct_elements_list RBRACE;
struct_elements_list: struct_elements struct_elements_list |struct_elements ;
struct_elements: fieldname_list | method_list ;
method_list: methods method_list | methods;
fieldname_list: fieldname fieldname_list | fieldname;
fieldname: ID typ (SEMICOLON_NEWLINE | SEMI ) ;

// // 4.7 Interface type
interface: TYPE ID INTERFACE LBRACE interface_method_list RBRACE;
interface_method_list: interface_method interface_method_list | interface_method; 
interface_method: ID LPAREN paramaters_list RPAREN (typ | ) (SEMICOLON_NEWLINE | SEMI);



// // //! -------------------------- End  parser structure -----------------------