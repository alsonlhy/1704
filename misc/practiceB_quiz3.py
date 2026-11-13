def get_project_summaries(projects):
    summaries = []

    for project in projects:
        name = project[0]
        completed = []
        pending = 0

        for task in project[1]:
            if task[1]:
                completed.append(task[0])
            else:
                pending += 1

        summaries.append((name, completed, pending))

    return summaries



def display_project_summaries(projects):

    new_lst = get_project_summaries(projects)

    print("Project task summary: ")

    for project in new_lst:

        if project[2] > 0:
            pending = project[2]
        else:
            pending = "No"
        print(project[0] + ":" + " Completed tasks " + project[1] + "- " + pending + "pending task")

print(get_project_summaries([('Website', [('Design', True), ('Testing', False), ('Launch', False)])]))