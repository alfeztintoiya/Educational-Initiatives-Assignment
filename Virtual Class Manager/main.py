from manager import VirtualClassManager
from logger_config import setup_logger

logger = setup_logger()

if __name__ == "__main__":
    manager = VirtualClassManager()
    logger.info("Virtual Classroom Manager")
    
    manager.show_commands()
    running = True
    while running:
        cmd = input("\n> ")
        if not manager.handle_command(cmd):
            break;