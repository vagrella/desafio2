#Vornei: Classe de modelagem Job

#Nomes dos Campos
class Campo:
    id = 'ID'
    descricao = 'Descrição'
    data_maxima_conclusao = 'Data Máxima de conclusão'
    tempo_estimado = 'Tempo estimado'

#Informações
class Info:
    def __init__(self, Info):
        self.id = Info.id
        self.descricao = Info.descricao
        self.data_maxima_conclusao = Info.data_maxima_conclusao
        self.tempo_estimado = Info.tempo_estimado