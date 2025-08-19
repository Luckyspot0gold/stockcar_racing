def handle_command(self, command):
    """Wyoming-style straight talk"""
    cmd = command.lower().strip()
    
    if "break the jar" in cmd:
        return self.break_jar()
    elif "power" in cmd:
        return self.manage_power(cmd)
    elif "crypto" in cmd:
        return "CRYPTO IS DIGITAL SOVEREIGNTY. BUILD ON TRUTH."
    elif "racing" in cmd or "stockcar" in cmd:
        return self.racing_analysis(cmd)
    elif "help" in cmd:
        return self.show_help()
    elif "exit" in cmd:
        return "exit"
    else:
        return "THAT AIN'T A WYOMING PROBLEM."

def racing_analysis(self, cmd):
    """Stockcar racing insights"""
    if "strategy" in cmd:
        return "WYOMING RACING: DRAFT SMART, PASS CLEAN, WIN HONEST."
    elif "track" in cmd:
        return "EVERY TRACK'S GOT SECRETS. LEARN 'EM OR EAT DUST."
    else:
        return "STOCKCAR RACING: WHERE HORSEPOWER MEETS WILLPOWER."
