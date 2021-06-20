#! / usr / bin / env python
""  "Utilitário de linha de comando do Django para tarefas administrativas."  ""
importar   os
import   sys


def   main ():
    os . amb . setdefault ( 'DJANGO_SETTINGS_MODULE' , 'resumeBuilder.settings' )
    tente :
        do   django . n ú cleo . gerenciamento  de   importação çã o   execute_from_command_line
    EXCETO   ImportError   Como   exc :
        raise   ImportError (
            "Não foi possível importar Django. Você tem certeza que está instalado e"
            "disponível em sua variável de ambiente PYTHONPATH? Você"
            "carga de ativar um ambiente virtual?"
        ) de   exc
    execute_from_command_line ( sys . argv )
