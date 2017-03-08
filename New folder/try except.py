while True:
    try:
        number=int(input('Whats the number :\n'));
        print(10/number);
        break;
    except ValueError:
        print('Make sure you enter a number');
    except ZeroDivisionError:
        print('Don\'t enter 0');
    finally:
        print('Finally')