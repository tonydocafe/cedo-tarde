# cedo-tarde
Este script é utilizado para calcular os tempos mais cedo e mais tarde em que cada tarefa de um projeto pode começar e terminar, respectivamente, sem atrasar o projeto. 
Ele também identifica o caminho crítico, que é a sequência de tarefas que determina a duração total do projeto
#### Biblioteca 
NetworkX, utilizada em python para manipulção de grafos 

## Funções 

### calcular_tempo_mais_cedo
Esta função calcula o tempo mais cedo em que cada tarefa (ou nó) pode começar.
A ordem topológica garante que um nó seja processado somente depois de seus predecessores.
O tempo mais cedo é determinado pelo maior tempo de início possível entre todos os predecessores mais o tempo necessário para a tarefa.
###### Cálculo do Tempo Mais Cedo:
- Para cada nó, inicializa-se o tempo mais cedo como 0.
- Para cada predecessor do nó, calcula-se o tempo mais cedo possível considerando o tempo mais cedo do predecessor e a duração da tarefa (aresta) entre o predecessor e o nó atual.
- O tempo mais cedo do nó atual é o máximo desses valores.
- Resultado: Um dicionário tempo_cedo com o tempo mais cedo calculado para cada nó.

### calcular_tempo_mais_tarde
Esta função calcula o tempo mais tarde em que cada tarefa pode terminar sem atrasar o projeto. 
Começa definindo todos os tempos como infinito. O tempo mais tarde do último nó é definido como seu tempo mais cedo. 
Depois, percorre os nós em ordem topológica invertida para ajustar os tempos mais tarde com base nos sucessores.
###### Cálculo do Tempo Mais Tarde:
- Percorre os nós em ordem topológica invertida (do fim para o início).
- Para cada sucessor do nó, calcula-se o tempo mais tarde possível considerando o tempo mais tarde do sucessor e a duração da tarefa (aresta) entre o nó atual e o sucessor.
- O tempo mais tarde do nó atual é o mínimo desses valores.
- Resultado: Um dicionário tempo_tarde com o tempo mais tarde calculado para cada nó.

### encontrar_caminho_critico
Esta função encontra o caminho crítico, que é o conjunto de tarefas que determinam a duração total do projeto. 
Um nó está no caminho crítico se o seu tempo mais cedo for igual ao seu tempo mais tarde.
##### Cálculo Caminho Crítico:
- Um nó está no caminho crítico se o seu tempo mais cedo é igual ao seu tempo mais tarde.
- Isso significa que não há flexibilidade no início dessa tarefa: qualquer atraso nela causará um atraso no projeto inteiro.
- Resultado: Uma lista caminho_critico com os nós que pertencem ao caminho crítico.
### main
- Lê um grafo direcionado de um arquivo chamado "tempo.txt", onde as arestas têm um atributo 'tempo'.
- Chama as funções calcular_tempo_mais_cedo e calcular_tempo_mais_tarde para obter os tempos mais cedo e mais tarde de cada nó.
- Chama a função encontrar_caminho_critico para determinar o caminho crítico.
- Imprime os tempos mais cedo e mais tarde de cada nó.
- Imprime o caminho crítico.


