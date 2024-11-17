# for petlja mora ić van comprehensiona za dictionary da se dictionary ponavlja za svaki par
kubovi = [{broj: broj*broj*broj if broj % 2 != 0 else broj}
          for broj in range(1, 11)]

# [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9: 729}, {10: 10}]
print(kubovi)
