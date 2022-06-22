import os, sys


class EnvBuilder:
    def __init__(self, name: str) -> None:
        self.name = name

    def create(self):
        print(f'creating virtual environment named {self.name}')
        os.system(f'python -m venv {self.name}')

    def activate(self):
        print('activating virtual environment')
        os.system(f'source {self.name}/Scripts/activate')

    def deactivate(self):
        print('deactivating virtual environment')
        os.system('deactivate')

    def install_requirements(self, req_list: str):
        print(f'installing python modules listed in {req_list}')
        os.system(f'pip install -r {req_list}')

    def extend_search_path(self):
        print('extending python search path for packages and modules')
        path_for_searchpath = os.getcwd()
        print(path_for_searchpath)
        with open(f'{self.name}/Lib/site-packages/pinball-env.pth', 'w') as f:
            f.write(path_for_searchpath)

def main(arg: str):
    env = EnvBuilder('pinball-venv')
    if arg == '-c':
        env.create()
    elif arg == '-d':
        env.install_requirements('requirements.txt')
        env.extend_search_path()

if __name__=='__main__':
    main(sys.argv[1])