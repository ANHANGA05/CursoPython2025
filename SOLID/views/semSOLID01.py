class SistemaCadastro:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int): # 1
            print("Acessando o banco de dados...") # 2
            print(f"Cadastrar usuario {nome}, idade {idade}")
        else:
            print("dados invalidos") # 3

sistema = SistemaCadastro()
sistema.cadastrar("Antonio Gomes", 37)
sistema.cadastrar("Antonio Nhanga", "37a")