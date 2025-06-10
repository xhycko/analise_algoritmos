import java.util.*;
import java.io.*;

public class ContaNomesComDicionario {
    public static void main(String[] args) {
        Map<String, Integer> contagem = new HashMap<>();

        try (BufferedReader reader = new BufferedReader(new FileReader("nomes.txt"))) {
            String linha;
            
			while ((linha = reader.readLine()) != null) {
                String nome = linha.trim();
                if (nome.isEmpty())
					continue;

                //Mapear nomes e contagem
            }
        } catch (IOException e) {
            System.err.println("Erro ao ler o arquivo: " + e.getMessage());
            return;
        }

        //Exibir os nomes e valores
    }
}
