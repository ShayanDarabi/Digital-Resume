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
pm4py = "https://pm4py.fit.fraunhofer.de"
open_route_api = 'https://openrouteservice.org'
st.write(
    f"""
✔️ Solving a Capacitated Vehicle Routing Problem (CVRP):
- Navigating a complex challenge, I delved into the intricacies of the Capacitated Vehicle Routing Problem (CVRP). With 41 workers and a fleet of 17 vehicles at hand, I harnessed the power of [Google OR-Tools]({google_or}) to optimize routes while adhering to capacity constraints.

- Every distance and time matrix was meticulously calculated, forming a sturdy foundation for the optimization journey. Careful allocation of vehicles, considering capacities, ensured smooth operations.

- As the optimal solution emerged, I visualized each vehicle's route using [Folium]({folium}) and the [Open Route Source API]({open_route_api}). This tangible representation brought logistical efficiency to life on the map, translating intricate plans into actionable reality.

- In essence, my expertise fused mathematics, data analysis, and visualization to conquer the CVRP, exemplifying a dedication to practical solutions for complex real-world puzzles.
"""
)

st.write(
    f"""
✔️ Several Projects About Data Aggregation, Cleaning, and Visualization
- I excel at refining and combining intricate datasets using Pandas and Numpy, ensuring data integrity. Leveraging Matplotlib and Seaborn, I craft enlightening visuals, including P control charts. I create informative dashboards, and with Pandas Profiling, I extract actionable insights from exploratory data analysis. My focus is on turning complexity into clarity. 
"""
)


st.write(f"""
✔️ Process Mining:
- Using the dataset at my disposal, I took a close look at a company's operations using a helpful tool called [pm4py]({pm4py}), a popular library in Python for process mining. After getting the data in shape, I let pm4py work its magic. It revealed how things flowed, pinpointed bottlenecks, and made sure the actual processes matched the plan.  
"""
)

repo = 'https://github.com/ShayanDarabi/File-Handling'
st.write(
    f"""
✔️ [File Organizer: Simplifying Your Directory Chaos]({repo})
- I embarked on a quest to declutter my files, and the result is my own Python tool. This nifty script swiftly organizes my images, documents, videos, and music, turning chaos into harmony. No more scavenger hunts for files – I just let it work its magic. It's simplicity at its best, keeping my digital world neat and tidy.
    """
)