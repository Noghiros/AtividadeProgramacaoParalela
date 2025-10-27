### Verificador de Sudoku com Threads em Python

Este projeto verifica se uma **solução de Sudoku 9x9** é válida utilizando **threads paralelas** em Python.  
Baseado no exercício proposto no livro *Fundamentos de Sistemas Operacionais* de A. Silberschatz, P. Galvin e G. Gagne (página 110).

O programa cria múltiplas threads para verificar simultaneamente:
- Todas as **linhas** do Sudoku  
- Todas as **colunas**  
- Cada uma das **9 subgrades 3x3**

No total, são **11 threads** sendo executadas em paralelo.
Exemplo de um sudoku válido utilizado no codigo:

<img width="591" height="598" alt="image" src="https://github.com/user-attachments/assets/ad5d439c-243a-4a8c-a87c-204f2b0e7f86" />
