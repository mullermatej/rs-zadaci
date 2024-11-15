rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj",
          "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
# min_duljina = 7

duge_rijeci = list(
    filter(lambda rijec: len(rijec) > min_duljina, rijeci))

# ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']
print(duge_rijeci)
