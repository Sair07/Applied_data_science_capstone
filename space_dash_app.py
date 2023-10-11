{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red194\green126\blue101;\red140\green211\blue254;\red70\green137\blue204;\red67\green192\blue160;
\red167\green197\blue152;\red212\green214\blue154;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c80784\c56863\c47059;\cssrgb\c61176\c86275\c99608;\cssrgb\c33725\c61176\c83922;\cssrgb\c30588\c78824\c69020;
\cssrgb\c70980\c80784\c65882;\cssrgb\c86275\c86275\c66667;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Import required libraries\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  pandas \cf5 \strokec5 as\cf4 \strokec4  pd\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  dash\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  dash_html_components \cf5 \strokec5 as\cf4 \strokec4  html\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  dash_core_components \cf5 \strokec5 as\cf4 \strokec4  dcc\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  dash.dependencies \cf5 \strokec5 import\cf4 \strokec4  Input, Output\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  plotly.express \cf5 \strokec5 as\cf4 \strokec4  px\cb1 \
\
\cf2 \cb3 \strokec2 # Read the airline data into pandas dataframe\cf4 \cb1 \strokec4 \
\cb3 spacex_df = pd.read_csv(\cf6 \strokec6 "spacex_launch_dash.csv"\cf4 \strokec4 )\cb1 \
\cb3 max_payload = spacex_df[\cf6 \strokec6 'Payload Mass (kg)'\cf4 \strokec4 ].max()\cb1 \
\cb3 min_payload = spacex_df[\cf6 \strokec6 'Payload Mass (kg)'\cf4 \strokec4 ].min()\cb1 \
\cb3 launch_sites_df = spacex_df.groupby([\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ], \cf7 \strokec7 as_index\cf4 \strokec4 =\cf8 \strokec8 False\cf4 \strokec4 ).first()\cb1 \
\cb3 launch_sites_df = launch_sites_df[[\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ]]\cb1 \
\cb3 launchsite = \cf9 \strokec9 list\cf4 \strokec4 (launch_sites_df[\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ])\cb1 \
\
\cf2 \cb3 \strokec2 # Create a dash application\cf4 \cb1 \strokec4 \
\cb3 app = dash.Dash(\cf7 \strokec7 __name__\cf4 \strokec4 )\cb1 \
\
\cf2 \cb3 \strokec2 # Create an app layout\cf4 \cb1 \strokec4 \
\cb3 app.layout = html.Div(\cf7 \strokec7 children\cf4 \strokec4 =[html.H1(\cf6 \strokec6 'SpaceX Launch Records Dashboard'\cf4 \strokec4 ,\cb1 \
\cb3                                         \cf7 \strokec7 style\cf4 \strokec4 =\{\cf6 \strokec6 'textAlign'\cf4 \strokec4 : \cf6 \strokec6 'center'\cf4 \strokec4 , \cf6 \strokec6 'color'\cf4 \strokec4 : \cf6 \strokec6 '#503D36'\cf4 \strokec4 ,\cb1 \
\cb3                                                \cf6 \strokec6 'font-size'\cf4 \strokec4 : \cf10 \strokec10 40\cf4 \strokec4 \}),\cb1 \
\cb3                                 \cf2 \strokec2 # TASK 1: Add a dropdown list to enable Launch Site selection\cf4 \cb1 \strokec4 \
\cb3                                 \cf2 \strokec2 # The default select value is for ALL sites\cf4 \cb1 \strokec4 \
\cb3                                 dcc.Dropdown(\cf7 \strokec7 id\cf4 \strokec4 =\cf6 \strokec6 'site-dropdown'\cf4 \strokec4 ,  \cf7 \strokec7 options\cf4 \strokec4 =[\cb1 \
\cb3                                     \{\cf6 \strokec6 'label'\cf4 \strokec4 : \cf6 \strokec6 'All Sites'\cf4 \strokec4 , \cf6 \strokec6 'value'\cf4 \strokec4 : \cf6 \strokec6 'ALL'\cf4 \strokec4 \},\cb1 \
\cb3                                     \{\cf6 \strokec6 'label'\cf4 \strokec4 : launchsite[\cf10 \strokec10 0\cf4 \strokec4 ], \cf6 \strokec6 'value'\cf4 \strokec4 : launchsite[\cf10 \strokec10 0\cf4 \strokec4 ]\},\cb1 \
\cb3                                     \{\cf6 \strokec6 'label'\cf4 \strokec4 : launchsite[\cf10 \strokec10 1\cf4 \strokec4 ], \cf6 \strokec6 'value'\cf4 \strokec4 : launchsite[\cf10 \strokec10 1\cf4 \strokec4 ]\},\cb1 \
\cb3                                     \{\cf6 \strokec6 'label'\cf4 \strokec4 : launchsite[\cf10 \strokec10 2\cf4 \strokec4 ], \cf6 \strokec6 'value'\cf4 \strokec4 : launchsite[\cf10 \strokec10 2\cf4 \strokec4 ]\},\cb1 \
\cb3                                     \{\cf6 \strokec6 'label'\cf4 \strokec4 : launchsite[\cf10 \strokec10 3\cf4 \strokec4 ], \cf6 \strokec6 'value'\cf4 \strokec4 : launchsite[\cf10 \strokec10 3\cf4 \strokec4 ]\},\cb1 \
\cb3                                     ],\cb1 \
\cb3                                     \cf7 \strokec7 value\cf4 \strokec4  = \cf6 \strokec6 'ALL'\cf4 \strokec4 ,\cb1 \
\cb3                                     \cf7 \strokec7 placeholder\cf4 \strokec4 =\cf6 \strokec6 'Select a Launch Site here'\cf4 \strokec4 ,\cb1 \
\cb3                                     \cf7 \strokec7 searchable\cf4 \strokec4 =\cf8 \strokec8 True\cf4 \cb1 \strokec4 \
\cb3                                     ),\cb1 \
\cb3                                 html.Br(),\cb1 \
\
\cb3                                 \cf2 \strokec2 # TASK 2: Add a pie chart to show the total successful launches count for all sites\cf4 \cb1 \strokec4 \
\cb3                                 \cf2 \strokec2 # If a specific launch site was selected, show the Success vs. Failed counts for the site\cf4 \cb1 \strokec4 \
\cb3                                 html.Div(dcc.Graph(\cf7 \strokec7 id\cf4 \strokec4 =\cf6 \strokec6 'success-pie-chart'\cf4 \strokec4 )),\cb1 \
\cb3                                 html.Br(),\cb1 \
\
\cb3                                 html.P(\cf6 \strokec6 "Payload range (Kg):"\cf4 \strokec4 ),\cb1 \
\cb3                                 \cf2 \strokec2 # TASK 3: Add a slider to select payload range\cf4 \cb1 \strokec4 \
\cb3                                 dcc.RangeSlider(\cb1 \
\cb3                                     \cf7 \strokec7 id\cf4 \strokec4 =\cf6 \strokec6 'payload-slider'\cf4 \strokec4 ,\cb1 \
\cb3                                     \cf7 \strokec7 min\cf4 \strokec4 =\cf10 \strokec10 0\cf4 \strokec4 , \cf7 \strokec7 max\cf4 \strokec4  =\cf10 \strokec10 10000\cf4 \strokec4 , \cf7 \strokec7 step\cf4 \strokec4 = \cf10 \strokec10 1000\cf4 \strokec4 ,\cb1 \
\cb3                                     \cf7 \strokec7 marks\cf4 \strokec4 =\{\cf10 \strokec10 0\cf4 \strokec4 :\cf6 \strokec6 '0'\cf4 \strokec4 ,\cf10 \strokec10 2500\cf4 \strokec4 :\cf6 \strokec6 '2500'\cf4 \strokec4 ,\cf10 \strokec10 5000\cf4 \strokec4 :\cf6 \strokec6 '5000'\cf4 \strokec4 ,\cf10 \strokec10 7500\cf4 \strokec4 :\cf6 \strokec6 '7500'\cf4 \strokec4 \},\cb1 \
\cb3                                     \cf7 \strokec7 value\cf4 \strokec4 =[min_payload,max_payload]),\cb1 \
\
\cb3                                 \cf2 \strokec2 # TASK 4: Add a scatter chart to show the correlation between payload and launch success\cf4 \cb1 \strokec4 \
\cb3                                 html.Div(dcc.Graph(\cf7 \strokec7 id\cf4 \strokec4 =\cf6 \strokec6 'success-payload-scatter-chart'\cf4 \strokec4 )),\cb1 \
\cb3                                 ])\cb1 \
\
\cf2 \cb3 \strokec2 # TASK 2:\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Add a callback function for `site-dropdown` as input, `success-pie-chart` as output\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Function decorator to specify function input and output\cf4 \cb1 \strokec4 \
\cf11 \cb3 \strokec11 @app.callback\cf4 \strokec4 (Output(\cf7 \strokec7 component_id\cf4 \strokec4 =\cf6 \strokec6 'success-pie-chart'\cf4 \strokec4 , \cf7 \strokec7 component_property\cf4 \strokec4 =\cf6 \strokec6 'figure'\cf4 \strokec4 ),\cb1 \
\cb3               Input(\cf7 \strokec7 component_id\cf4 \strokec4 =\cf6 \strokec6 'site-dropdown'\cf4 \strokec4 , \cf7 \strokec7 component_property\cf4 \strokec4 =\cf6 \strokec6 'value'\cf4 \strokec4 ))\cb1 \
\cf8 \cb3 \strokec8 def\cf4 \strokec4  \cf11 \strokec11 get_pie_chart\cf4 \strokec4 (\cf7 \strokec7 entered_site\cf4 \strokec4 ):\cb1 \
\cb3     filtered_df = spacex_df.groupby(\cf6 \strokec6 'Launch Site'\cf4 \strokec4 )[\cf6 \strokec6 'class'\cf4 \strokec4 ].sum().reset_index()\cb1 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  entered_site == \cf6 \strokec6 'ALL'\cf4 \strokec4 :\cb1 \
\cb3         fig = px.pie(filtered_df, \cf7 \strokec7 values\cf4 \strokec4 =\cf6 \strokec6 'class'\cf4 \strokec4 , \cb1 \
\cb3         \cf7 \strokec7 names\cf4 \strokec4 =\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ,\cb1 \
\cb3         \cf7 \strokec7 title\cf4 \strokec4 =\cf6 \strokec6 'Total Sucess Launches by site'\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  fig\cb1 \
\cb3     \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 # return the outcomes piechart for a selected site\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 for\cf4 \strokec4  site \cf5 \strokec5 in\cf4 \strokec4  launchsite:\cb1 \
\cb3             \cf5 \strokec5 if\cf4 \strokec4  site == entered_site:\cb1 \
\cb3                 data = spacex_df.groupby(spacex_df[\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ] == entered_site)[\cf6 \strokec6 'class'\cf4 \strokec4 ].sum().reset_index()\cb1 \
\cb3                 data[\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ].replace(\cf8 \strokec8 True\cf4 \strokec4 ,\cf10 \strokec10 1\cf4 \strokec4 ,\cf7 \strokec7 inplace\cf4 \strokec4  = \cf8 \strokec8 True\cf4 \strokec4 )\cb1 \
\cb3                 data[\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ].replace(\cf8 \strokec8 False\cf4 \strokec4 ,\cf10 \strokec10 0\cf4 \strokec4 ,\cf7 \strokec7 inplace\cf4 \strokec4  = \cf8 \strokec8 True\cf4 \strokec4 )\cb1 \
\cb3                 fig = px.pie(data, \cf7 \strokec7 values\cf4 \strokec4 =\cf6 \strokec6 'class'\cf4 \strokec4 ,\cf7 \strokec7 names\cf4 \strokec4 =\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ,\cb1 \
\cb3                 \cf7 \strokec7 title\cf4 \strokec4 =\cf6 \strokec6 'Total Sucess launches for \cf8 \strokec8 \{\}\cf6 \strokec6 '\cf4 \strokec4 .format(entered_site))\cb1 \
\cb3                 \cf5 \strokec5 return\cf4 \strokec4  fig\cb1 \
\cf2 \cb3 \strokec2 # TASK 4:\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output\cf4 \cb1 \strokec4 \
\
\cf11 \cb3 \strokec11 @app.callback\cf4 \strokec4 (Output(\cf7 \strokec7 component_id\cf4 \strokec4 =\cf6 \strokec6 'success-payload-scatter-chart'\cf4 \strokec4 , \cf7 \strokec7 component_property\cf4 \strokec4 =\cf6 \strokec6 'figure'\cf4 \strokec4 ),\cb1 \
\cb3     [Input(\cf7 \strokec7 component_id\cf4 \strokec4 =\cf6 \strokec6 'site-dropdown'\cf4 \strokec4 , \cf7 \strokec7 component_property\cf4 \strokec4 =\cf6 \strokec6 'value'\cf4 \strokec4 ),\cb1 \
\cb3      Input(\cf7 \strokec7 component_id\cf4 \strokec4 =\cf6 \strokec6 "payload-slider"\cf4 \strokec4 , \cf7 \strokec7 component_property\cf4 \strokec4 =\cf6 \strokec6 "value"\cf4 \strokec4 )])\cb1 \
\cf8 \cb3 \strokec8 def\cf4 \strokec4  \cf11 \strokec11 get_scatter_chart\cf4 \strokec4 (\cf7 \strokec7 entered_site\cf4 \strokec4 ,\cf7 \strokec7 payload_value\cf4 \strokec4 ):\cb1 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4  entered_site == \cf6 \strokec6 'ALL'\cf4 \strokec4 :\cb1 \
\cb3         low, high = payload_value\cb1 \
\cb3         mask = (spacex_df[\cf6 \strokec6 'Payload Mass (kg)'\cf4 \strokec4 ] > low) & (spacex_df[\cf6 \strokec6 'Payload Mass (kg)'\cf4 \strokec4 ] < high)\cb1 \
\cb3         fig = px.scatter(\cb1 \
\cb3             spacex_df[mask], \cf7 \strokec7 x\cf4 \strokec4 =\cf6 \strokec6 "Payload Mass (kg)"\cf4 \strokec4 , \cf7 \strokec7 y\cf4 \strokec4 =\cf6 \strokec6 "class"\cf4 \strokec4 , \cb1 \
\cb3             \cf7 \strokec7 color\cf4 \strokec4 =\cf6 \strokec6 "Booster Version Category"\cf4 \strokec4 ,\cb1 \
\cb3             \cf7 \strokec7 title\cf4 \strokec4 =\cf6 \strokec6 'Correlation between payload and sucess for all Sites'\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  fig\cb1 \
\cb3     \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 for\cf4 \strokec4  site \cf5 \strokec5 in\cf4 \strokec4  launchsite:\cb1 \
\cb3             \cf5 \strokec5 if\cf4 \strokec4  site == entered_site:\cb1 \
\cb3                 data = spacex_df[spacex_df[\cf6 \strokec6 'Launch Site'\cf4 \strokec4 ] == entered_site]\cb1 \
\cb3                 low, high = payload_value\cb1 \
\cb3                 mask = (data[\cf6 \strokec6 'Payload Mass (kg)'\cf4 \strokec4 ] > low) & (data[\cf6 \strokec6 'Payload Mass (kg)'\cf4 \strokec4 ] < high)\cb1 \
\cb3                 fig = px.scatter(\cb1 \
\cb3                 data[mask], \cf7 \strokec7 x\cf4 \strokec4 =\cf6 \strokec6 "Payload Mass (kg)"\cf4 \strokec4 , \cf7 \strokec7 y\cf4 \strokec4 =\cf6 \strokec6 "class"\cf4 \strokec4 , \cb1 \
\cb3                 \cf7 \strokec7 color\cf4 \strokec4 =\cf6 \strokec6 "Booster Version Category"\cf4 \strokec4 ,\cb1 \
\cb3                 \cf7 \strokec7 title\cf4 \strokec4 =\cf6 \strokec6 'Correlation between payload and sucess for site \cf8 \strokec8 \{\}\cf6 \strokec6 '\cf4 \strokec4 .format(entered_site))\cb1 \
\cb3                 \cf5 \strokec5 return\cf4 \strokec4  fig\cb1 \
\
\
\
\cf2 \cb3 \strokec2 # Run the app\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf7 \strokec7 __name__\cf4 \strokec4  == \cf6 \strokec6 '__main__'\cf4 \strokec4 :\cb1 \
\cb3     app.run_server()\cb1 \
\
\
}