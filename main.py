import os

class ClothesStream:
    def __init__(self, path):
        self.path = path

    def run(self):
        ls = os.listdir(self.path)
        for folder in ls:
            eup = os.listdir(f'{self.path}/{folder}')
            for file in eup:
                newName = f'{folder}/{folder}^{file}'
                old = f'{folder}/{file}'
                os.renames(f'{self.path}/{old}', f'{self.path}/{newName}')

        print('Done.')

path = 'path-to-stream-files' # C:/files

run = ClothesStream(path)
run.run()
