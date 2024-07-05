import json
import logging


logging.basicConfig(filename='bot_steps.html', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def step(step):
    with open("common/decorators/steps.json", 'r') as f:
        steps = json.load(f)
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                step_description = steps.get(step, "Unknown step")
                log_message = f"Step {step}: {step_description}..."
                log_div = f"<div class='success'><span class='ball'>&#x1F7E2;</span> Step {step}: {step_description}...</div>"
                log_entry = f"INFO - {log_div}"
                print(log_message)
                logging.info(log_entry)
                return func(*args, **kwargs)
            except Exception as e:
                step_description = steps.get(step, "Unknown step")
                error_message = f"Error on step {step}: {step_description}: {e}"
                error_div = f"<div class='error'><span class='ball'>&#x1F534;</span> Error on step {step}: {step_description}</div>"
                error_details = f"<ul><li>{e}</li></ul>"
                error_log_entry = f"ERROR - {error_div}{error_details}"
                print(error_message)
                logging.error(error_log_entry)
        return wrapper
    return decorator