import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Projects",
    page_icon="👨‍💻",
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# --- Projects & Accomplishments ---
google_or = 'https://developers.google.com/optimization'
folium = 'https://python-visualization.github.io/folium'
open_route_api = 'https://openrouteservice.org'
st.write(
    f"""
✔️ Solving a Capacitated Vehicle Routing Problem (CVRP):
- Navigating a complex challenge, I delved into the intricacies of the Capacitated Vehicle Routing Problem (CVRP). With 41 workers and a fleet of 17 vehicles at hand, I harnessed the power of Google OR-Tools to optimize routes while adhering to capacity constraints.

- Every distance and time matrix was meticulously calculated, forming a sturdy foundation for the optimization journey. Careful allocation of vehicles, considering capacities, ensured smooth operations.

- As the optimal solution emerged, I visualized each vehicle's route using Folium and the Open Route Source API. This tangible representation brought logistical efficiency to life on the map, translating intricate plans into actionable reality.

- In essence, my expertise fused mathematics, data analysis, and visualization to conquer the CVRP, exemplifying a dedication to practical solutions for complex real-world puzzles. This is the project code:
"""
)

code_snippet = """
import pandas as pd
import requests
import time
import folium
from folium.features import CustomIcon
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

data = pd.read_excel('Routing problem - Raw Data - V2 .xlsx', index_col='Code',sheet_name='distance')
distance_matrix = [data.iloc[i].values.tolist() for i in range(45)]

def create_data_model():
    #Stores the data for the problem.
    data = {}
    data['distance_matrix'] = distance_matrix
    data['demands'] = [0, 1, 1 ,0] + [1] * 41
    data['vehicle_capacities'] = [5, 5] + [4] * 15
    data['num_vehicles'] = 17
    data['starts'] =[1, 2] + [3] * 15
    data['ends'] = [0 for _ in range(17)]
    return data

def print_solution(data, manager, routing, solution):
     #Prints solution on console.
     print(f'Objective: {solution.ObjectiveValue()}')
     total_distance = 0
     total_load = 0
     for vehicle_id in range(data['num_vehicles']):
         index = routing.Start(vehicle_id)
         plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
         route_distance = 0
         route_load = 0
         while not routing.IsEnd(index):
             node_index = manager.IndexToNode(index)
             route_load += data['demands'][node_index]
             plan_output += '{0} Load({1}) -> '.format(node_index, route_load)
             previous_index = index
             index = solution.Value(routing.NextVar(index))
             route_distance += routing.GetArcCostForVehicle(
                 previous_index, index, vehicle_id)
         plan_output += '{0} Load({1})\n'.format(manager.IndexToNode(index),
         route_load)
         plan_output += 'Distance of the route: {}km\n'.format(route_distance)
         plan_output += 'Load of the route: {}\n'.format(route_load)
         print(plan_output)
         total_distance += route_distance
         total_load += route_load
     print('Total distance of all routes: {}km'.format(total_distance))
     print('Total load of all routes: {}'.format(total_load))
     print('-'* 20)


def main():
     #Solve the CVRP problem.
     # Instantiate the data problem.
     data = create_data_model()
     # Create the routing index manager.
     manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                             data['num_vehicles'], data['starts'],
                                             data['ends'])
                                             # Create Routing Model.
     routing = pywrapcp.RoutingModel(manager)
     # Create and register a transit callback.
     def distance_callback(from_index, to_index):
        #Returns the distance between the two nodes.
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

     transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
     routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


     # Add Capacity constraint.
     def demand_callback(from_index):
         #Returns the demand of the node.
         # Convert from routing variable Index to demands NodeIndex.
         from_node = manager.IndexToNode(from_index)
         return data['demands'][from_node]
         
     demand_callback_index = routing.RegisterUnaryTransitCallback(
     demand_callback)
     routing.AddDimensionWithVehicleCapacity(
         demand_callback_index,
         0, # null capacity slack
         data['vehicle_capacities'], # vehicle maximum capacities
         True, # start cumul to zero
         'Capacity')

     # Setting first solution heuristic.
     search_parameters = pywrapcp.DefaultRoutingSearchParameters()
     search_parameters.first_solution_strategy = (
     routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
     search_parameters.local_search_metaheuristic = (
     routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
     search_parameters.time_limit.FromSeconds(1)
     # Solve the problem.
     solution = routing.SolveWithParameters(search_parameters)
     # Print solution on console.
     if solution:
         print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()

# Create a map centered at a specific location
df = pd.read_excel('Routing problem - Raw Data - V2 .xlsx')
dataframe = {'Latitude':df['Latitude'].tolist(),
            'Longitude':df['Longitude'].tolist(),
            'Gender':df['Gender'].tolist(),
            'Name':df['Family'].tolist()}

dataframe = pd.DataFrame(dataframe)
m = folium.Map(location=[Lat, Long], zoom_start=15)

# Add markers for each location with custom icons
for index, row in dataframe.iterrows():
    if index == 0:
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color="red", icon='home')
    ).add_to(m)
        
    if index == 1:
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color="green", icon='car'),  
        ).add_to(m)
        
    if row['Gender'] == 'M':
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color="blue"), 
        ).add_to(m)
    else:
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color="pink"),   
        ).add_to(m)

cordinations = [dataframe[['Latitude', 'Longitude']].iloc[[1, 12, 10, 18, 36, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[2, 17, 28, 33, 41, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 39, 34, 15, 27, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 20, 9, 14, 8, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 4, 7, 5, 16, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 44, 25, 31, 26, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 33, 13, 35, 40, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 43, 24, 19, 30, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 37, 38, 22, 0]].values.tolist()]

color_dict = {0:'blue',
        1:'red',
        2:'gray',
        3:'black',
        4:'yellow',
        5:'green',
        6:'white',
        7:'purple',
        8:'brown'}

for color_index, points in enumerate(cordinations):
   # Calculate routes between points using OpenRouteService API
    for i in range(len(points) - 1):
        start_point = points[i]
        end_point = points[i+1]
        
        # Request route data from OpenRouteService
        params = {
            "api_key": "5b3ce3597851110001cf6248f668245b4f504409a13a50f75764fa80",
            "start": f"{start_point[1]},{start_point[0]}",
            "end": f"{end_point[1]},{end_point[0]}"
        }
        response = requests.get(api_url, params=params)
        route_data = response.json()
        
        # Extract coordinates along the route
        route_coordinates = [
            (coord[1], coord[0]) for coord in route_data["features"][0]["geometry"]["coordinates"]
        ]
        
        # Add polyline for the route
        folium.PolyLine(locations=route_coordinates, color=color_dict[color_index], weight=6).add_to(m)
        time.sleep(2)
        m.save(f'./map{index}.html')
"""
st.code(code_snippet, language='python')

st.write(
    f"""
✔️ Several Projects About Data Aggregation, Cleaning and Visualization
- I excel at refining and combining intricate datasets using Pandas and Numpy, ensuring data integrity. Leveraging Matplotlib and Seaborn, I craft enlightening visuals, including P control charts. I create informative dashboards, and with Pandas Profiling, I extract actionable insights from exploratory data analysis. My focus is on turning complexity into clarity. 
"""
)


st.write(
    """
✔️ [File Organizer: Simplifying Your Directory Chaos]({https://github.com/ShayanDarabi/File-Handling)
- I embarked on a quest to declutter my files, and the result is my own Python tool. This nifty script swiftly organizes my images, documents, videos, and music, turning chaos into harmony. No more scavenger hunts for files – I just let it work its magic. It's simplicity at its best, keeping my digital world neat and tidy.
    """
)