import logic2048

if __name__ == '__main__':
    mat = logic2048.start_game()

print(mat)
while(True):
    x = input("Press the command: ")
    if(x == 'W' or x == 'w'):
        mat, flag = logic2048.move_up(mat)
        status = logic2048.get_current_status(mat)
        if(status == 'Game not over'):
            logic2048.add_new_2(mat)
        else:
            break

    elif (x == 'S' or x == 's'):
        mat, flag = logic2048.move_down(mat)
        status = logic2048.get_current_state(mat)
        print(status)
        if (status == 'Game not over'):
            logic2048.add_new_2(mat)
        else:
            break

    elif (x == 'A' or x == 'a'):
        mat, flag = logic2048.move_left(mat)
        status = logic2048.get_current_state(mat)
        print(status)
        if (status == 'Game not over'):
            logic2048.add_new_2(mat)
        else:
            break

        # to move right
    elif (x == 'D' or x == 'd'):
        mat, flag = logic2048.move_right(mat)
        status = logic2048.get_current_state(mat)
        print(status)
        if (status == 'Game not over'):
            logic2048.add_new_2(mat)
        else:
            break
    else:
        print("Invalid Key Pressed")

    print(mat)