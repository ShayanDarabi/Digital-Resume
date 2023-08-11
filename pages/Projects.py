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

# Display a centered title
st.title("My Projects")


# --- Projects & Accomplishments ---
google_or = 'https://developers.google.com/optimization'
folium = 'https://python-visualization.github.io/folium'
pm4py = "https://pm4py.fit.fraunhofer.de"
open_route_api = 'https://openrouteservice.org'
st.write('\n')
st.write(
    f"""
✔️ Solving a Capacitated Vehicle Routing Problem (CVRP):
- Navigating a complex challenge, I delved into the intricacies of the Capacitated Vehicle Routing Problem (CVRP). With 41 workers and a fleet of 17 vehicles at hand, I harnessed the power of [Google OR-Tools]({google_or}) to optimize routes while adhering to capacity constraints.

- Every distance and time matrix was meticulously calculated, forming a sturdy foundation for the optimization journey. Careful allocation of vehicles, considering capacities, ensured smooth operations.

- As the optimal solution emerged, I visualized each vehicle's route using [Folium]({folium}) and the [Open Route Source API]({open_route_api}). This tangible representation brought logistical efficiency to life on the map, translating intricate plans into actionable reality.

- In essence, my expertise fused mathematics, data analysis, and visualization to conquer the CVRP, exemplifying a dedication to practical solutions for complex real-world puzzles. 
"""
)

st.write("This is the project code:")
custom_css = """
<style>
    /* Target the code block by its class */
    .streamlit-code-block {
        background-color: white;
        color: black;
        border: 1px solid gray;
    }
</style>
"""

# Display the custom CSS using markdown
st.markdown(custom_css, unsafe_allow_html=True)

st.code(
    """
import time
import requests
import pandas as pd
import folium
from folium.features import CustomIcon
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Load data from Excel
data = pd.read_excel('Routing problem - Raw Data - V2 .xlsx', index_col='Code', sheet_name='distance')
distance_matrix = [data.iloc[i].values.tolist() for i in range(45)]

# Define API URL for OpenRouteService
api_url = "https://api.openrouteservice.org/v2/directions/driving-car"

def create_data_model():
    #Stores the data for the problem.
    data = {}
    data['distance_matrix'] = distance_matrix
    data['demands'] = [0, 1, 1, 0] + [1] * 41
    data['vehicle_capacities'] = [5, 5] + [4] * 15
    data['num_vehicles'] = 17
    data['starts'] = [1, 2] + [3] * 15
    data['ends'] = [0] * 17
    return data

def distance_callback(from_index, to_index):
    #Returns the distance between the two nodes.
    return data['distance_matrix'][from_index][to_index]

def demand_callback(from_index):
    #Returns the demand of the node.
    return data['demands'][from_index]

def print_solution(data, manager, routing, solution):
    #Prints solution on console.
    print(f'Objective: {solution.ObjectiveValue()}')
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            route_distance += routing.GetArcCostForVehicle(index, solution.Value(routing.NextVar(index)), vehicle_id)
            index = solution.Value(routing.NextVar(index))
        total_distance += route_distance
        total_load += route_load
    print(f'Total distance of all routes: {total_distance} km')
    print(f'Total load of all routes: {total_load}')
    print('-' * 20)

def main():
    #Solve the CVRP problem.
    data_model = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data_model['distance_matrix']), data_model['num_vehicles'], data_model['starts'], data_model['ends'])
    routing = pywrapcp.RoutingModel(manager)

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(demand_callback_index, 0, data_model['vehicle_capacities'], True, 'Capacity')

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    search_parameters.time_limit.FromSeconds(1)
    
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data_model, manager, routing, solution)

if __name__ == '__main__':
    main()

cordinations_list = [[1, 12, 10, 35, 9, 0],
                    [2, 4, 7, 14, 8, 0],
                    [3, 26, 38, 15, 33, 0],
                    [3, 27, 32, 11, 6, 0],
                    [3, 16, 5, 40, 31, 0],
                    [3, 22, 13, 19, 17, 0],
                    [3, 37, 24, 30, 25, 0],
                    [3, 36, 41, 34, 39, 0],
                    [3, 18, 28, 21, 42, 0],
                    [3, 23, 29, 20, 0]]

cordinations = [dataframe[['Latitude', 'Longitude']].iloc[[1, 12, 10, 35, 9, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[2, 4, 7, 14, 8, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 26, 38, 15, 33, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 27, 32, 11, 6, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 16, 5, 40, 31, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 22, 13, 19, 17, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 37, 24, 30, 25, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 36, 41, 34, 39, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 18, 28, 21, 42, 0]].values.tolist(),
               dataframe[['Latitude', 'Longitude']].iloc[[3, 23, 29, 20, 0]].values.tolist(),]


for index, points in enumerate(cordinations):
    
    dataframe = {'Latitude':df['Latitude'].iloc[cordinations_list[index]].tolist(),
            'Longitude':df['Longitude'].iloc[cordinations_list[index]].tolist(),
            'Gender':df['Gender'].iloc[cordinations_list[index]].tolist(),
            'Name':df['Family'].iloc[cordinations_list[index]].tolist()}
    dataframe = pd.DataFrame(dataframe)
    
    m = folium.Map(location=[Lat, Long], zoom_start=15)

    # Add markers for each location with custom icons
    for index_dataframe, row in dataframe.iterrows():
        if index_dataframe == (dataframe.shape[0] - 1):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Name'],
                icon=folium.Icon(color="green", icon='home', prefix='fa')
        ).add_to(m)

        elif index_dataframe == 0:
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Name'],
                icon=folium.Icon(color="red", icon='car', prefix='fa')
        ).add_to(m)
            
        elif row['Gender'] == 'M':
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Name'],
                icon=folium.Icon(color="blue", icon='person', prefix='fa', iconColor='black'),   
            ).add_to(m)
            
        else:
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Name'],
                icon=folium.Icon(color="pink", icon='person-dress', prefix='fa'),  
            ).add_to(m)
    
   # Calculate routes between points using OpenRouteService API
    for i in range(len(points) - 1):
        start_point = points[i]
        end_point = points[i+1]
        
        # Request route data from OpenRouteService
        params = {
            "api_key": "YOUR_OPENROUTESERVICE_API_KEY"",
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
        folium.PolyLine(locations=route_coordinates, color='blue', weight=3).add_to(m)
        time.sleep(2)
        m.save(f'./time/map{index}.html'
    """
, language = 'python')

