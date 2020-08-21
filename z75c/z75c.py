ADD = 1
REMOVE = 2
PRINT = 3
UNDO = 4
REDO = 5

history = [['', 0]]
current_index = -1


def BastShoe(command):
    global current_index
    global history
    code = int(command[0])
    arg = command[2:]
    current_string = history[current_index][0]
    if code == ADD:
        result = current_string + arg
        if current_index != -1:
            history = [history[current_index]]
            current_index = -1
        history.append([result, ADD])
        return result
    elif code == REMOVE:
        symbols_to_delete = int(arg)
        result = current_string[0:-symbols_to_delete]
        if current_index != -1:
            history = [history[current_index]]
            current_index = -1
        history.append([result, REMOVE])
        return result
    elif code == PRINT:
        index = int(arg)
        if len(current_string) <= index:
            result = ''
        else:
            result = current_string[index]
        return result
    elif code == UNDO:
        current_index -= 1
        if current_index < -len(history):
            current_index = -len(history)
        result = history[current_index][0]

        return result
    elif code == REDO:
        current_index += 1
        if current_index >= 0:
            current_index = -1
        return history[current_index][0]
    else:
        return current_string
