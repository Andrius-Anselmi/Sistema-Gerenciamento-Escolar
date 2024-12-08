class Pessoa:
    def __init__(self, nome: str, idade: float):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        # Polimorfismo: O método 'apresentar' será sobrescrito nas classes filhas (Aluno e Professor)
        return f"{self.nome}, {self.idade} anos."


class Nota:
    def __init__(self, valor: float, turma: 'Turma'):
        self.valor = valor
        self.turma = turma  # Associação: A Nota está associada à turma (disciplina) em que foi dada

    def formatar_nota(self):
        return f"Disciplina: {self.turma.nome}, Nota: {self.valor:.2f}"


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: float):
        super().__init__(nome, idade)
        self.notas = []  # Associação: O Aluno tem uma lista de Notas associadas

    def adicionar_nota(self, nota: Nota):
        self.notas.append(nota)

    def calcular_media(self):
        if self.notas:
            return sum(nota.valor for nota in self.notas) / len(self.notas)
        return 0

    def apresentar(self):
        # Polimorfismo: A classe Aluno sobrescreve o método 'apresentar'
        # para incluir as notas e a média do aluno
        notas_formatadas = "\n  ".join([nota.formatar_nota() for nota in self.notas]) if self.notas else "Nenhuma nota registrada."
        return f"Aluno: {self.nome}, {self.idade} anos\nNotas:\n  {notas_formatadas}\nMédia: {self.calcular_media():.2f}"


class Professor(Pessoa):
    def __init__(self, nome: str, idade: float, disciplina: str):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        # Polimorfismo: A classe Professor sobrescreve o método 'apresentar'
        # para exibir informações sobre o professor e a disciplina
        return f"Professor: {self.nome}, Disciplina: {self.disciplina}"


