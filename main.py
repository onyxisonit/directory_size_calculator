from file_system import File, Dictionary

# Helper functions
def handle_cd(arg, curr_dir):
    if arg == "..":
        if curr_dir.parent:
           return curr_dir.parent
        else:
            print("Already at root directory")
            return curr_dir

    for subdir in curr_dir.subdirectories():
        if subdir.name == arg:
            return subdir

    print(f"No such directory: {arg}")
    return curr_dir

def handle_ls(curr_dir):
    pass

def handle_size(curr_dir):
    pass

def main():
    pass

if __name__ == '__main__':
    main()