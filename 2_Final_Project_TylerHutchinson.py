"""
Name: Tyler Hutchinson
CS230: Section 2
Data: Fast Food Data

Description: This is my Final Project for CS230. I worked with the Fast Food Restaurant data set. In this app I created
some maps and charts as way to better visualize and understand in the dataset. This project includes an icon map,
a density map, pie charts, and bar charts.
"""
import streamlit as st
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt

# Webpage Configuration
st.set_page_config(page_title="Fast Food Data",
                   page_icon=":bar_chart:")

# Input Data
ffd = pd.read_csv('Fast_Food_Data.csv')

# Dropping Unneeded Data
ffd = ffd.drop(['id', 'keys', 'sourceURLs', 'websites'], axis=1)

# Sidebar
st.sidebar.title("Fast Food Data App")
st.sidebar.markdown("Tyler Hutchinson")
st.sidebar.subheader("Navigation")
selected_page = st.sidebar.selectbox("Select a Page", ["Home", "Icon Map", "Density Map", "Pie Charts", "Bar Charts"])
st.sidebar.subheader("About")
st.sidebar.markdown("This is my Final Project for CS230. I worked with the Fast Food Restaurant data set. In this"
                    " app I created some maps and charts as way to better visualize and understand in the dataset.")


# Home Page
if selected_page == "Home":
    header = st.container()
    dataset = st.container()
    features = st.container()

    with header:
        st.title('Fast Food Restaurants App')
        st.markdown("""This app performs simple visualization of fast food restaurants across the US!""")
    with dataset:
        st.header("Dataset")
        ffd = pd.read_csv('Fast_Food_Data.csv')
        ffd = ffd.drop(['id','keys', 'sourceURLs', 'websites'], axis=1)
        st.write(ffd.head(5))
    with features:
        st.header("Features")
        st.markdown('* **Icon Map** | This is an icon map that is centered on the Boston Area, each point on the map '
                    'is represented by an icon that provides the Restaurant Name.')
        st.markdown('* **Density Map** | This is a density map that displays, the density of restaurants in each individual '
               'state. It answers the question, Whats the geospatial perspective of the restaurants in different'
               ' states? The color bar is used to depict different densities through varying shades of the color red.')
        st.markdown('* **Pie Charts** | The first pie chart uses the Pandas describe() function I found the mean, max, and min number of '
                'restaurants in each city. The mean number came out to about 3.55 restaurants per city. In this pie '
                'chart I depict how many cities have more than 4 restaurants and how many have less than 4 restaurants. '
                ' The second is an interactive pie chart in which you choose the state you would like to '
                'analyze. It shows the distribution of the top 10 restaurants within the selected state.')
        st.markdown('* **Bar Charts** | The first bar chart is an interactive bar chart that allows the user to adjust how many '
                'restaurants they would like to include. Once the user chooses a value it shows the top (user value) '
                'restaurants. The second bar chart is also an interactive bar chart that allows the user to adjust how many '
                'cities they would like to include. Once the user chooses a value it shows the top (user value) '
                'cities.')


# Icon Map
if selected_page == "Icon Map":
    st.title('Icon Map')
    st.markdown('**Description** | This is an icon map that is centered on the Boston Area, '
                'each point on the map is represented by an icon that provides the Restaurant Name.')
    ICON_URL = "https://upload.wikimedia.org/wikipedia/commons/b/b3/Icon_Information.svg"
    icon_data = {
        "url": ICON_URL,
        "width": 100,
        "height": 100,
        "anchorY": 100
        }
    ffd["icon_data"] = None
    for i in ffd.index:
        ffd["icon_data"][i] = icon_data
    icon_layer = pdk.Layer(type="IconLayer",
                           data = ffd,
                           get_icon="icon_data",
                           get_position='[longitude,latitude]',
                           get_size=4,
                           size_scale=10,
                           pickable=True)
    view_state = pdk.ViewState(
        longitude=-71.0589,
        latitude=42.3601,
        zoom=10,
        min_zoom=3,
        max_zoom=15,
        pitch=40,
        bearing=-20,
        )
    tool_tip = {"html": "Restaurant Name:<br/> <b>{name}</b>",
                "style": { "backgroundColor": "orange",
                            "color": "white"}
              }
    icon_map = pdk.Deck(
        map_style='mapbox://styles/mapbox/navigation-day-v1',
        layers=[icon_layer],
        initial_view_state= view_state,
        tooltip = tool_tip)
    st.pydeck_chart(icon_map)


