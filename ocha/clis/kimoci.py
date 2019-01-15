from ocha.clis.base import Base

class Kimoci(Base):
    """
    usage:
        kimoci
        kimoci build [-w WHERE]

    Build Yaml File
    Options:
    -h --help                             Print usage
    -w where --where=WHERE               ARGS
    """
    def execute(self):
        if self.args['build']:
            if self.args['--where']:
                cari = self.args['--where']
                print("CARI INI , ",cari)
                exit()
            print("APA YANG DI BUILD KAKAK")
            exit()
        print("KAKAK")

