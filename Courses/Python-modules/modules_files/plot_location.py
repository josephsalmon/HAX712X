import pygal                                                       # First import pygal
# from pygal.maps.fr import aggregate_regions


def plot_location(gd):
  fr_chart = pygal.maps.fr.Departments(human_readable=True)
  fr_chart.title = 'Accident by region'

  fr_chart.add('Accidents', gd.to_dict())

  fr_chart.render_in_browser()
  # fr_chart.render_to_file('./chart.svg')  # Write the chart in the specified file
