from utils.automate_browser import load_session_data, save_session_data

work_data = {
    "urls": [
        "https://www.atlassian.com/software/jira",
        "https://github.com/"
    ],
    "apps": [
        "windows terminal",
        "discord"
    ]
}

# save_session_data(work_data)

new_data = load_session_data()

print(new_data)


