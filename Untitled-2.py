def calcimc(altura,peso):
    imc = peso/altura**2
    return imc

alt = float (input('informe sua altura \n'))
pes = float (input('informe seu peso \n'))
res = calcimc(alt, pes)
if res < 18.5:
    print('Magresa nivel Biel!')
elif res > 18.5 and res < 24.9:
    print ('Normal igual o Vaginildo!')
elif res > 25 and res < 29.9:
    print ('Sobrepeso nivel Pelado Pai!')
elif res > 30 and res < 39.9:
    print ('Obeso Nivel Pelado vermelho!')
elif res > 40:
    print ('Você esta um perereco Blob!')