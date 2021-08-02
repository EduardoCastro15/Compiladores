package practica_4;

public class Practica_4 {
	/*
	E -> TZ
	T -> a
	Z -> +TZ | e | R
	R -> -TZ | e
    */
    public static void main(String[] args) {
        String cadena = "a-a+a-a+a-a+a-a+a-a+a-a+ae";
        System.out.println("_____Analizador Sintactico de Descenso Recursivo_____");
        lenguaje obt = new lenguaje();
        obt.validad(cadena);
    }
}