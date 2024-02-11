import json
from llamaapi import LlamaAPI

class consultantAI:
    def read_report(self,file_path):
        with open(file_path, 'r') as file:
            report_content = file.read()
        return report_content

    def generate_solution(self,prompt):
         

        # Initialize the SDK
        llama = LlamaAPI("")

        # Build the API request
        api_request_json = {
            "messages": [
                {"role": "user", "content": "your a web security consultant give solutions and feedback give answer in a minimized adn organized way alwyas use icons  "},
                {"role": "user", "content": prompt},  # Add the prompt to the messages

            ],
          
            
            "stream": False,
            "function_call": "get_current_weather",
        }

        # Execute the Request
        try:
            response = llama.run(api_request_json)
            response_data = response.json()
            message_content = response_data['choices'][0]['message']['content']
            return message_content
        except Exception as e:
            if "api key invalid" in str(e).lower():
                print("API key invalid")
            else:
                print("An error occurred:", e)
            return None

