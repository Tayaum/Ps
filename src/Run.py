try:
    import sys
    import os
    import basic
    from rich.console import Console
    console = Console()
    print = console.print
    if os.path.exists(sys.argv[0]):
        result, error = basic.run('[blue]' + sys.argv[0] + '[/]', 'run("' + sys.argv[0].replace('\\', '/') + '")')
        if error:
            print("[red]" + error.as_string(), highlight=False)
        elif result:
            if len(result.elements) == 1:
                result = result.elements[0]
                print(result, highlight=False)
            else:
                result = result
                print(result, highlight=False)

    else:
        console.print('[red]File Does Not Exist')
except KeyboardInterrupt:
    exit(2)