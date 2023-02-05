d_i = int(input('Dia '))
h_i, m_i, s_i = str(input('')).split(":")
dia_f = int(input('Dia '))
h_f, m_f, s_f = str(input('')).split(":")
h_i, m_i, s_i, h_f, m_f, s_f = int(h_i), int(m_i), int(s_i), int(h_f), int(m_f), int(s_f)

hora_i = 3600 * h_i
minuto_i = 60 * m_i
segundo_i = hora_i + minuto_i + s_i

hora_f = 3600 * h_f
minuto_f = 60 * m_f
segundo_f = hora_f + minuto_f + s_f

if segundo_i > segundo_f:
    segundo = segundo_i - segundo_f
else:
    if segundo_f > segundo_i:
        segundo = segundo_f - segundo_i

horas = segundo // 3600
minutos = segundo - (horas * 3600)
segundos = minutos // 60

print(horas, minutos, segundos)

