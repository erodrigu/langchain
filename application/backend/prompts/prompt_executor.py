class PromptExecutor:
    def __init__(self, model, prompts):
        self.model = model
        self.prompts = prompts

    def execute_prompts(self):
        outputs = []        
        for prompt in self.prompts:
            output = self.model.run_prompt(prompt)
            outputs.append(output)
        return outputs
