from consola import iniciar_programa


if __name__ == "__main__":
    try:
        iniciar_programa()
    except(keyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
        
        
#TERMINADO