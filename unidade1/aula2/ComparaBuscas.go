package main

import (
	"fmt"
	"sort"
	"time"
)

// Implementação da busca linear
func buscaLinear(arr []int, alvo int) int {
	for i := 0; i < len(arr); i++ {
		if arr[i] == alvo {
			return i // Retorna o índice onde o elemento foi encontrado
		}
	}
	return -1 // Retorna -1 se o elemento não for encontrado
}

// Implementação da busca binária (usando a função pronta do Go)
func buscaBinaria(arr []int, alvo int) int {
	return sort.Search(len(arr), func(i int) bool {
		return arr[i] >= alvo
	}) - 1 // Retorna o índice ou -1 caso não encontre
}

func main() {
	// Gerando um array maior com 10 mil elementos
	tamanho := 1000000
	arr := make([]int, tamanho)
	for i := 0; i < tamanho; i++ {
		arr[i] = i * 2 // Populando o array com números pares
	}
	alvo := 999998 // Elemento que estamos procurando

	// Medindo o tempo da busca linear
	inicioLinear := time.Now()
	resultadoLinear := buscaLinear(arr, alvo)
	tempoLinear := time.Since(inicioLinear)

	// Medindo o tempo da busca binária
	inicioBinario := time.Now()
	resultadoBinario := buscaBinaria(arr, alvo)
	tempoBinario := time.Since(inicioBinario)

	// Exibindo os resultados
	if resultadoLinear >= 0 {
		fmt.Printf("Busca Linear: Elemento encontrado no índice %d\n", resultadoLinear)
	} else {
		fmt.Println("Busca Linear: Elemento não encontrado")
	}
	fmt.Printf("Tempo de execução da busca linear: %v\n", tempoLinear)

	if resultadoBinario >= 0 {
		fmt.Printf("Busca Binária: Elemento encontrado no índice %d\n", resultadoBinario)
	} else {
		fmt.Println("Busca Binária: Elemento não encontrado")
	}
	fmt.Printf("Tempo de execução da busca binária: %v\n", tempoBinario)
}
