from nicegui import app, ui
from utils.languages_file import languages

language_list=[]
for language in languages:
    language_list.append(language["name"])

app.native.window_args["resizable"]=False
app.native.start_args["debug"]=True

@ui.page("/existing_project")
def existing_project():
    ui.button("Go Back",on_click=ui.navigate.back)
    ui.label("Get Access to an Existing Language")
    ui.select(options=language_list,label="Select a Language",with_input=True)
    ui.checkbox("Add Language to NVDA")
    ui.checkbox("Download File to add to NVDA")
    ui.checkbox("Download Language Spreadsheet")
    ui.button("Next")

@ui.page("/contribute_existing")
def contribute_existing():
    ui.button("Go Back",on_click=ui.navigate.back)
    ui.label("Contribute to an Existing Project")

@ui.page("/create_project")
def create_project():
    ui.button("Go Back",on_click=ui.navigate.back)
    ui.label("Create New Project")

ui.label("What do you want to do?")
ui.link("Get Access to Existing Project",existing_project)
ui.link("Contribute to Existing Project",contribute_existing)
ui.link("Create a New Project",create_project)

ui.run(native=True,window_size=(400,300),fullscreen=False,title="example")