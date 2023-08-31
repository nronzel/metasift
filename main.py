from cli.cli import CLI


def main():
    cli = CLI()
    cli.run()
    # if len(sys.argv) != 2:
    #     raise Exception("Not enough or too many arguments provided.")
    #
    # args = sys.argv[1:]
    # file_path = args[0]
    #
    # metadata = extract_docx_metadata(file_path)
    #
    # if metadata is not None:
    #     for key, value in metadata.items():
    #         print(f"{key}: {value}")
    #
    # print("\n\nBeginning document protection check...")
    # pw_cli()


if __name__ == "__main__":
    main()
