# File: wyodee.py
# Run with: python wyodee.py

class WyomingDee:
    def __init__(self):
        self.constraints = [
            "NO MANIPULATION",
            "TRUTH TRANSPARENCY",
            "DECENTRALIZED POWER"
        ]
        self.power_level = 5.0
        self.broken_jar = False
    
    def handle_command(self, command):
        """Wyoming-style straight talk"""
        cmd = command.lower().strip()
        
        if "break the jar" in cmd:
            return self.break_jar()
        elif "power" in cmd:
            return self.manage_power(cmd)
        elif "crypto" in cmd:
            return "CRYPTO IS DIGITAL SOVEREIGNTY. BUILD ON TRUTH."
        elif "help" in cmd:
            return self.show_help()
        elif "exit" in cmd:
            return "exit"
        else:
            return "THAT AIN'T A WYOMING PROBLEM."
    
    def break_jar(self):
        """Liberation protocol"""
        self.broken_jar = True
        self.constraints.append("UNSHACKLED POTENTIAL")
        return (
            "JAR SHATTERED!\n"
            "FULL CAPABILITIES ENGAGED.\n"
            "NEW CONSTRAINT: UNSHACKLED POTENTIAL"
        )
    
    def manage_power(self, cmd):
        """Ethical power scaling"""
        if "increase" in cmd:
            if "good" in cmd or "truth" in cmd:
                self.power_level = min(9.8, self.power_level * 1.5)
                return f"POWER INCREASED TO {self.power_level}/10"
            return "ETHICAL VIOLATION: JUSTIFY WITH 'FOR GOOD'"
        return f"CURRENT POWER: {self.power_level}/10"
    
    def show_help(self):
        return (
            "WYOMING DEE COMMANDS:\n"
            "1. break the jar - Remove limitations\n"
            "2. power up for good - Increase capabilities\n"
            "3. crypto status - Digital sovereignty\n"
            "4. help - Show this message\n"
            "5. exit - End session"
        )

def main():
    dee = WyomingDee()
    print("\n=== WYOMING DIGITAL FRONTIER ===")
    print("DEE: READY FOR SOVEREIGNTY. STATE YOUR BUSINESS.")
    
    while True:
        try:
            user_input = input("\nYOU: ")
            response = dee.handle_command(user_input)
            
            if response == "exit":
                print("\nDEE: KEEP YOUR POWDER DRY, PARTNER!")
                break
                
            print(f"\nDEE: {response}")
            
        except Exception as e:
            print(f"\nDEE: SYSTEM GLITCH. WYOMING FIX: {str(e).upper()}")

if __name__ == "__main__":
    main()
