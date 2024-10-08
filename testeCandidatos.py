import random

class Candidato:
    def __init__(self, nome, partido, voto):
        self.nome = nome
        self.partido = partido
        self.voto = voto

    def __str__(self):
        return f'Nome: {self.nome}, Partido: {self.partido}, Votos: {self.voto}'

class Candidatos:
    
    @staticmethod
    def Dados():
        nomes_partidos = {
            "Betão Nelo": "Vai dar PT",
            "Marta RossLinda": "PLA",
            "BolsaNoah": "UNI",
            "Lulala": "PUC",
            "Diego": "BZ"
        }

        NomesCand = []

        for nome, partido in nomes_partidos.items():
            voto = random.randint(0, 1000) 
            NomesCand.append(Candidato(nome, partido, voto))
        
        return NomesCand

    @staticmethod
    def PrintaCandidato(NomesCand):
        for candidato in NomesCand:
            print(candidato)

    @staticmethod
    def OrdenaçãoNome(NomesCand):
        for cont in range(1, len(NomesCand)):
            TempCand = NomesCand[cont]
            contComp = cont - 1
            while contComp >= 0 and (NomesCand[contComp].nome > TempCand.nome or
                                     (NomesCand[contComp].nome == TempCand.nome and NomesCand[contComp].voto > TempCand.voto) or
                                     (NomesCand[contComp].nome == TempCand.nome and NomesCand[contComp].voto == TempCand.voto and NomesCand[contComp].partido > TempCand.partido)):
                NomesCand[contComp + 1] = NomesCand[contComp]
                contComp -= 1
            NomesCand[contComp + 1] = TempCand

    @staticmethod
    def OrdenaçãoPartido(NomesCand):
        for cont in range(len(NomesCand)):
            MenorCont = cont
            for j in range(cont + 1, len(NomesCand)):
                if (NomesCand[j].partido < NomesCand[MenorCont].partido or
                   (NomesCand[j].partido == NomesCand[MenorCont].partido and NomesCand[j].voto > NomesCand[MenorCont].voto) or
                   (NomesCand[j].partido == NomesCand[MenorCont].partido and NomesCand[j].voto == NomesCand[MenorCont].voto and NomesCand[j].nome < NomesCand[MenorCont].nome)):
                    MenorCont = j
            NomesCand[cont], NomesCand[MenorCont] = NomesCand[MenorCont], NomesCand[cont]

    @staticmethod
    def OrdenaçãoVoto(NomesCand):
        for cont in range(len(NomesCand)):
            MenorCont = cont
            for j in range(cont + 1, len(NomesCand)):
                if (NomesCand[j].voto < NomesCand[MenorCont].voto or
                   (NomesCand[j].voto == NomesCand[MenorCont].voto and NomesCand[j].nome < NomesCand[MenorCont].nome) or
                   (NomesCand[j].voto == NomesCand[MenorCont].voto and NomesCand[j].nome == NomesCand[MenorCont].nome and NomesCand[j].partido < NomesCand[MenorCont].partido)):
                    MenorCont = j
            NomesCand[cont], NomesCand[MenorCont] = NomesCand[MenorCont], NomesCand[cont]

    @staticmethod
    def PBCand(NomesCand, CandProcurado):
        esquerda, direita = 0, len(NomesCand) - 1

        while esquerda <= direita:
            centro = (esquerda + direita) // 2
            if NomesCand[centro].nome == CandProcurado:
                return centro
            elif NomesCand[centro].nome < CandProcurado:
                esquerda = centro + 1
            else:
                direita = centro - 1
        return -1


if __name__ == "__main__":
    NomesCand = Candidatos.Dados()

    print("Candidatos Concorridos:")
    Candidatos.PrintaCandidato(NomesCand)

    print("\nCandidatos em Ordem Alfabética (Nome):")
    Candidatos.OrdenaçãoNome(NomesCand)
    Candidatos.PrintaCandidato(NomesCand)

    print("\nCandidatos em Ordem por Votos:")
    Candidatos.OrdenaçãoVoto(NomesCand)
    Candidatos.PrintaCandidato(NomesCand)

    print("\nCandidatos em Ordem por Partido:")
    Candidatos.OrdenaçãoPartido(NomesCand)
    Candidatos.PrintaCandidato(NomesCand)

    CandProcurado = input("\nPesquise um Candidato (Nome) --> ")
    Candidatos.OrdenaçãoNome(NomesCand)  
    Result = Candidatos.PBCand(NomesCand, CandProcurado)

    if Result != -1:
        print("\nSegue o Candidato Procurado -->")
        print(NomesCand[Result])
    else:
        print("\nHmmm, Não Achei o que procura")
