import dash # type: ignore
from dash import dcc # type: ignore
from dash import html # type: ignore
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
import numpy as np
import plotly.graph_objects as go

mouse_data = pd.read_csv('Mouse_metadata.csv')
study_results = pd.read_csv('Study_results.csv')
merged_df = pd.merge(mouse_data, study_results, on = 'Mouse ID')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)



# --------------------------------------------------------------------------------------------------------------

#											PART 1: DESIGN PARAMETERS

# --------------------------------------------------------------------------------------------------------------
# Here we will set the colors, margins, DIV height&weight and other parameters

color_choices = {
	'light-blue': '#7FAB8',
	'light-grey': '#F7EFED',
	'light-red':  '#F1485B',
	'dark-blue':  '#33546D',
	'middle-blue': '#61D4E2'
}

drug_colors = {
	'Placebo':		'#29304E',
	'Capomulin':	'#27706B',
	'Ramicane':		'#71AB7F',
	'Ceftamin':		'#9F4440',
	'Infubinol':	'#FFD37B',
	'Ketapril':		'#FEADB9',
	'Naftisol':		'#B3AB9E',
	'Propriva':		'#ED5CD4',
	'Stelasyn':		'#97C1DF',
	'Zoniferol':	'#8980D4'
}

colors = {
		'full-background':		color_choices['light-grey'],
		'chart-background':		color_choices['light-grey'],
		'histogram-color-1':	color_choices['dark-blue'],
		'histogram-color-2':	color_choices['light-red'],
		'block-borders':		color_choices['dark-blue']
}

margins = {
		'block-margins': '8px 8px 8px 8px',
		'block-margins-short': '4px 4px 2px 4px'
}

sizes = {
		 'subblock-heights': '250px'
}



# --------------------------------------------------------------------------------------------------------------

#											PART 2: ACTUAL LAYOUT

# --------------------------------------------------------------------------------------------------------------
# Here we will set the DIV-s and other parts of our layout
# We need to have a 2x2 grid
# I have also included 1 more grid on top of others, where we will show the title of the app



# -------------------------------------------------------------------------------------- DIV for TITLE
div_title = html.Div(children =	html.H1('Mouse Experiment'),
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'center'
							}
                     )



# -------------------------------------------------------------------------------------- DIV for first raw (1.1 and 1.2)
div_1_1_button = dcc.Checklist(
                id='weight-histogram-checklist',
                options=[
                    {'label': drug, 'value': drug} for drug in np.unique(mouse_data['Drug Regimen'])
                ],
                value=['Placebo'],
                labelStyle={'display': 'inline-block'}
)

div_1_1_graph = dcc.Graph(
                id='weight-histogram',
            )

div_1_1 = html.Div(children = [div_1_1_button, div_1_1_graph],
				   style={
					   'border': '1px {} solid'.format(colors['block-borders']),
					   'margin': margins['block-margins'],
					   'width': '50%',
					   # 'height': sizes['subblock-heights'],
				   })



# -------------------------------------------------------------------------------------- DIV for first raw (1.1 and 1.2)
div_1_2_button = dcc.RadioItems(
                id='weight-histogram-radioitem',
                options=[
                    {'label': drug, 'value': drug} for drug in np.unique(mouse_data['Drug Regimen'])
                ],
                value='Placebo',
                labelStyle={'display': 'inline-block'}
)

div_1_2_graph = dcc.Graph(
                id='weight-histogram-radio',

            )

div_1_2 = html.Div(children = [div_1_2_button, div_1_2_graph],
				   style={
					   'border': '1px {} solid'.format(colors['block-borders']),
					   'margin': margins['block-margins'],
					   'width': '50%',
					   # 'height': sizes['subblock-heights'],
				   })



# Collecting DIV 1.1 and 1.2 into the DIV of first raw.
# Pay attention to the 'display' and 'flex-flaw' attributes.
# With this configuration you are able to let the DIV-s 1.1 and 1.2 be side-by-side to each other.
# If you skip them, the DIV-s 1.1 and 1.2 will be ordered as separate rows.
# Pay also attention to the 'width' attributes, which specifiy what percentage of full row will each DIV cover.
div_raw1 = html.Div(children=[div_1_1, div_1_2],
                    style={
                        'border': '3px {} solid'.format(colors['block-borders']),
                        'margin': margins['block-margins'],
                        'display': 'flex',
                        'flex-wrap': 'wrap'
                    })


# -------------------------------------------------------------------------------------- DIV for second raw (2.1 and 2.2)
div_2_1_button = dcc.Checklist(
                id='weight-histogram-group',
                options=[
                    {'label': drug, 'value': drug} for drug in np.unique(mouse_data['Drug Regimen'])
                ],
                value=['Placebo'],
                labelStyle={'display': 'inline-block'}
)

div_2_1_graph = dcc.Graph(
                id='weight-histogram-g',

            )

div_2_1 = html.Div(children = [div_2_1_button, div_2_1_graph],
				   style={
					   'border': '1px {} solid'.format(colors['block-borders']),
					   'margin': margins['block-margins'],
					   'width': '50%',
					   # 'height': sizes['subblock-heights'],
				   })


div_2_2_button = dcc.Checklist(
                id='weight-histogram-linechart',
                options=[
                    {'label': drug, 'value': drug} for drug in np.unique(mouse_data['Drug Regimen'])
                ],
                value=['Placebo'],
                labelStyle={'display': 'inline-block'}
)

div_2_2_graph = dcc.Graph(
                id='weight-histogram-l',

            )

