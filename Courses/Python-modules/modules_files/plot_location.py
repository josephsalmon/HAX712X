import pygal  # First import pygal

# from pygal.maps.fr import aggregate_regions


def plot_location(gd):
    fr_chart = pygal.maps.fr.Departments(human_readable=True)
    fr_chart.title = "Accident by region"
    fr_chart.add("Accidents", gd.to_dict())
    fr_chart.render_to_file(
        "./biketrauma_map.svg"
    )  # Save chart in specified file; open it in the browser to visualize

    # fr_chart.render_in_browser() # might not work with most viewers...
