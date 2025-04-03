salario = 2000 #pode ser usada apenas no codigo em questao - escopo local


def salario_bonus(bonus):
    global salario #pode ser usada a qualquer momento do codigo - escopo global
    salario += bonus
    return salario


salario_bonus(500)  # 2500
