from edit_distance.recursive_memo import edit_distance

def main():
    print("Distância de Edição (Recursiva com Memoization)")
    s1 = input("Digite a primeira string: ").strip()
    s2 = input("Digite a segunda string: ").strip()

    distance = edit_distance(s1, s2)
    print(f"\nA distância de edição entre '{s1}' e '{s2}' é: {distance}")

if __name__ == "__main__":
    main()
