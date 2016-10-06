from xlrd import open_workbook

planilha_a = open_workbook('planilha_a.xls', on_demand=True)
planilha_b = open_workbook('planilha_b.xls', on_demand=True)

lista1 = []
lista2 = []


def carrega_lista():
    pasta_a1 = planilha_a.sheet_by_index(0)
    pasta_b1 = planilha_b.sheet_by_index(0)

    for row in range(1, pasta_a1.nrows):
        lista1.append(pasta_a1.cell(row, 0).value)

    for row in range(1, pasta_b1.nrows):
        lista2.append(pasta_b1.cell(row, 0).value)


def grava_diferenca(lista1, lista2):
    carrega_lista()
    with open("resultado.txt", "w") as txt:
        lista3 = (list(set(lista1) - set(lista2)))

        for linha in lista3:
            txt.write(linha + "\n")


if __name__ == '__main__':
    grava_diferenca(lista1, lista2)
