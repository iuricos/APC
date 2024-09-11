dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
horarios = {
    'M': ['08:00 - 08:55', '08:55 - 09:50', '10:00 - 10:55', '10:55 - 11:50', '12:00 - 12:55', '12:55 - 13:50'],
    'T': ['14:00 - 14:55', '14:55 - 15:50', '16:00 - 16:55', '16:55 - 17:50', '18:00 - 18:55', '18:55 - 19:50'],
    'N': ['19:00 - 19:50', '19:50 - 20:40', '20:50 - 21:40', '21:40 - 22:30']
}

grade = {dia: {turno: [''] * len(horarios[turno]) for turno in horarios} for dia in range(2, 8)}

def adicionar_disciplina(disciplina, horarios_disciplina):
    for horario in horarios_disciplina:
        dia = int(horario[0])
        turno = horario[1]
        aulas = list(map(int, horario[2:]))
        
        for aula in aulas:
            if grade[dia][turno][aula - 1] != '':
                print(f"!({'+ ' + disciplina + ' ' + ' '.join(horarios_disciplina)})")
                return
        for aula in aulas:
            grade[dia][turno][aula - 1] = disciplina

def remover_disciplina(disciplina, horarios_disciplina):
    for horario in horarios_disciplina:
        dia = int(horario[0])
        turno = horario[1]
        aulas = list(map(int, horario[2:]))
        
        for aula in aulas:
            if grade[dia][turno][aula - 1] != disciplina:
                print(f"!({'- ' + disciplina + ' ' + ' '.join(horarios_disciplina)})")
                return
        for aula in aulas:
            grade[dia][turno][aula - 1] = ''

def exibir_grade():
    print("+---------------+----------+----------+----------+----------+----------+----------+")
    print("|               " '|'+.join(dias_semana) + "|")
    print("+---------------+----------+----------+----------+----------+----------+----------+")
    
    for turno in horarios:
        for i, hora in enumerate(horarios[turno]):
            if any(grade[dia][turno][i] != '' for dia in range(2, 8)):
                linha = f"| {hora} "
                for dia in range(2, 8):
                    aula = grade[dia][turno][i]
                    linha += f"| {aula} " if aula != '' else "|          "
                print(linha + "|")
                print("+---------------+----------+----------+----------+----------+----------+----------+")


while True:
    comando = input().strip()
    
    if comando == "Hasta la vista, beibe!":
        break
    elif comando.startswith('+'):
        partes = comando.split()
        disciplina = partes[1]
        horarios_disciplina = partes[2:]
        adicionar_disciplina(disciplina, horarios_disciplina)
    elif comando.startswith('-'):
        partes = comando.split()
        disciplina = partes[1]
        horarios_disciplina = partes[2:]
        remover_disciplina(disciplina, horarios_disciplina)
    elif comando == '?':
        exibir_grade()
