%{ 
      // #include <math.h> 
%}

Digito          [0-9]
Variable        [_a-zA-Z][-_a-z0-9A-Z]*
Decimal         [.][0-9]*
Suma            [0-9]+[+][0-9]+
Resta           [0-9]+[-][0-9]+
Division        [0-9]+[/][0-9]+
Multiplicacion  [0-9]+[*][0-9]+

%%

"+"?{Digito}+ {
            printf( "Entero con o sin signo positivo: %s \n", yytext);
            }

"-"{Digito}+ {
            printf( "Entero con signo negativo: %s\n", yytext);
            }

"+"?{Digito}+{Decimal}* {
            printf( "Decimal con signo positivo: %s\n", yytext);
            }

"-"+{Digito}+{Decimal}* {
            printf( "Decimal con signo negativo: %s\n", yytext);
            }

"+"?"-"?{Digito}+{Decimal}*"^""+"?{Digito}+ {
            printf( "Potencia con signo positivo: %s\n", yytext);
            }

"+"?"-"?{Digito}+{Decimal}*"^""-"{Digito}+ {
            printf( "Potencia con signo negativo: %s\n", yytext);
            }


{Variable}        printf( "Variable: %s\n", yytext );
{Suma}        printf( "Suma: %s\n", yytext );
{Resta}        printf( "Resta: %s\n", yytext );
{Division}        printf( "Division: %s\n", yytext );
{Multiplicacion}        printf( "Multiplicacion: %s\n", yytext );

"MOD("{Digito}+")" {
            printf( "MOD: %s \n", yytext);
            }



"+"|"-"|"*"|"/"   printf( "Operador: %s\n", yytext );

"{"[^}\n]*"}"     /*elimina una linea de comentarios */

[ \t\n]+          /*Elimina espacios en blanco */

.           printf( "Caracter no valido: %s\n", yytext );

