def read_and_modify_file(input_filename , output_filename):
    try:
        with open(input_filename , 'r') as infile:
            content = infile.read()

            modified_content = content.upper()

            with open(output_filename , 'w') as outfile:
                outfile.write(modified_content)

                print(f"File modified successfully. The modified content has been written to {output_filename}.")
    except FileNotFoundError:
        print(f"Error: The fie '{input_filename}' does not exist.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")        

    
def ask_for_file():
    try:
        input_file = input("Enter the file to read from:  ")
        output_file = input("Enter the filename to write the modified content to:  ")

        read_and_modify_file(input_file , output_file)

    except Exception as e:
        print(f"An error occurred while processing: {e}")

        ask_for_file()