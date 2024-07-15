import datetime
from datetime import datetime, timedelta, date, timezone
import pytz

'''datetime'''

data = date(2024, 6, 11)
print(data)

d1 = datetime.today()
print(d1)

# Criando data e hora
d = datetime(2024, 6, 10, 20, 48)
print(d)

# Utiliando delta
# Adicionando uma semama
d = d + timedelta(weeks=1)
print(d)

tipo_carro = 'P'  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == 'M':
    print(data_atual)
else:
    print(data_atual)

print(date.today() - timedelta(days=1))  # retorna a data anterior ao dia que se está

resultado = datetime(2024, 6, 11, 16, 59)
print(resultado.time())  # horario

print(datetime.now().date())  # ano, mes e dia

'''strftime e strptime'''
data_hora_atual = datetime.now()
data_hora_str = "2024-6-11 17:56"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

'''Timezone'''

# Utilizando o timezone com a biblioteca pytz (necessita ser instalada)
# Criando datetime com timezone
moment = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(moment)
# Uma boa pratica é salvar no banco de dados objetos datas em utc

# Utilizando o timezone com o datetime (padrão do python)
# Criando datetime com timezone
d_padrao = datetime.now(timezone(timedelta(hours=-3), "BRT"))
print(d_padrao)

# Convertendo para outro timezone
d_utc = d.astimezone(timezone.utc)
print(d_utc)