# Density Map
if selected_page == "Density Map":
   st.title("Density Map")
   st.markdown('**Description** | This is a density map that displays, the density of restaurants in each individual '
               'state. It answers the question, Whats the geospatial perspective of the restaurants in different'
               ' states? The color bar is used to depict different densities through varying shades of the color red.')

   state_codes = ffd['province'].value_counts().index.tolist()
   value_counts_by_states = ffd['province'].value_counts()
   data= [dict(type='choropleth',
                locations = state_codes,
                z = value_counts_by_states,
                locationmode = 'USA-states',
                colorscale = 'Reds',
                marker_line_color = 'white',
                colorbar_title = "Number of Fast Fast Restaurants"
            )]
   layout = dict(title = 'Fast Food Restaurants by State',
                  geo = dict(scope='usa'))
   st.plotly_chart(data)


# Pie Chart 1
rest_count_by_city = ffd['city'].value_counts()
rest_count_by_city.describe()

if selected_page == "Pie Charts":
    st.subheader("How Many Cities are Above and Below the Mean?")
    st.markdown('**Description** | Using the Pandas describe() function I found the mean, max, and min number of '
                'restaurants in each city. The mean number came out to about 3.55 restaurants per city. In this pie '
                'chart I depict how many cities have more than 4 restaurants and how many have less than 4 restaurants.')
    rest_count_by_city = ffd['city'].value_counts()
    rest_count_by_city.describe()
    fig, ax = plt.subplots()
    total_cities_with_less_than_4_rests = len(rest_count_by_city[rest_count_by_city < 4])
    total_cities_with_greater_equal_4_rests = ffd['city'].nunique() - total_cities_with_less_than_4_rests
    values = [total_cities_with_less_than_4_rests, total_cities_with_greater_equal_4_rests]
    ax.pie(values,
           labels=["Cities With 1-3 Restaurants", "Cities With 4+ Restaurants"], autopct='%.1f%%', radius=1,
           explode = (0.1, 0))
    ax.set_aspect('equal')
    ax.set_title("US Cities' Fast Food Restaurants Number")
    st.pyplot(fig)

# Pie Chart 2
    st.subheader("Restaurant Distribution by State")
    st.markdown('**Description** | This is an interactive pie chart in which you choose the state you would like to '
                'analyze. It shows the distribution of the top 10 restaurants within the selected state.')
    province = st.selectbox('Select a State', ffd['province'])
    counts = ffd[ffd["province"]==province]["name"].value_counts()[:10].values
    labels = ffd[ffd["province"]==province]["name"].value_counts().index.tolist()[:10]
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels, autopct='%.1f%%', radius=1.1,
          explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    ax1.set_aspect('equal')
    ax1.set_title("Top 10 Restaurants in " + province)
    st.pyplot(fig1)


# Bar Charts
if selected_page == "Bar Charts":
    st.subheader('Top Restaurants')
    st.markdown("**Description** | This is an interactive bar chart that allows the user to adjust how many "
                "restaurants they would like to include. Once the user chooses a value it shows the top (user value) "
                "restaurants.")
    fig2, ax2 = plt.subplots()
    size = st.slider("Number of Restaurants:", 5, 20)
    ax2=ffd['name'].value_counts()[:size].plot.bar(title='Top Mentioned Restaurants')
    ax2.set_xlabel('Restaurant',size=10)
    ax2.set_ylabel('Number of Restaurants',size=10)
    st.pyplot(fig2)

# Bar Chart 2
    st.subheader('Top Cities')
    st.markdown("**Description** | This is an interactive bar chart that allows the user to adjust how many "
                "cities they would like to include. Once the user chooses a value it shows the top (user value) "
                "cities.")
    fig3, ax3 = plt.subplots()
    s = st.slider("Number of Cities:", 5, 20)
    ax3 = ffd['city'].value_counts()[:s].plot.bar(title='Top Mentioned Cities')
    ax3.set_xlabel('City',size=10)
    ax3.set_ylabel('Number of Restaurants',size=10)
    st.pyplot(fig3)
