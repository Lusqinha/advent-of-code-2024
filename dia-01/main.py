def readlines(filename) -> list[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()
    
    
def separarListas(linhas:list[str]) -> tuple[list[int], list[int]]:
    esquerda: list = []
    direita: list = []
    
    for line in linhas:
        x:list; y:list
        x, y = line.split()
        
        esquerda.append(int(x))
        direita.append(int(y))
        
    return esquerda, direita

def parte01(lines: list[str]) -> int:
    esquerda:list[int]; direita:list[int]
    
    esquerda, direita = separarListas(lines)
        
    gap:list[int] = []
    
    for i in range(len(esquerda)):
        line_diff:int = (sorted(esquerda)[i] - sorted(direita)[i])
        gap.append(abs(line_diff))
            
    return sum(gap)

def parte02(lines: list[str]) -> int:
    
    esquerda:list[int]; direita:list[int]
    
    esquerda, direita = separarListas(lines)

    lista_pontuacao: list[int] = []

    for i in range(len(esquerda)):
        ocorrencias: int = direita.count(esquerda[i])
        pontuacao:int = esquerda[i] * ocorrencias
        
        lista_pontuacao.append(pontuacao)

    return sum(lista_pontuacao)


def main() -> None:

    test_file: list[str] = readlines('dia-01/example.txt')
    input_file: list[str] = readlines('dia-01/input.txt')

    print('Resposta parte 01:', parte01(input_file))

    print('Resposta parte 02:', parte02(input_file))
    
if __name__ == "__main__":
    main()