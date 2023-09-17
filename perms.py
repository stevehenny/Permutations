def get_string_perms(l: list[str]) -> list[list[str]]:
    lst = []
    for word in l:
        lst.append(word)

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  perm is
        # remaining list
        perm = lst[:i] + lst[i + 1 :]

        # Generating all permutations where m is first
        # element
        for p in get_string_perms(perm):
            l.append([m] + p)
    return l


def main() -> NotImplementedError:
    val = input("What do you want the input to be?")
    lst = val.split()
    lst = get_string_perms(lst)
    for val in lst:
        s = " ".join(val)
        print(s)
    return 0


if __name__ == "__main__":
    main()
