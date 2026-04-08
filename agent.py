def web_agent():
    print("Web Agent: Fetching data from web...")
    return "Data fetched"

def task_agent(data):
    print("Task Agent: Processing data...")
    return f"Task completed using {data}"

def main_agent():
    data = web_agent()
    result = task_agent(data)
    print("Final Output:", result)

if _name_ == "_main_":
    main_agent()
