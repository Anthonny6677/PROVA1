pais_a = 80000
crescimento_a = 0.03
pais_b = 200000
crescimento_b = 0.015

anos = 0

while pais_a <= pais_b:
    pais_a += pais_a * crescimento_a
    pais_b += pais_b * crescimento_b
    anos += 1

print(f"São necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B")
