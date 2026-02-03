# Write a program that handles multiple exceptions (ValueError, TypeError, FileNotFoundError, ZeroDivisionError).

def heavy_code(a, b, file_name):
    try:
        
        add = a+b
        div = a/b
    
        with open("output.txt", 'w') as file:
            file.write(f"This is output.txt file {add}   ----    {div}")
        

    except ValueError as err:
        print(err)
    
    except TypeError as err:
        print(err)
    
    except FileNotFoundError as err:
        print(err)
    
    except ZeroDivisionError as err:
        print(err)
    else:
        return add, div
    finally:
        print("Finally called")

# print(heavy_code(12, 8, "output.txt"))
# print(heavy_code(12, 0, "output.txt"))
# print(heavy_code(12, '1', "output.txt"))
print(heavy_code(12, 1, "output.txt"))


    
