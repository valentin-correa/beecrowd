while True:

    try:

        N = int(input())  # Pairs of shoes

        # Dictionary that contains a pair number and an array of feets [D,E]
        shoes = {}

        for i in range(0, N):
            size, feet = input().split()

            if feet in ['D', 'E']:  # Only left and right feets
                if size not in shoes:
                    shoes[size] = [feet]
                elif size in shoes and feet not in shoes[size]:  # Missing feet
                    shoes[size].append(feet)

        count = 0

        for shoe in shoes:
            if len(shoes[shoe]) == 2:  # Only complete pairs
                count += 1

        print(count)

    except EOFError:
        break
