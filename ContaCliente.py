import datetime

class ContaPoupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneracaoConta(self):
        self.saldo += self.saldo * self.taxaremuneracao


class ContaCliente:
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido = (self.valorinvestido - (self.taxarendimento * self.IOF * self.IR))

    def Extrato(self):
        print(f"O saldo atual da conta {self.numero} é {self.valorinvestido:.2f}")


class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)

    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)


class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)

    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido -= self.valorinvestido * self.IOF


class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self, contacliente):
        self.contas.append(contacliente)

    def calcularendimentomensal(self):
        for c in self.contas:
            c.CalculoRendimento()

    def Imprimesaldocontas(self):
        for c in self.contas:
            c.Extrato()

banco1 = Banco(999, "tels")
contacliente1 = ContaCliente(1, 0.01, 0.1, 1000, 0.05)
contacomum1 = ContaComum(2, 0.01, 0.1, 2000, 0.05)
contaremunerada1 = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

banco1.adicionaconta(contacliente1)
banco1.adicionaconta(contacomum1)
banco1.adicionaconta(contaremunerada1)
banco1.calcularendimentomensal()
banco1.Imprimesaldocontas()