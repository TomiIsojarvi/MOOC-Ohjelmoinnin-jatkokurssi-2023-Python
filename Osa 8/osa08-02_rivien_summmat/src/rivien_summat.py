def rivien_summat(matriisi: list):
  for rivi in matriisi:
    summa = sum(rivi)
    rivi.append(summa)

if __name__ == "__main__":
  matriisi = [[1, 2], [3, 4]]
  rivien_summat(matriisi)
  print(matriisi)