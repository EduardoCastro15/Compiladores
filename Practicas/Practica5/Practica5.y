%{
#include <stdio.h>
extern int yylex(void);
%}

%union{
	int entero;
	double flotante;
}

%token <entero> ENTERO
%token <flotante> RACIONAL
%token MOD

%type <entero> exp term
%type <flotante> expf termf

%left '+' '-'
%left '*' '/'
%left NEGATIVE
%left MOD

%%

input:
        | input line             
;

line:     '\n'
        | exp '\n'  				{ printf ("\tresultado: %d\n", $1); }
        | expf '\n'  				{ printf ("\tresultado: %.8g\n", $1); }
;

exp:  term							{ $$ = $1; 			}
    |     exp '+' exp				{ $$ = $1 + $3;    	}
    |     exp '-' exp				{ $$ = $1 - $3;    	}
    |     exp '*' exp				{ $$ = $1 * $3;    	}
    |     exp '/' exp				{ $$ = $1 / $3;    	}
    |     MOD '(' exp ',' exp ')'   { $$ = $3 % $5; 	}
    |     '-' exp  %prec NEGATIVE	{ $$ = - $2;       	}
;

expf:  termf						{ $$ = $1;         	}
    |     expf '+' expf				{ $$ = $1 + $3;    	}
    |     expf '+' exp				{ $$ = $1 + $3;    	}
    |     exp  '+' expf				{ $$ = $1 + $3;    	}
    |     expf '-' expf				{ $$ = $1 - $3;    	}
    |     expf '-' exp				{ $$ = $1 - $3;    	}
    |     exp  '-' expf				{ $$ = $1 - $3;    	}
    |     expf '*' expf				{ $$ = $1 * $3;    	}
    |     expf '*' exp 				{ $$ = $1 * $3;    	}
    |     exp  '*' expf				{ $$ = $1 * $3;    	}
    |     expf '/' expf				{ $$ = $1 / $3;    	}
    |     expf '/' exp				{ $$ = $1 / $3;    	}
    |     exp  '/' expf				{ $$ = $1 / $3;    	}
    |     '-' expf  %prec NEGATIVE	{ $$ = - $2;       	}
;

term:     ENTERO					{ $$ = $1;         	}
    |     '(' exp ')'				{ $$ = $2;        	}
;

termf:     RACIONAL					{ $$ = $1;         	}
    |     '(' expf ')'				{ $$ = $2;         	}
;

%%

#include <stdlib.h>

int yyerror(char *s){
    printf("--%s--\n", s);
    return 0;
}

int yywrap(){
	return 1;
}

int main(){
	yyparse();
	return 0;
}