class Turma:
    def __init__(self, nome: str, professor: Professor):
        self.nome = nome
        self.professor = professor  # Associação: A Turma tem um Professor associado
        self.alunos = []  # Associação: A Turma tem uma lista de Alunos associados

    def adicionar_aluno(self, aluno: Aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
        else:
            print(f"Aluno {aluno.nome} já está matriculado na disciplina {self.nome}.")

    def listar_turma(self):
        return [aluno.nome for aluno in self.alunos]

    def apresentar_turma(self):
        print(f"\n=== Disciplina: {self.nome} ===")
        print(f"Professor: {self.professor.apresentar()}")
        if self.alunos:
            for aluno in self.alunos:
                print(f"\n{aluno.apresentar()}")  # Polimorfismo: O método 'apresentar' é chamado 
        else:
            print("Nenhum aluno matriculado.")


# Listas para armazenar objetos
professores = []
alunos = []
turmas = []


def validar_input_numerico(prompt, tipo=float, valor_min=0, valor_max=float('inf')):
    while True:
        try:
            valor = tipo(input(prompt))
            if valor < valor_min or valor > valor_max:
                print(f"Por favor, insira um valor entre {valor_min} e {valor_max}.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def cadastrar_professor():
    nome = input("Nome do professor: ")
    idade = validar_input_numerico("Idade do professor: ", tipo=float, valor_min=18)
    disciplina = input("Disciplina que o professor ensina: ")

    for professor in professores:
        if professor.nome == nome and professor.disciplina == disciplina:
            print(f"Professor {nome} já está cadastrado com a disciplina {disciplina}.")
            return

    professores.append(Professor(nome, idade, disciplina))
    print(f"Professor {nome} cadastrado com sucesso!")


def cadastrar_aluno():
    nome = input("Nome do(a) aluno: ")
    idade = validar_input_numerico("Idade do(a) aluno: ", tipo=float, valor_min=0)
    
    alunos.append(Aluno(nome, idade))  # Associação: O Aluno é adicionado à lista de alunos
    print(f"Aluno(a) {nome} cadastrado com sucesso!")


def criar_turma():
    if not professores:
        print("Não há professores cadastrados. Cadastre um professor primeiro.")
        return

    print("\nProfessores disponíveis:")
    for i, professor in enumerate(professores):
        print(f"{i + 1}. {professor.apresentar()}")  # Polimorfismo: O método 'apresentar' é chamado para o professor

    escolha_prof = validar_input_numerico("Escolha o professor (número): ", tipo=int, valor_min=1, valor_max=len(professores)) - 1
    professor = professores[escolha_prof]

    nome_turma = input("Nome da turma): ")
    turmas.append(Turma(nome_turma, professor))  # Associação: A Turma é associada a um Professor
    print(f"Turma {nome_turma} criada com sucesso!")


def matricular_aluno_em_turma():
    if not turmas:
        print("Não há disciplinas (turmas) cadastradas. Cadastre uma turma primeiro.")
        return

    if not alunos:
        print("Não há alunos cadastrados. Cadastre um aluno primeiro.")
        return

    print("\nDisciplinas (turmas) disponíveis:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1}. {turma.nome} (Professor: {turma.professor.nome})")  # Associação: Exibe as turmas com seus professores

    escolha_turma = validar_input_numerico("Escolha a disciplina (turma) (número): ", tipo=int, valor_min=1, valor_max=len(turmas)) - 1
    turma = turmas[escolha_turma]

    print("\nAlunos disponíveis:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1}. {aluno.nome}")  # Associação: Exibe os alunos cadastrados

    escolha_aluno = validar_input_numerico("Escolha o aluno(a) (número): ", tipo=int, valor_min=1, valor_max=len(alunos)) - 1
    aluno = alunos[escolha_aluno]

    turma.adicionar_aluno(aluno)  # Associação: Adiciona o aluno à turma
    print(f"Aluno(a) {aluno.nome} matriculado na turma:  {turma.nome} com sucesso!")


def adicionar_nota():
    if not alunos:
        print("Não há alunos cadastrados. Cadastre um aluno primeiro.")
        return

    print("\nAlunos disponíveis:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1}. {aluno.nome}")  # Associação: Exibe os alunos cadastrados

    escolha_aluno = validar_input_numerico("Escolha o aluno(a) (número): ", tipo=int, valor_min=1, valor_max=len(alunos)) - 1
    aluno = alunos[escolha_aluno]

    # Listando as turmas nas quais o aluno está matriculado
    turmas_matriculadas = [turma for turma in turmas if aluno in turma.alunos]
    
    if not turmas_matriculadas:
        print(f"Aluno(a) {aluno.nome} não está matriculado em nenhuma turma.")
        return

    print("\nDisciplinas (turmas) nas quais o aluno(a) está matriculado:")
    for i, turma in enumerate(turmas_matriculadas):
        print(f"{i + 1}. {turma.nome} (Professor: {turma.professor.nome})")

    escolha_turma = validar_input_numerico("Escolha a disciplina (turma) (número): ", tipo=int, valor_min=1, valor_max=len(turmas_matriculadas)) - 1
    turma_associada = turmas_matriculadas[escolha_turma]

    valor = validar_input_numerico("Nota: ", tipo=float, valor_min=0, valor_max=10)
    aluno.adicionar_nota(Nota(valor, turma_associada))  # Associação: A Nota é associada ao Aluno e à Turma
    print(f"Nota de {valor} adicionada à disciplina {turma_associada.nome} do(a) aluno {aluno.nome} com sucesso!")


def exibir_turmas():
    # Verifica se há alunos cadastrados
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    # Exibe a lista de alunos cadastrados
    print("\nAlunos disponíveis:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1}. {aluno.nome}")  # Exibe o nome de cada aluno cadastrado

    # Solicita ao usuário escolher um aluno
    escolha_aluno = validar_input_numerico("Escolha o aluno(a) (número): ", tipo=int, valor_min=1, valor_max=len(alunos)) - 1
    aluno = alunos[escolha_aluno]  # Atribui o aluno escolhido

    # Filtra as turmas nas quais o aluno está matriculado
    turmas_matriculadas = [turma for turma in turmas if aluno in turma.alunos]

    # Verifica se o aluno está matriculado em alguma turma
    if not turmas_matriculadas:
        print(f"Aluno(a) {aluno.nome} não está matriculado em nenhuma turma.")
        return

    # Exibe as turmas em que o aluno está matriculado
    print(f"\nDisciplinas (turmas) nas quais o aluno {aluno.nome} está matriculado:")
    for turma in turmas_matriculadas:
        print(f"\nTurma: {turma.nome} (Professor: {turma.professor.nome})")  # Exibe o nome da turma e do professor
        
        # Filtra as notas do aluno na turma atual
        notas_do_aluno = [nota for nota in aluno.notas if nota.turma == turma]
        
        # Verifica se o aluno tem notas na turma e exibe-as
        if notas_do_aluno:
            for nota in notas_do_aluno:
                print(f"  Nota: {nota.valor:.2f}")  # Exibe a nota formatada com 2 casas decimais
        else:
            # Caso o aluno não tenha notas na turma, exibe uma mensagem
            print("  Nenhuma nota registrada nesta turma.")



def menu():
    while True:
        print("\n=== Sistema Escolar ===")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Turma")
        print("4. Matricular Aluno em Disciplina (Turma)")
        print("5. Adicionar Nota a Aluno")
        print("6. Exibir Disciplinas (Turmas)")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_aluno()

        elif escolha == "2":
            cadastrar_professor()

        elif escolha == "3":
            criar_turma()

        elif escolha == "4":
            matricular_aluno_em_turma()

        elif escolha == "5":
            adicionar_nota()

        elif escolha == "6":
            exibir_turmas()

        elif escolha == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Executa o menu
menu()
