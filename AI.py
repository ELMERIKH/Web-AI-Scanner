import json
from llamaapi import LlamaAPI

class consultantAI:
    def read_report(self,file_path):
        with open(file_path, 'r') as file:
            report_content = file.read()
        return report_content

    def generate_solution(self,prompt):
         

        # Initialize the SDK
        llama = LlamaAPI("LL-pz8hwhHY8l0wNtEJiQf7ezLA4kQNTCYir5HkwMTQf4XCmaUgmOykPgJdLlU6qjAV")

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
        response = llama.run(api_request_json)
        response_data = response.json()

        print(json.dumps(response.json(), indent=2))
        message_content = response_data['choices'][0]['message']['content']

        return message_content

