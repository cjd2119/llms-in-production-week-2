PROMPT = """

Generate a valid SQL query for the following natural language instruction:

${nl_instruction}

Only generate SQL code and nothing else. Do not use any line breaks, the output should be a single line.
Name all columns but do not make their names longer than necessary.

Suppose I receive the instructions: Show departments that have more than 10 employees.,
I would want my SQL query to be: SELECT department FROM employees GROUP BY department HAVING COUNT(*) > 10;

${gr.complete_json_suffix}
"""
