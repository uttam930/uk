import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asgard_proj.settings")
    
    import asgard_proj.startup as startup
    startup.run()
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
