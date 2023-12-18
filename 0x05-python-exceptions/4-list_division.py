#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    elements = []
    for i in range(list_length):
        try:
            elements.append(my_list_1[i]/my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            elements.append(0)
        except ZeroDivisionError:
            print("division by 0")
            elements.append(0)
        except IndexError:
            print("out of range")
            elements.append(0)
        finally:
            pass
    return (elements)