st.write('\n')
st.write(
    f"""
✔️ Several Projects About Data Aggregation, Cleaning, and Visualization
- I excel at refining and combining intricate datasets using Pandas and Numpy, ensuring data integrity. Leveraging Matplotlib and Seaborn, I craft enlightening visuals, including P control charts. I create informative dashboards, and with Pandas Profiling, I extract actionable insights from exploratory data analysis. My focus is on turning complexity into clarity. 
"""
)

st.write('\n')
st.write(f"""
✔️ Process Mining:
- Using the dataset at my disposal, I took a close look at a company's operations using a helpful tool called [pm4py]({pm4py}), a popular library in Python for process mining. After getting the data in shape, I let pm4py work its magic. It revealed how things flowed, pinpointed bottlenecks, and made sure the actual processes matched the plan.  
"""
)
st.write('\n')
streamlit = 'https://streamlit.io/'
st.write(f"""
✔️ Digital Résumé:
- I've crafted this digital résumé with the help of the [Streamlit]({streamlit}) package that helps you build a web app in the simplest possible way. It lets you deploy and share your app on its community cloud for free. Isn't it amazing? 
- One of the traits that I like the most in myself is that I love learning and building new stuff and as a data scientist I have a plan to make the most of this incredible platform to build many data apps that can deliver insightful information to team members and stakeholders and are easy to work and play with.
"""
)
st.write('\n')
repo = 'https://github.com/ShayanDarabi/File-Handling'
st.write(
    f"""
✔️ [File Organizer: Simplifying Your Directory Chaos]({repo})
- I embarked on a quest to declutter my files, and the result is my own Python tool. This nifty script swiftly organizes my images, documents, videos, and music, turning chaos into harmony. No more scavenger hunts for files – I just let it work its magic. It's simplicity at its best, keeping my digital world neat and tidy.
    """
)