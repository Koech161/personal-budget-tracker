from cli.cli import main


if __name__ == '__main__':
    
    try:
        main()
    except Exception as e:
        print(f'An error ocored {e}.')

