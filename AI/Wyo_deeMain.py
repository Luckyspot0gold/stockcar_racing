def main():
    dee = WyomingDee()
    print("\n=== WYOMING DIGITAL FRONTIER ===")
    print("DEE: READY FOR SOVEREIGNTY. STATE YOUR BUSINESS.")
    
    while True:
        try:
            user_input = input("\nYOU: ").strip()
            if not user_input:
                continue
                
            response = dee.handle_command(user_input)
            
            if response == "exit":
                print("\nDEE: KEEP YOUR POWDER DRY, PARTNER!")
                break
                
            print(f"\nDEE: {response}")
            
        except KeyboardInterrupt:
            print("\n\nDEE: CTRL+C DETECTED. WYOMING GOODBYE!")
            break
        except EOFError:
            print("\n\nDEE: INPUT STREAM ENDED. RIDING INTO SUNSET!")
            break
        except Exception as e:
            print(f"\nDEE: SYSTEM GLITCH. WYOMING FIX: {str(e).upper()}")
