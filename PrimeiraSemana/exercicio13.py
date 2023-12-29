
#### ----- Decomposição de problemas ----- ####

HIST = ''

def calcula(expr):
    try:
        return eval(expr) # A função Eval avalia o expressão de cadeia de caracteres e retorna seu valor.
    except:
        print('Expressão inválida!')
        return None

def historico(expr, res):
    global HIST # ----------- A variável "GLOBAL" são aquelas que podem ser acessadas e modificadas em qualquer parte do
    if res is not None:     # programa, seja dentro de funções, classes ou módulos.
        HIST += '\n\n' + expr
        HIST += '\n' + str(res)

def principal():
    while True:
        print('Informe a expressão matemática')
        print('(h para histórico, s para sair)')
        expr = input()
        if expr.lower() == 's':
            break
        if expr.lower() == 'h':
            print(HIST, '\n')
        else:
            res = calcula(expr)
            historico(expr, res)
            print(res, '\n')

if __name__ == '__main__':
    principal()

