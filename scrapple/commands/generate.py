"""
scrapple.commands.generate
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function
from jinja2 import Template
import os
import json
from colorama import init, Fore, Back

import scrapple
from scrapple.commands import command

class GenerateCommand(command.Command):
    """
    Defines the execution of :ref:`generate <command-generate>`
    """

    def __init__(self, args):
        super(GenerateCommand, self).__init__(args)
        init()

    def execute_command(self):
        """
        
        """
        print(Back.GREEN + Fore.BLACK + "Scrapple Generate")
        print(Back.RESET + Fore.RESET)
        directory = os.path.join(scrapple.__path__[0], 'templates', 'scripts')
        with open(os.path.join(directory, 'generate.txt'), 'r') as f:
            template_content = f.read()
        template = Template(template_content)
        try:
            with open(self.args['<projectname>'] + '.json', 'r') as f:
                config = json.load(f)
            if self.args['--output_type'] == 'csv':
                from scrapple.utils.config import extract_fieldnames
                config['fields'] = str(extract_fieldnames(config))
            config['output_file'] = self.args['<output_filename>']
            config['output_type'] = self.args['--output_type']
            rendered = template.render(config=config)
            with open(self.args['<output_filename>'] + '.py', 'w') as f:
                f.write(rendered)
            print(Back.WHITE + Fore.RED + self.args['<output_filename>'], \
                  ".py has been created" + Back.RESET + Fore.RESET, sep="")
        except IOError:
            print(Back.WHITE + Fore.RED + self.args['<projectname>'], ".json does not ", \
                  "exist. Use ``scrapple genconfig``." + Back.RESET + Fore.RESET, sep="")
