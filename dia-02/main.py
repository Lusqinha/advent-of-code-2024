def readlines(filename) -> list[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()

def separarRelatorios(lines:list[str]) -> list[list[int]]:
    separado:list[list[int]] = []
    
    for line in lines:
        x: list[str] = line.split(" ")
        x: list[int] = [int(value) for value in x]

        separado.append(x)
    
    return separado

def isSafe(relatorio) -> bool:
    
    crescente:bool = True if relatorio[0] < relatorio[-1] else False
    relatorio_length = len(relatorio)-1
    
    checked = 0
    
    for i in relatorio: 
        isSmaller = (i!=relatorio[-1] and abs(i - relatorio[relatorio.index(i)+1])<=3)
        
        if isSmaller:
            if i < relatorio[relatorio.index(i)+1] and crescente:
                checked+=1
            elif i > relatorio[relatorio.index(i)+1] and not crescente:
                checked+=1
    
    if checked == relatorio_length:
        return True

    return False

def isSafeAfterRemoval(relatorio) -> bool:
    for i in range(len(relatorio)):
        relatorio_alterado:list[int] = relatorio[:i] + relatorio[i+1:]
        
        if isSafe(relatorio_alterado):
            return True
    
    return False

def parte01(lines:list[str]) -> int:
    
    relatorios: list[list[int]] = separarRelatorios(lines)
    
    seguros:int = 0
    
    for relatorio in relatorios:
        if isSafe(relatorio):
            seguros += 1
            
    return seguros
        
def parte02(lines:list[str]) -> int:
    relatorios: list[list[int]] = separarRelatorios(lines)
    
    seguros: int = 0
    aprovado_direto = 0
    aprovado_corrigido = 0
    
    for relatorio in relatorios:
        if isSafe(relatorio):
            
            seguros += 1
            aprovado_direto += 1
        elif isSafeAfterRemoval(relatorio):
            
            seguros += 1
            aprovado_corrigido += 1
            
    print(f"DIRETO: {aprovado_direto}\nCORRIGIDO: {aprovado_corrigido}\nTOTAL: {seguros}")
    return seguros

            

def main() -> None:
    
    lines_input: list[str] = readlines('dia-02/input.txt')
    lines_example: list[str] = readlines('dia-02/example.txt')

    print(parte02(lines_input))
    
if __name__ == "__main__":
    main()