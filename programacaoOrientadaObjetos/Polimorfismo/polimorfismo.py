class Passaro:
    def voar(self):
        print("Voando....")


# Com a implementação do pai
class Pardal(Passaro):
    def voar(self):
        super().voar()


# Sem a implementação do pai
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


# FIXME: Exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())

