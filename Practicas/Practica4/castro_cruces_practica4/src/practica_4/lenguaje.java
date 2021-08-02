package practica_4;

public class lenguaje {
    String cadena;
    int i = 0;
    int TAM;
    
    //Inicia la validación de la cadena de cadena
    public void validad(String entrada){
        cadena = entrada;
        TAM = cadena.length();
        System.out.println("La cadena a validar es: " + cadena);
        E();
    }

    public void E(){
        T();
        Z();
    }

    public void T(){
        if(cadena.charAt(i) == 'a') Check('a');
        else{
            System.out.println("No pertenece a la gramatica");
            System.exit(0);
        }
    }

    public void Z(){
        if(cadena.charAt(i) == '+'){
            Check('+');
            T();
            Z();
        }
        else if(cadena.charAt(i) == 'e') Check('e');
        else{
            R();
        }
    }

    public void R(){
        if(cadena.charAt(i) == '-'){
            Check('-');
            T();
            Z();
        }
        else if(cadena.charAt(i) == 'e') Check('e');
        else{
            System.out.println("No pertenece a la gramatica");
            System.exit(0);
        }
    }

    public void Check(char elemento){
        if(cadena.charAt(i) == elemento) i++;   
        if(TAM == i){
            System.out.println("Si pertenece a la gramatica");
            System.exit(0);
        }
    }
}