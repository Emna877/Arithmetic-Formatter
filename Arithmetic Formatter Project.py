def arithmetic_arranger(problems, show_answers=False):
    # Error handling
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    results = []
    max_lengths = []
    
    # Iterate through each problem and split into parts
    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]
        
        # Validate the operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        # Validate the operands (only digits)
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Validate the operand length (max 4 digits)
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the result if show_answers is True
        if show_answers:
            if operator == "+":
                result = str(int(first_operand) + int(second_operand))
            elif operator == "-":
                result = str(int(first_operand) - int(second_operand))
        else:
            result = ""
        
        # Find the maximum length of the operands and result
        max_length = max(len(first_operand), len(second_operand)) + 2
        
        # Store the parts and maximum length
        first_operands.append(first_operand.rjust(max_length))
        second_operands.append(operator + " " + second_operand.rjust(max_length - 2))
        results.append(result.rjust(max_length))
        max_lengths.append(max_length)
    
    # Build the arranged problems
    first_line = "    ".join(first_operands)
    second_line = "    ".join(second_operands)
    dashes = "    ".join(["-" * length for length in max_lengths])
    arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    
    # Add the results line if show_answers is True
    if show_answers:
        results_line = "    ".join(results)
        arranged_problems += "\n" + results_line
    
    return arranged_problems