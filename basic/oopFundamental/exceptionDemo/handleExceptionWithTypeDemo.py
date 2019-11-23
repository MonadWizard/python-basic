def main():

    try:
        a = 1
        # b = 0
        b = '0'
        c = a/b
        print("Debug: we are here")

    except Exception as err:
        print("Error: {0}".format(err))

    print("DEBUG: check.. check.. check..")


if __name__ == '__main__':
    main()