class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger,cls).__new__(cls)
        return cls._instance
    
    def log(self,message):
        print(f"[LOG]: {message}")

logger1 = Logger()
logger2 = Logger()
logger1.log("System started")
logger2.log("User logged in")
print("Are logger1 and logger2 same?",logger1 is logger2)
