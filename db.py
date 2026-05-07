duties = [
    {
        "identifier": 5, 
        "description": "Build and operate a continuous Integration (CI) capability, employing version control of source code and related artifacts"
    },
    {
        "identifier": 7, 
        "description": "Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)"
    },
    {
        "identifier": 10, 
        "description": "Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable"
    }
]

def get_all_duties():
    return duties

def add_duty(new_duty):

    if not new_duty["identifier"]:
        return

    if not identifier_is_unique(new_duty["identifier"]):
        return

    duties.append(new_duty)

def identifier_is_unique(identifier):
    for duty in duties:
        if duty["identifier"] == identifier:
            return False
    
    return True
