def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ""
    firstline = ""
    secondline = ""
    dashesline = ""
    answerline = ""

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for pm in problems:
        operand1, operator, operand2 = pm.split()

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if len(operand1) > 4 or len(operand2) > 4:  
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(operand1), len(operand2))

        firstline += operand1.rjust(max_length + 2) + "    "
        secondline += operator + operand2.rjust(max_length + 1) + "    "
        dashesline += '-' * (max_length + 2) + "    "

        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answerline += answer.rjust(max_length + 2) + "    "

    arranged_problems = firstline.rstrip() + "\n" + secondline.rstrip() + "\n" + dashesline.rstrip()
    if show_answers:
        arranged_problems += "\n" + answerline.rstrip()

    return arranged_problems

