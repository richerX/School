def main():
    return 0



if __name__ == "__main__":
    try:
        main()
    except Exception as critical_exception:
        error_log_filepath = "Error log"
        with open(f"{error_log_filepath}.txt", "a", encoding = "utf-8") as file:
            traceback.print_exception(*sys.exc_info(), file = file)
    input("Для завершения нажмите Enter...")
