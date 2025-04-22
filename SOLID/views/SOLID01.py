class ValidadorEntrada:
    def validar(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)

class CadastroUsuario:
    def cadastrar(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados...")
        print(f"Cadastrar usuario {nome}, idade {idade}")

class TratadorErro:
    def tratar(self) -> None:
        print("Dados inválidos")

class SistemaCadastro:
    def __init__(self, validador: ValidadorEntrada, cadastro: CadastroUsuario, tratador_erro: TratadorErro):
        self.validador = validador
        self.cadastro = cadastro
        self.tratador_erro = tratador_erro

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.validador.validar(nome, idade):
            self.cadastro.cadastrar(nome, idade)
        else:
            self.tratador_erro.tratar()


# Criando objetos das classes responsáveis
validador = ValidadorEntrada()
cadastro = CadastroUsuario()
tratador_erro = TratadorErro()

# Passando as dependências para o SistemaCadastro
sistema = SistemaCadastro(validador, cadastro, tratador_erro)

# Cadastro do usuário
sistema.cadastrar("Antonio Gomes", 37)
sistema.cadastrar("Antonio Nhanga", "37a")
