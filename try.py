import ollama
output=ollama.generate("llama3.2:3b",
                       f"Create a intermediate math problem without text. Provide the problem in the first section labeled 'Problem', "
                        f"the correct answer as numbers only with no sign in the second section labeled 'Correct Answer', and a step-by-step explanation last section labeled 'explanation'."
                        )

print(output)
print(output['response'])