entradaDia = int(input())

ano = int(entradaDia/365)
print(ano ,'ano(s)')
mes = int((entradaDia%365)/30)
print(mes ,'mes(es)')
dia = int((entradaDia%365)%30)
print(dia ,'dia(s)')
