public class Troco {
    public static void main(String[] args) {
        //quero saber quantas cédulas foram dadas para esse troco
        int[] cedulasDisponiveis = {?}; //9,6,1?
        int trocoPara = ?; //12?
        int[] cedulasUsadas = new int[cedulasDisponiveis.length];

        for (int i = 0; i < cedulasDisponiveis.length; i++) {
            //cedulasUsadas[i]...
            ///trocoPara...
        }

        System.out.println("Cédulas usadas:");
        for (int i = 0; i < cedulasDisponiveis.length; i++) {
            System.out.println("R$ "+ cedulasDisponiveis[i] + ",00 == " + cedulasUsadas[i]);
        }
    }
}