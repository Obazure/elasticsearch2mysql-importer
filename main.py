

from modules.importer import es2mysql_importer
from system import boot

if __name__ == '__main__':
    context = boot.Context()

    es2mysql_importer(context)