div_2_2 = html.Div(children = [div_2_2_button, div_2_2_graph],
				   style={
					   'border': '1px {} solid'.format(colors['block-borders']),
					   'margin': margins['block-margins'],
					   'width': '50%',
					   # 'height': sizes['subblock-heights'],
				   })


div_raw2 = html.Div(children=[div_2_1, div_2_2],
                    style={
                        'border': '3px {} solid'.format(colors['block-borders']),
                        'margin': margins['block-margins'],
                        'display': 'flex',
                        'flex-wrap': 'wrap'
                    })

# -------------------------------------------------------------------------------------- Collecting all DIV-s in the final layout
# Here we collect all DIV-s into a final layout DIV

# -------------------------------------------------------------------------------------- Collecting all DIV-s in the final layout
# Here we collect all DIV-s into a final layout DIV
app.layout = html.Div(	[div_title,
    html.Div(children=[div_1_1, div_1_2], style={'display': 'flex'}),
    html.Div(children=[div_2_1, div_2_2], style={'display': 'flex'})
                              ],
						style = {
							'backgroundColor': colors['full-background']
						}
					)


# histogram of mice weights' for each drug
# it is a stacked histogram which lets us put histograms on top of each other

# Chart 1
@app.callback(
    Output(component_id='weight-histogram', component_property='figure'),
        [Input(component_id='weight-histogram-checklist', component_property='value')]
)
def update_weight_histogram(drug_names):
    traces = []

    for drug in drug_names:
        traces.append(go.Histogram(x=mouse_data[mouse_data['Drug Regimen'] == drug]['Weight (g)'],
                                   name=drug,
                                   opacity=0.9,
                                   marker=dict(color=drug_colors[drug]))
                      )

    return {
        'data': traces,
        'layout': dict(
            barmode='stack',
            xaxis={'title': 'mouse weight',
                   'range': [merged_df['Weight (g)'].min(), merged_df['Weight (g)'].max()],
                   'showgrid': False
                   },
            yaxis={'title': 'number of mice',
                   'showgrid': False,
                   'showticklabels': True
                   },
            autosize=False,
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},

            legend={'x': 0, 'y': 1},
        )
    }

# Chart 2
@app.callback(
        Output(component_id='weight-histogram-radio', component_property='figure'),
        [Input(component_id='weight-histogram-radioitem', component_property='value')]
)
def update_weight_distribution(drug_names):
    # Overall weight distribution
    overall_weights = mouse_data['Weight (g)']
    overall_hist, overall_bins = np.histogram(overall_weights, bins=30, density=True)

    traces = []

    for drug in drug_names:
        drug_weights = mouse_data[mouse_data['Drug Regimen'] == drug]['Weight (g)']
        drug_hist, _ = np.histogram(drug_weights, bins=overall_bins, density=True)

        traces.append(go.Histogram(x=drug_weights['Weight (g)'],
                                   name=drug,
                                   opacity=0.9,
                                   marker=dict(color=drug_colors[drug])))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'mouse weight', 'showgrid': False},
            yaxis={'title': 'number of mice', 'showgrid': False},
            autosize=False,
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
        )
    }

# Chart 3
@app.callback(
        Output(component_id='weight-histogram-g', component_property='figure'),
        [Input(component_id='weight-histogram-group', component_property='value')]
)
def update_survival_over_weight(drug_names):
    traces = []
    for drug in drug_names:
        drug_data = merged_df[merged_df['Drug Regimen'] == drug]
        weights = sorted(drug_data['Weight (g)'].unique())
        num_mice = []

        for weight in weights:
            num_mice_at_weight = len(drug_data[drug_data['Weight (g)'] == weight])
            num_mice.append(num_mice_at_weight)

        traces.append(go.Histogram(x=merged_df[merged_df['Drug Regimen'] == drug]['Weight (g)'],
                                   name=drug,
                                   opacity=0.9,
                                   marker=dict(color=drug_colors[drug])))
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'mouse weight', 'showgrid': False},
            yaxis={'title': 'number of mice', 'showgrid': False},
            autosize=False,
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
        )
    }

# Chart 4
@app.callback(
        Output(component_id='weight-histogram-l', component_property='figure'),
        [Input(component_id='weight-histogram-linechart', component_property='value')]
)
def update_survival_over_time_chart(drug_names):
    traces = []
    for drug in drug_names:
        drug_data = merged_df[merged_df['Drug Regimen'] == drug]
        time_points = sorted(drug_data['Timepoint'].unique())
        num_alive_mice = []

        for time_point in time_points:
            num_alive = len(drug_data[drug_data['Timepoint'] == time_point])
            num_alive_mice.append(num_alive)

        traces.append(go.Scatter(x=time_points, y=num_alive_mice,
                                 mode='lines',
                                 name=drug))
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'time point', 'showgrid': False},
            yaxis={'title': 'number of alive mice', 'showgrid': False},
            autosize=False,
            paper_bgcolor=colors['chart-background'],
            plot_bgcolor=colors['chart-background'],
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
        )
    }




# --------------------------------------------------------------------------------------------------------------

#											PART 4: RUNNING THE APP

# --------------------------------------------------------------------------------------------------------------
# >> use __ debug=True __ in order to be able to see the changes after refreshing the browser tab,
#			 don't forget to save this file before refreshing
# >> use __ port = 8081 __ or other number to be able to run several apps simultaneously
if __name__ == '__main__':
    app.run_server(debug=True,
                   # port = 8081, host = '0.0.0.0')
                   )