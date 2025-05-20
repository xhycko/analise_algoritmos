### U1 - Aula 3 - 22/05/2025 - Branch and Bounds, busca

#### (2,0) Busca em Vetor

Compare o desempenho, com o vetor de tamanho 10.000.000. Se quiser, use outro método de busca da linguagem.

Faça commit e push da sua implementação, junto com análise de desempenho e os arquivos na pasta unidade1\exercicio2 no seu repositório da disciplina.

Em python

```python
vetor = [71, 21, 33, 5, 84]

if 33 in vetor:
    print("30 está na lista")
else:
    print("30 não está na lista")
```

Em Java

```java
public class BuscaVetor {
    public static void main(String[] args) {
        int[] vetor = {71, 21, 33, 5, 84};
        boolean encontrado = false;

        for (int i = 0; i < vetor.length; i++)
            if (vetor[i] == 33) {
                System.out.println(33 + " está na lista");
                encontrado = true;
            }

        if (!encontrado)
            System.out.println(33 + " não está na lista");
   }
}
```
