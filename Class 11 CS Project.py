while True:
    print("\nWelcome To Army Public School")
    d = input("Enter Your Category eg. Student or Staff: ").strip().capitalize()

    if d == "Student":
        try:
            a = int(input("Enter Your Class eg. 1-12: "))
        except ValueError:
            print("❌ Invalid class input! Restarting...\n")
            continue

        if a in range(1, 11) or a == 12:
            print("Under Process")

        elif a == 11:
            print("\n1. English\n2. Math\n3. Computer Science\n4. Physics\n5. Chemistry\n6. Hindi")
            try:
                b = int(input("Select Subject (1-6): "))
            except ValueError:
                print("❌ Invalid subject input! Restarting...\n")
                continue

            if b in [1, 2, 4, 5, 6]:
                print("Under Process")
            elif b == 3:
                print("\nComputer Science Chapters:")
                print("1. Computer System and Organisation")
                print("2. Software")
                print("3. Data Representation")
                print("4. Boolean Algebra")
                print("5. Data Handling")
                print("6. Getting Started With Python")
                print("7. Flow of Control")
                print("8. String")
                print("9. List")
                print("10. Dictionary")
                print("11. Tuple")
                print("12. Cyber Security")

                try:
                    c = int(input("Select Chapter No. (1-12): "))
                except ValueError:
                    print("❌ Invalid chapter number! Restarting...\n")
                    continue

                if c == 5:
                    print("Data Types:\n Numbers\n  1.Integer\n  2.Float\n  3.Complex\n  4.Boolean")
                    print("Sequences:\n  1.String\n  2.Tuple\n  3.List\nMapping:\n  1.Dictionary")
                    print("Mutable - Values can be changed")
                    print("Immutable - Values can't be changed")
                    print("Variables - Memory storage")
                    print("Operators - +, -, >, <, /, is, not, and, or, etc.")

                elif c == 6:
                    print("Tokens: smallest units in a program")
                    print("Types:\n 1. Keywords\n 2. Identifiers\n 3. Literals\n 4. Operators\n 5. Punctuators")
                    print("Comments - Non-executable lines\nBlocks - Grouped statements")

                elif c == 7:
                    print("Flow of Control:")
                    print("1. Sequential - Default")
                    print("2. Selection - if, elif, else")
                    print("3. Iteration - for, while")

                elif c == 8:
                    print("String Basics - Immutable sequences")
                    print("Operators: + (Concatenate), * (Repeat), in / not in")
                    print("Slicing: string[start:stop:step]")
                    print("Useful Functions: len(), upper(), lower(), find(), replace(), split(), etc.")

                elif c == 9:
                    print("List - Mutable, ordered collection")
                    print("Syntax: [1, 2, 'text']")
                    print("Methods: append(), insert(), remove(), sort(), etc.")

                elif c == 10:
                    print("Dictionary - Key-value pair")
                    print("Syntax: {'key': value}")
                    print("Methods: keys(), values(), items(), get(), update()")

                elif c == 11:
                    print("Tuple - Immutable sequence")
                    print("Syntax: (1, 2, 'text')")
                    print("Functions: len(), max(), min(), tuple()")

                else:
                    print("Under Process")

            else:
                print("❌ Invalid Subject! Restarting...\n")
                continue
        else:
            print("❌ Invalid Class! Restarting...\n")
            continue

    elif d == "Staff":
        print("Under Process")

    else:
        print("❌ Invalid Category! Restarting...\n")
        continue

    restart = input("\nDo you want to restart? (yes/no): ").lower()
    if restart != "yes":
        print("Thank you for using the system!")
        break
