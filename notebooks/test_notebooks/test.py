


# # documentation link https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Container/Layout-widgets

# import ipywidgets as widgets
# from ipywidgets import FileUpload
# from IPython.display import display
# from IPython.core.display import display, HTML

# # These variables should be set using a GUI

# # path to the db that contains the data
# # database_path = "/home/craigsanders/persistent/private-90d/data_collection_analysis_tutorial.db"
# database_path = "/home/ecortez/persistent/private-90d/data_collection_analysis_tutorial.db"
# # plotting options
# # xlabel = "Angle (degrees)"
# # ylabel = "Detection Probability"
# # yes_label = "Detected Trial"
# t_level = 0.75
# cred_level = 0.95# no_label = "Undetected Trial"
# # targe


# # This should run whenever a new db is uploaded
# serv = AEPsychServer(database_path=database_path)
# strat = serv.get_strat_from_replay()

# #====================== CSS Style ====================
# # inputStyl = { border="2px solid red"}

# #====================== inputs ======================
# display(HTML('<h1 style="text-align: center;">AEPsych Visualization tool</h1>'))

# # File upload
# uploader = FileUpload(
#     description="Resume Session",
#     accept=".db",
#     multiple=False
#     )


# # Outcome Labels O and 1
# outcome_label = widgets.Label(value='Outcome Labels:')
# display(outcome_label)

# inputZero = widgets.Dropdown(
#     options=[('Yes Trial', "Detected Trial"), ('No Trial', "Undetected Trial")],
#     value="Detected Trial",
#     description='0:',
# )
# inputOne = widgets.Dropdown(
#     options=[ ('No Trial', "Undetected Trial"), ('Yes Trial', "Detected Trial")],
#     value="Undetected Trial",
#     description='1:',
# )

# # Float inputs
# target_level = widgets.BoundedFloatText(
#     value=0.75,
#     min=0,
#     max=1,
#     step=0.1,
#     description='target_level:',
#     disabled=False
# )

# cred_level = widgets.BoundedFloatText(
#     value=0.95,
#     min=0,
#     max=1,
#     step=0.1,
#     description='cred_level:',
#     disabled=False
# )

# # X and Y axis labels

# xlabel = widgets.Text(
#     value='Angle (degrees)',
#     placeholder='x axis',
#     description='xlabel:',
#     disabled=False
# )

# ylabel = widgets.Text(
#     value='Detection Probability',
#     placeholder='y axis',
#     description='ylabel:',
#     disabled=False
# )

# # Updated with .interact decorator
# @widgets.interact(
#     uploader=uploader,
#     inputZero=inputZero,
#     inputOne=inputOne,
#     target_level=target_level,
#     cred_level=cred_level,
#     xlabel=xlabel,
#     ylabel=ylabel
#     )
# def generatePlot(uploader, inputZero, inputOne,  target_level, cred_level, xlabel, ylabel):
#     # This should run whenever the user wants to generate a new plot
#     print("Session file data", uploader)
#     return plot_strat(strat, xlabel=xlabel, ylabel=ylabel, yes_label=inputOne, no_label=inputZero, cred_level=cred_level, target_level=target_level)


# # WITH .interactive
# # This should run whenever the user wants to generate a new plot
# # def update_plot(uploader,
# #     inputZero,
# #     inputOne,
# #     target_level,
# #     cred_level,
# #     xlabel,
# #     ylabel):
# #     """
# #     this funtion is linked to the inputs and it replots
# #     the graph when the inputs are changed.
# #     """
# #     print("Upload data:", uploader)
# #     return plot_strat(strat, xlabel=xlabel, ylabel=ylabel, yes_label=yes_label, no_label=no_label, cred_level=cred_level, target_level=target_level)


# # widgets.interactive(update_plot, uploader=uploader,
# #     inputZero=inputZero,
# #     inputOne=inputOne,
# #     target_level=target_level,
# #     cred_level=cred_level,
# #     xlabel=xlabel,
# #     ylabel=ylabel )
