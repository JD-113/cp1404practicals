"""Project management program."""
from prac_07.project import Project
import datetime

MENU = ("Menu:\n(L)oad projects\n(S)ave projects\n(D)isplay project\n(F)ilter projects by date\n(A)dd new project"
        "\n(U)pdate project\n(Q)uit")


def main():
    """Main program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == 'L':
            inject_file = input("Filename to load projects from: ")
            projects = load_projects(inject_file)
        elif choice == 'S':
            save_file = input("Filename to save projects to: ")
            save_projects(save_file, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            get_updated_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save = input("Would you like to save to projects.txt? ")
    if save.lower().startswith('y'):
        save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")


def get_updated_project(projects):
    for i, project in enumerate(projects):
        print(f'{i} {project.name}, start: {project.start_date}, priority {project.priority}, '
              f'estimate: ${project.cost}, completion: {project.completion}%')
    choice = int(input('Project choice: '))
    print(
        f'{projects[choice].name}, start: {projects[choice].start_date}, priority {projects[choice].priority},'
        f' estimate: ${projects[choice].cost}, completion: {projects[choice].completion}%')
    update_project(projects[choice])


def load_projects(inject_file):
    projects = []
    with open(inject_file, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to out_file."""
    with open(filename, 'w') as out_file:
        out_file.write('Name	Start Date	Priority	Cost Estimate	Completion Percentage\n')
        for project in projects:
            out_file.write(project.__str__() + '\n')


def display_projects(projects):
    """Display incomplete and complete projects based on the completeness parameter."""
    print('Incomplete projects:')
    for project in projects:
        if not project.is_complete():
            print(f'{project.name}, start: {project.start_date}, priority {project.priority}, '
                  f'estimate: ${project.cost}, completion: {project.completion}%')

    # Display complete projects
    print('Complete projects:')
    for project in projects:
        if project.is_complete():
            print(f'{project.name}, start: {project.start_date}, priority {project.priority}, '
                  f'estimate: ${project.cost}, completion: {project.completion}%')


def filter_projects_by_date(projects):
    """Display projects after a specified date."""
    date = get_date()
    for project in projects:
        if project.started_date(date):
            print(f'{project.name}, start: {project.start_date}, priority {project.priority}, '
                  f'estimate: ${project.cost}, completion: {project.completion}%')


def update_project(project):
    project.completion = get_valid_number("New Percentage: ", int)
    project.priority = get_valid_number("New Priority: ", int)


def add_new_project(projects):
    new_project = []
    name = input("Name: ")
    start_date = get_date()
    priority = get_valid_number("Priority: ", int)
    cost = get_valid_number("Cost estimate: ", float)
    complete = get_valid_number("Percent complete: ", int)
    new_project.append(Project(name, start_date, priority, cost, complete))
    projects.append(new_project)


def get_valid_number(prompt, variable_type):
    """Get a valid number."""
    is_valid = False
    while not is_valid:
        try:
            number = variable_type(input(prompt))
            if number > 0:
                is_valid = True
                return number
            else:
                print("Number must be > 0")
        except ValueError:
            print("Input can not be blank")
        except TypeError:
            print("Invalid input; enter a valid number")


def get_date():
    """Get date."""
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return date


if __name__ == "__main__":
    main()
