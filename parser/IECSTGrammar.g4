/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/

grammar IECSTGrammar;

configurationfile
: program configuration
;

program:
'PROGRAM' name=ID
var_blocks+=var_block*
program_block_body
'END_PROGRAM';

configuration:
'CONFIGURATION' name=ID
(single_resource_declaration | resource_declaration (resource_declaration)*)
'END_CONFIGURATION';

resource_declaration:
'RESOURCE' name=ID 'ON' resource_type_name
single_resource_declaration
'END_RESOURCE';

single_resource_declaration:
task_configuration ';'//|task_configuration ';' (task_configuration)*
program_configuration ';';//|program_configuration ';' (program_configuration)*

task_configuration:
'TASK' name=ID task_initialization;

task_initialization:
'(' ('SINGLE' ':=' data_source ',')? 'INTERVAL' ':=' interval_time ',' 'PRIORITY' ':=' Decimal_literal ')';

interval_time:
'T' '#' Decimal_literal time_unit;

time_unit:
's' | 'ms' | 'us';

program_configuration:
'PROGRAM' inst_name=ID 'WITH' task_name=ID ':' prog_name=ID;

var_block locals[boolean input, boolean output, boolean temp]
: ('VAR'
| { $input=true; } 'VAR_INPUT'
| { $output=true; } 'VAR_OUTPUT')
( variables+=variable_declaration* 'END_VAR');

type_rule:
name=ID #simpleType;

variable_declaration:
names+=ID (',' names+=ID)* ':' type=type_rule ;

program_block_body:
statement_list;

statement_list:
statement (';' statement)*';';

statement:
NIL | assignment_statement | if_then_else_statement;

assignment_statement:
variable ':=' expression;

if_then_else_statement:
'IF' expression 'THEN' statement_list
('ELSIF' expression 'THEN' statement_list)*
('ELSE' statement_list)?
'END_IF'

variable:
name=ID;

expression:
xor_expression ('OR' xor_expression)*;

xor_expression:
and_expression ('XOR' and_expression)*;

and_expression:
comparison (('&' | 'AND') comparison)*;

comparison:
equ_expression (('=' | '<>') equ_expression)*;

equ_expression:
add_expression (comparison_operator add_expression)*;

comparison_operator:
'<' | '>' | '<=' | '>=';

add_expression:
term (add_operator term)*;

add_operator :
'+' | '-';

term:
power_expression (multiply_operator power_expression)*;

multiply_operator:
'*' | '/';

power_expression:
unary_expression (’**’ unary_expression)*;

unary_expression:
unary_operator? primary_expression;

unary_operator: '-' | 'NOT';

primary_expression:
literal | variable | '(' expression ')';

literal:
numeric_literal | bollean_literal;

boolean_literal: 'TRUE' | 'FALSE';

numeric_literal
: '-'? integer_literal
| '-'? Floating_point_literal
;

integer_literal
: Binary_literal
| Octal_literal
| Decimal_literal
| Pure_decimal_digits
| Hexadecimal_literal
;

Binary_literal : '2#' Binary_digit Binary_literal_characters? ;
fragment Binary_digit : [01] ;
fragment Binary_literal_character : Binary_digit | '_'  ;
fragment Binary_literal_characters : Binary_literal_character+ ;

Octal_literal : '8#' Octal_digit Octal_literal_characters? ;
fragment Octal_digit : [0-7] ;
fragment Octal_literal_character : Octal_digit | '_'  ;
fragment Octal_literal_characters : Octal_literal_character+ ;

Decimal_literal        : [0-9] [0-9_]* ;
Pure_decimal_digits : [0-9]+ ;
fragment Decimal_digit : [0-9] ;
fragment Decimal_literal_character : Decimal_digit | '_'  ;
fragment Decimal_literal_characters : Decimal_literal_character+ ;

Hexadecimal_literal : '16#' Hexadecimal_digit Hexadecimal_literal_characters? ;
fragment Hexadecimal_digit : [0-9a-fA-F] ;
fragment Hexadecimal_literal_character : Hexadecimal_digit | '_'  ;
fragment Hexadecimal_literal_characters : Hexadecimal_literal_character+ ;

Floating_point_literal
: Decimal_literal Decimal_fraction? Decimal_exponent?
;

fragment Decimal_fraction : '.' Decimal_literal ;
fragment Decimal_exponent : Floating_point_e Sign? Decimal_literal ;
fragment Floating_point_e : [eE] ;
fragment Floating_point_p : [pP] ;
fragment Sign : [+\-] ;

ID: [A-Za-z][A-Za-z_0-9]*;
NIL: WS;
WS : [ \n\r\t]+ -> channel(HIDDEN) ;
Block_comment : '(*' (Block_comment|.)*? '*)' -> channel(HIDDEN) ; // nesting comments allowed
