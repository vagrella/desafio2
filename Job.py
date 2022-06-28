#Vornei: Classe de modelagem Job

#Nomes dos Campos
class Job:
    cl_id = 'ID'
    cl_descricao = 'Descrição'
    cl_data_maxima_conclusao = 'Data Máxima de conclusão'
    cl_tempo_estimado = 'Tempo estimado'

#Informações
class Info:
    def __init__(self, Info):
        self.id = Info.id
        self.descricao = Info.descricao
        self.data_maxima_conclusao = Info.data_maxima_conclusao
        self.tempo_estimado = Info.dtempo_estimado