from ocha.clis.base import Base
import getpass

class Cantik(Base):
    """
    usage:
        cantik
        cantik search [-f FILE]

    Build Yaml File
    Options:
    -h --help                             Print usage
    -f file --file=FILE
    """
    def execute(self):

        if self.args['search']:
            if self.args['--file']:
                print("Kaka Suruh Cari saya ini : ", self.args['--file'])
                question = input("Y/N : ")
                if question=="Y" or question=="y":
                    print("Ocha Lagi Malas Kak :) ")
                exit()
            print("Apa Yang Dicari Kak?")
            exit()

        print("Hey Saya Ocha")
        nama = input("Nama Kakak Siapa : ")
        print("Hello Kakak "+nama+" Yang Suka Ba patende!")
        exit()
