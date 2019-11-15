import webbrowser

def start_fb(x): 
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://www.facebook.com")
    return """in func """ + x

def start_yt(x): 
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://www.youtube.com")
    return """in func """ + x


def start_kodi(x): 
    return """in func """ + x

ras_actions= {
                "start_browsing": 
                    {
                        "name": "Start Browser", 
                        "func": lambda x: "WIP: in func " + x
                    }
                ,  
                "play_music": 
                    {
                        "name": "Play Music", 
                        "func": lambda x: "WIP: in func " + x
                    }
                , 
                "start_kodi": 
                    {
                        "name": "Start Kodi", 
                        "func": start_kodi
                    }
                , 
                "go_to_youtube": 
                    {
                        "name": "Start YouTube", 
                        "func": start_yt
                    }
                , 
                "start_facebook": 
                    {
                        "name": "Start Facebook", 
                        "func": start_fb
                    }
            }
