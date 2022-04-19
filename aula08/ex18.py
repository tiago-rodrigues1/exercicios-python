from math import sin, cos, tan, radians

angulo = float(input('- Digite o ângulo que você deseja: '))

sin = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))
