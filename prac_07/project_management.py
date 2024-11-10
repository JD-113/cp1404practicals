"""Project management program."""
from prac_07.project import Project
from datetime import datetime

MENU = ("Menu:\n(L)oad projects\n(S)ave projects\n(D)isplay projectsn\n(F)ilter projects by date\n(A)dd new project"
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
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save = input("Would you like to save to projects.txt? ")
    if save.lower().startswith('y'):
        save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")




if __name__ == "__main__":
    main()
