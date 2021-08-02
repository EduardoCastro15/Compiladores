%{
#include <stdio.h>
#include "Practica5.tab.h"

extern YYSTYPE yylval;
%}

NUM [0-9]+

%%

{NUM}                   {
                        printf("Numero entero sin signo %s\n", yytext);
                        yylval.entero = atoi(yytext);
                        return (ENTERO);
                        }

("-")({NUM})            {
                        printf("Numero entero con signo %s\n", yytext);
                        yylval.entero = atoi(yytext);
                        return (ENTERO);
                        }

({NUM})(".")({NUM})     {
                        printf("Numero flotante sin signo %s\n",yytext);
                        yylval.flotante = strtod(yytext, NULL);
                        return (RACIONAL);
                        }

("-")({NUM})(".")({NUM})     {
                        printf("Numero flotante con signo %s\n",yytext);
                        yylval.flotante = strtod(yytext, NULL);
                        return (RACIONAL);
                        }

"+"|"*"|"/"         {
                        printf("Signo op\n");
                        return (yytext[0]);
                        }

"("|")"                 {
                        printf("Signo parentesis\n");
                        return (yytext[0]);
                        }

","                     {
                        printf("Coma\n");
                        return (yytext[0]);
                        }

[Mm][Oo][Dd]            {
                        printf("Modulo\n");
                        return MOD;
                        }

"\n"                     {
                        printf("Salto de linea\n");
                        return (yytext[0]);
                        }

%%
