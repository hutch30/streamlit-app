"""
Name: Tyler Hutchinson
CS230: Section 2
Data: Fast Food Data

Description: This is my Final Project for CS230. I worked with the Fast Food Restaurant data set. In this app I created
some maps and charts as way to better visualize and understand in the dataset. This project includes an icon map,
a density map, pie charts, and bar charts.

***Disclosure*** I have two versions of the code, this one includes a lot of data cleaning. In the dataset, there were
different name variations of the same restaurant. I cleaned the data so that the variations now equal one,
consistent value. As a result, the data visualizations are more accurate, the issue being the website runs
incredibly slow. That said both work, but this one includes data cleaning that really slows down the app functions.
"""

import streamlit as st
import pandas as pd
import pydeck as pdk
# I used the nltk python function to clean my data
import nltk
import matplotlib.pyplot as plt

# Webpage Configuration
st.set_page_config(page_title="Fast Food Data",
                   page_icon=":bar_chart:")

# Input Data
ffd = pd.read_csv('Fast_Food_Data.csv')

# Condensing the dataset
ffd = ffd.drop(['id', 'keys', 'sourceURLs', 'websites'], axis=1)

# Check for Missing Values
def missing_value_describe(data):
    missing_value_stats = (data.isnull().sum() / len(data)*100)
    missing_value_col_count = sum(missing_value_stats > 0)
    missing_value_stats = missing_value_stats.sort_values(ascending=False)[:missing_value_col_count]
    print("Number of columns with missing values:", missing_value_col_count)
    if missing_value_col_count != 0:
        # print out column names with missing value percentage
        print("\nMissing percentage (desceding):")
        print(missing_value_stats)
    else:
        print("No misisng data!!!")
missing_value_describe(ffd)

# Sidebar
st.sidebar.title("Fast Food Data App")
st.sidebar.markdown("Tyler Hutchinson")
st.sidebar.subheader("Navigation")
selected_page = st.sidebar.selectbox("Select a Page", ["Dictionary", "Home", "Icon Map", "Density Map", "Pie Charts", "Bar Charts"])
st.sidebar.subheader("About")
st.sidebar.markdown("This is my Final Project for CS230. I worked with the Fast Food Restaurant data set. In this"
                    " app I created some maps and charts as way to better visualize and understand in the dataset.")

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

if selected_page == "Dictionary":
 restaurant_names = ffd['name'].unique()

 # calculate similarity and record most-similar names together
 most_similar = []
 for i in range(len(restaurant_names)):
     temp_similar = [restaurant_names[i]]

 # compare and save similar words
     for j in range(len(restaurant_names)):
         if restaurant_names[i] == restaurant_names[j]:
             continue
         if nltk.edit_distance(restaurant_names[i].lower(), restaurant_names[j].lower()) < 3:
             temp_similar.append(restaurant_names[j])

 # similar word(s) found
     if len(temp_similar) > 1:
         most_similar.append(temp_similar)
     if i > 0 and i % 10 == 0:
         print("index", i-10, "-", i, "checking finished| most similar size:", len(most_similar))
 print("similarity checking finished")

 # count number of similar words
 most_similar_word_count = 0
 for i in most_similar:
     most_similar_word_count += len(i)
 print("size of the most similar list:", most_similar_word_count)
 most_similar

 most_similar_edited = [["Carl's Jr.", "Carl's Jr", 'Carls Jr'],
  ["McDonald's", "Mc Donald's", 'Mcdonalds', 'McDonalds'],
  ['Cook-Out', 'Cook Out', 'CookOut'],
  ["Steak 'n Shake",
   "STEAK 'N SHAKE",
   'Steak N Shake',
   'Steak n Shake',
   "Steak 'N Shake"],
  ['QDOBA Mexican Eats', 'Qdoba Mexican Eats'],
  ['Burger King', 'Burger King®'],
  ["Hardee's", 'Hardees'],
  ['Taco Time', 'TacoTime'],
  ["Arby's", 'Arbys'],
  ['Chick-fil-A', 'Chick-Fil-A', 'ChickfilA'],
  ['Subway', 'SUBWAY'],
  ['Kfc', 'KFC'],
  ["Jack's", 'Jacks'],
  ['Sonic Drive-In',
   'SONIC Drive-In',
   'SONIC Drive In',
   'Sonic DriveIn',
   'Sonic Drive-in'],
  ["Church's Chicken", 'Churchs Chicken'],
  ['Big Boys', 'Big Boy'],
  ['Dairy Queen', 'Dairy queen'],
  ['Guthries', "Guthrie's"],
  ['Chick-Fil-A', 'Chick-fil-A', 'ChickfilA'],
  ["Wendy's", 'Wendys'],
  ["Jimmy John's", 'Jimmy Johns'],
  ['Dairy Queen Grill Chill', 'Dairy Queen Grill & Chill'],
  ["Moe's Southwest Grill", 'Moes Southwest Grill'],
  ["Domino's Pizza", 'Dominos Pizza'],
  ["Rally's", 'Rallys'],
  ['Full Moon Bar-B-Que', 'Full Moon Bar B Que'],
  ["Guthrie's", 'Guthries'],
  ["McAlister's Deli", "Mcalister's Deli", 'McAlisters Deli'],
  ["Jason's Deli", 'Jasons Deli'],
  ['KFC', 'Kfc', 'KFC Kentucky Fried Chicken', 'KFC - Kentucky Fried Chicken'],
  ['Popeyes Louisiana Kitchen', "Popeye's Louisiana Kitchen"],
  ["Long John Silver's", 'Long John Silvers'],
  ['BLIMPIE', 'Blimpie'],
  ['Five Guys Burgers Fries', 'Five Guys Burgers & Fries'],
  ['SUBWAY', 'Subway'],
  ['Dairy Queen Grill & Chill', 'Dairy Queen Grill Chill'],
  ['Potbelly Sandwich Works', 'Pot Belly Sandwich Works'],
  ["Charley's Grilled Subs", 'Charleys Grilled Subs'],
  ["Jersey Mike's Subs", 'Jersey Mikes Subs'],
  ['In-N-Out Burger', 'InNOut Burger'],
  ["Culver's", "CULVER'S", 'Culvers'],
  ["Famous Dave's", 'Famous Daves'],
  ["Freddy's Frozen Custard Steakburgers",
   'Freddys Frozen Custard Steakburgers',
   "Freddy's Frozen Custard & Steakburgers"],
  ['Cook Out', 'Cook-Out', 'CookOut'],
  ['TacoTime', 'Taco Time'],
  ['Hooters', 'Roosters'],
  ['BurgerFi', 'Burgerfi'],
  ["Chen's Restaurant", "Chan's Restaurant"],
  ['Taco Del Mar', 'Taco del Mar'],
  ['SONIC Drive-In',
   'Sonic Drive-In',
   'SONIC Drive In',
   'Sonic DriveIn',
   'Sonic Drive-in'],
  ['Ciscos Taqueria', "Cisco's Taqueria"],
  ['China King', 'China Lin'],
  ["Bojangles' Famous Chicken 'n Biscuits",
   'Bojangles Famous Chicken n Biscuits'],
  ["Dominic's of New York", 'Dominics of New York'],
  ["Papa John's Pizza", 'Papa Johns Pizza'],
  ['Chanellos Pizza', 'Chanello’s Pizza'],
  ["Fazoli's", 'Fazolis'],
  ['Wing Street', 'Wingstreet'],
  ["George's Gyros Spot", "George's Gyros Spot 2"],
  ['Taco Johns', "Taco John's"],
  ['RUNZA', 'Runza'],
  ['Bru Burger Bar', 'Grub Burger Bar'],
  ["Taco John's", 'Taco Johns'],
  ["Bob's Burger Brew", "Bob's Burgers Brew", "Bob's Burgers Brew", "Bob's Burger Brew"],
  ['Best Burgers', 'Best Burger'],
  ['Burgermaster', 'Burger Master'],
  ["Dick's Drive-In", "DK's Drive-In"],
  ["Charley's Grill Spirits", "Charley's Grill & Spirits"],
  ['Tom Drive-in', "Tom's Drive-In"],
  ["Fox's Pizza Den", 'Foxs Pizza Den'],
  ["Mc Donald's", "McDonald's", 'Mcdonalds', 'McDonalds'],
  ['Taco CASA', 'Taco Casa'],
  ["Mcalister's Deli", "McAlister's Deli", 'McAlisters Deli'],
  ['Saras Too', "Sara's Too"],
  ['Backyard Burgers', 'Back Yard Burgers'],
  ["CULVER'S", "Culver's", 'Culvers'],
  ["Simple Simon's Pizza", 'Simple Simons Pizza'],
  ['China Sea', 'China Star', 'China Bear'],
  ["Dino's Drive In", "Dan's Drive In"],
  ["STEAK 'N SHAKE",
   "Steak 'n Shake",
   'Steak N Shake',
   'Steak n Shake',
   "Steak 'N Shake"],
  ['Stanfields Steak House', "Stanfield's Steakhouse"],
  ['Wingstreet', 'Wing Street'],
  ["Big Billy's Burger Joint", 'Big Billys Burger Joint'],
  ['Big Boy', 'Big Boys'],
  ["Frisch's Big Boy Restaurant", "1 Frisch's Big Boy Restaurant",
   "40 Frisch's Big Boy Restaurant", "1 Frisch's Big Boy Restaurant",
   "90 Frisch's Big Boy Restaurant"],
  ['Fireplace Restaurant Lounge', 'Fireplace Restaurant & Lounge'],
  ["Carl's Jr", "Carl's Jr.", 'Carls Jr'],
  ["Rick's on the River", 'Ricks on the River'],
  ['Grub Burger Bar', 'Bru Burger Bar'],
  ["Franky's", "Grandy's"],
  ['Gyro X-Press', 'Gyro Express'],
  ['Dominos Pizza', "Domino's Pizza"],
  ["Pietro's Pizza Gallery of Games", "Pietro's Pizza & Gallery of Games"],
  ['Burrtio Amigos', 'Burrito Amigos'],
  ["Albee's Ny Gyros", "Albee's NY Gyros"],
  ['Gyro Stop', 'Gyro Spot'],
  ['Nicholas Restaurant', "Nicholas' Restaurant"],
  ['Mcdonalds', "McDonald's", "Mc Donald's", 'McDonalds'],
  ['Burgerfi', 'BurgerFi'],
  ["Ryan's", 'Ryans'],
  ['Taste of Buffalo Pizzeria', 'Taste Of Buffalo Pizzeria'],
  ['Bad Daddys Burger Bar', "Bad Daddy's Burger Bar"],
  ["Zaxby's", "Arby's"],
  ["Topper's Pizza", 'Toppers Pizza'],
  ['C J Drive In', 'C & J Drive In'],
  ['Full Moon Bar B Que', 'Full Moon Bar-B-Que'],
  ['China Lin', 'China King'],
  ["Raising Cane's Chicken Fingers", 'Raising Canes Chicken Fingers'],
  ["Mary's Pizza Shack", 'Marys Pizza Shack'],
  ['Peking Chinese Restaurants', 'Peking Chinese Restaurant'],
  ['Arbys', "Arby's"],
  ['SONIC Drive In',
   'Sonic Drive-In',
   'SONIC Drive-In',
   'Sonic DriveIn',
   'Sonic Drive-in'],
  ['Hardees', "Hardee's"],
  ['McDonalds', "McDonald's", "Mc Donald's", 'Mcdonalds'],
  ['Wendys', "Wendy's"],
  ['Papa Johns Pizza', "Papa John's Pizza"],
  ["George's Gyros Spot 2", "George's Gyros Spot"],
  ['ChickfilA', 'Chick-fil-A', 'Chick-Fil-A'],
  ['Rallys', "Rally's"],
  ['C & J Drive In', 'C J Drive In'],
  ['Steak N Shake',
   "Steak 'n Shake",
   "STEAK 'N SHAKE",
   'Steak n Shake',
   "Steak 'N Shake"],
  ["Popeye's Louisiana Kitchen", 'Popeyes Louisiana Kitchen'],
  ["DJ's Drive-In", "DK's Drive-In"],
  ["Dan's Drive In", "Dino's Drive In"],
  ['Best Burger', 'Best Burgers', 'Beef Burger'],
  ['Jimmy Johns', "Jimmy John's"],
  ['BaskinRobbins', 'Baskin-Robbins', 'Baskin Robbins'],
  ['Carls Jr', "Carl's Jr.", "Carl's Jr"],
  ['WG Grinders', 'Wg Grinders'],
  ['McAlisters Deli', "McAlister's Deli", "Mcalister's Deli"],
  ['Fazolis', "Fazoli's"],
  ['Marys Pizza Shack', "Mary's Pizza Shack"],
  ['Bojangles Famous Chicken n Biscuits',
   "Bojangles' Famous Chicken 'n Biscuits"],
  ['Jacks', "Jack's"],
  ["Hardee's/red Burrito", 'Hardees Red Burrito', "Hardee's/Red Burrito"],
  ['Captain Ds', "Captain D'S"],
  ['Mr Hero', 'Mr. Hero'],
  ["Chan's Restaurant", "Chen's Restaurant"],
  ['Ritters Frozen Custard', "Ritter's Frozen Custard"],
  ['Hot Dog on a Stick', 'Hot Dog On A Stick'],
  ['Jersey Mikes Subs', "Jersey Mike's Subs"],
  ['AW Restaurants',
   'Aw Restaurants',
   'AWRestaurants',
   'A W Restaurant',
   'AW Restaurant',
   'Jam Restaurants'],
  ['Long John Silvers', "Long John Silver's"],
  ["Rally's Hamburgers", 'Rallys Hamburgers'],
  ['HomeTown Buffet', 'Hometown Buffet'],
  ['Back Yard Burgers', 'Backyard Burgers'],
  ['Hardees Red Burrito', "Hardee's/red Burrito", "Hardee's/Red Burrito"],
  ["DK's Drive-In", "Dick's Drive-In", "DJ's Drive-In", "K's Drive In"],
  ['Baskin-Robbins', 'BaskinRobbins', 'Baskin Robbins'],
  ['Churchs Chicken', "Church's Chicken"],
  ['Blimpie', 'BLIMPIE'],
  ['Foxs Pizza Den', "Fox's Pizza Den"],
  ['Steak n Shake',
   "Steak 'n Shake",
   "STEAK 'N SHAKE",
   'Steak N Shake',
   "Steak 'N Shake"],
  ['Rallys Hamburgers', "Rally's Hamburgers"],
  ['Sonic DriveIn',
   'Sonic Drive-In',
   'SONIC Drive-In',
   'SONIC Drive In',
   'Sonic Drive-in'],
  ['Famous Daves', "Famous Dave's"],
  ['Beef Burger', 'Best Burger'],
  ['Dominics of New York', "Dominic's of New York"],
  ['Z-Pizza', 'zpizza'],
  ['KFC - Kentucky Fried Chicken', 'KFC Kentucky Fried Chicken'],
  ["Rockne's", 'Rocknes'],
  ["Hardee's/Red Burrito", "Hardee's/red Burrito", 'Hardees Red Burrito'],
  ['Aw Restaurants',
   'AW Restaurants',
   'AWRestaurants',
   'A W Restaurant',
   'AW Restaurant',
   'Jam Restaurants'],
  ['AWRestaurants', 'AW Restaurants', 'Aw Restaurants', 'AW Restaurant'],
  ["Hardee's Restaurant", "Hardee's Restaurants"],
  ["Hardee's Restaurants", "Hardee's Restaurant"],
  ["Stanfield's Steakhouse", 'Stanfields Steak House'],
  ['Dunkin Donuts', "Dunkin' Donuts"],
  ['Einstein Bros. Bagels', 'Einstein Bros Bagels'],
  ['Simple Simons Pizza', "Simple Simon's Pizza"],
  ['A W Restaurant', 'AW Restaurants', 'Aw Restaurants', 'AW Restaurant'],
  ['Einstein Bros Bagels', 'Einstein Bros. Bagels'],
  ['Roosters', 'Hooters'],
  ['Culvers', "Culver's", "CULVER'S"],
  ['Slice of Life', 'Slice Of Life'],
  ['Jasons Deli', "Jason's Deli"],
  ['Wg Grinders', 'WG Grinders'],
  ['Charleys Grilled Subs', "Charley's Grilled Subs"],
  ['Freddys Frozen Custard Steakburgers',
   "Freddy's Frozen Custard Steakburgers"],
  ['Moes Southwest Grill', "Moe's Southwest Grill"],
  ['CookOut', 'Cook-Out', 'Cook Out'],
  ['Peking Chinese Restaurant', 'Peking Chinese Restaurants'],
  ['InNOut Burger', 'In-N-Out Burger'],
  ["Nicholas' Restaurant", 'Nicholas Restaurant'],
  ['Chanello’s Pizza', 'Chanellos Pizza'],
  ['Ryans', "Ryan's"],
  ['Burger King®', 'Burger King'],
  ['Toppers Pizza', "Topper's Pizza"],
  ["Albee's NY Gyros", "Albee's Ny Gyros"],
  ['Qdoba Mexican Eats', 'QDOBA Mexican Eats'],
  ['Runza', 'RUNZA'],
  ['Slice Of Life', 'Slice of Life'],
  ['Mai-Tai Restaurant', 'Mai Tai Restaurant'],
  ['Gyro Express', 'Gyro X-Press'],
  ['zpizza', 'Z-Pizza'],
  ['Raising Canes Chicken Fingers', "Raising Cane's Chicken Fingers"],
  ['Rocknes', "Rockne's"],
  ['LL Hawaiian Barbecue', 'L L Hawaiian Barbecue', 'L L Hawaiian Barbeque'],
  ['Dairy queen', 'Dairy Queen'],
  ['Blakes Lotaburger', "Blake's Lotaburger"],
  ['Emidio & Sons Italian Restaurant', 'Emidio Sons Italian Restaurant'],
  ['Taste Of Buffalo Pizzeria', 'Taste of Buffalo Pizzeria'],
  ['L L Hawaiian Barbecue',
   'LL Hawaiian Barbecue',
   'L L Hawaiian Barbeque',
   'L & L Hawaiian Barbecue'],
  ['Killer Burgers', 'Killer Burger'],
  ["Steak 'N Shake",
   "Steak 'n Shake",
   "STEAK 'N SHAKE",
   'Steak N Shake',
   'Steak n Shake'],
  ['Burrito Amigos', 'Burrtio Amigos'],
  ["Zack's Hamburgers", "Jack's Hamburgers"],
  ['AW Restaurant',
   'AW Restaurants',
   'Aw Restaurants',
   'AWRestaurants',
  'A W Restaurant'],
  ['Jam Restaurants', 'AW Restaurants', 'Aw Restaurants'],
  ['Big Billys Burger Joint', "Big Billy's Burger Joint"],
  ['L L Hawaiian Barbeque', 'LL Hawaiian Barbecue', 'L L Hawaiian Barbecue'],
  ["Ritter's Frozen Custard", 'Ritters Frozen Custard'],
  ["Pietro's Pizza & Gallery of Games", "Pietro's Pizza Gallery of Games"],
  ["K's Drive In", "DK's Drive-In"],
  ['Killer Burger', 'Killer Burgers'],
  ["Dunkin' Donuts", 'Dunkin Donuts'],
  ['Farlows on the Water', "Farlow's On The Water"],
  ['Hometown Buffet', 'HomeTown Buffet'],
  ["Blake's Lotaburger", 'Blakes Lotaburger'],
  ["Jack's Hamburgers", "Zack's Hamburgers"],
  ["Cisco's Taqueria", 'Ciscos Taqueria'],
  ["Grandy's", "Franky's"],
  ["Farlow's On The Water", 'Farlows on the Water'],
  ["Bad Daddy's Burger Bar", 'Bad Daddys Burger Bar'],
  ['Baskin Robbins', 'BaskinRobbins', 'Baskin-Robbins'],
  ["Sara's Too", 'Saras Too'],
  ['T & L Hotdogs', 'T & L Hot Dogs'],
  ["Tom's Drive-In", 'Tom Drive-in'],
  ['Sonic Drive-in',
   'Sonic Drive-In',
   'SONIC Drive-In',
   'SONIC Drive In',
   'Sonic DriveIn'],
  ['Taco Casa', 'Taco CASA'],
  ['Emidio Sons Italian Restaurant', 'Emidio & Sons Italian Restaurant'],
  ['Fireplace Restaurant & Lounge', 'Fireplace Restaurant Lounge'],
  ['Mai Tai Restaurant', 'Mai-Tai Restaurant'],
  ['Ricks on the River', "Rick's on the River"],
  ['Taco del Mar', 'Taco Del Mar'],
  ['Five Guys Burgers & Fries', 'Five Guys Burgers Fries'],
  ['Mr. Hero', 'Mr Hero'],
  ["Captain D'S", 'Captain Ds'],
  ['Gyro Spot', 'Gyro Stop'],
  ["Charley's Grill & Spirits", "Charley's Grill Spirits"],
  ['Hot Dog On A Stick', 'Hot Dog on a Stick'],
  ['L & L Hawaiian Barbecue', 'L L Hawaiian Barbecue'],
  ['Pot Belly Sandwich Works', 'Potbelly Sandwich Works'],
  ['Burger Master', 'Burgermaster'],
  ["Freddy's Frozen Custard & Steakburgers",
   "Freddy's Frozen Custard Steakburgers"]]

 most_similar_sorted = [
  ['AW Restaurant', 'AW Restaurants', 'Aw Restaurants', 'A W Restaurant', 'AWRestaurants'],
  ["Albee's NY Gyros", "Albee's Ny Gyros"],
  ["Arby's", 'Arbys'],
  ['BLIMPIE', 'Blimpie'],
  ['Back Yard Burgers', 'Backyard Burgers'],
  ["Bad Daddy's Burger Bar", 'Bad Daddys Burger Bar'],
  ['Baskin Robbins', 'BaskinRobbins', 'Baskin-Robbins'],
  ['Best Burgers', 'Best Burger'],
  ["Big Billy's Burger Joint", 'Big Billys Burger Joint'],
  ['Big Boy', 'Big Boys'],
  ["Blake's Lotaburger", 'Blakes Lotaburger'],
  ['Blimpie', 'BLIMPIE'],
  ["Bob's Burger Brew",
   "Bob's Burgers Brew"],
  ['Bojangles Famous Chicken n Biscuits',
   "Bojangles' Famous Chicken 'n Biscuits"],
  ['Burger King', 'Burger King®'],
  ['Burger Master', 'Burgermaster'],
  ['BurgerFi', 'Burgerfi'],
  ['Burgermaster', 'Burger Master'],
  ['Burrito Amigos', 'Burrtio Amigos'],
  ['C & J Drive In', 'C J Drive In'],
  ["CULVER'S", "Culver's", 'Culvers'],
  ["Captain D'S", 'Captain Ds'],
  ["Carl's Jr", "Carl's Jr.", 'Carls Jr'],
  ["Chan's Restaurant", "Chen's Restaurant"],
  ['Chanellos Pizza', 'Chanello’s Pizza'],
  ["Charley's Grill & Spirits", "Charley's Grill Spirits"],
  ["Charley's Grilled Subs", 'Charleys Grilled Subs'],
  ["Chen's Restaurant", "Chan's Restaurant"],
  ['Chick-Fil-A', 'Chick-fil-A', 'ChickfilA'],
  ['China Sea', 'China Star', 'China Bear'],
  ["Church's Chicken", 'Churchs Chicken'],
  ["Cisco's Taqueria", 'Ciscos Taqueria'],
  ['Cook Out', 'Cook-Out', 'CookOut'],
  ["Culver's", "CULVER'S", 'Culvers'],
  ['Dairy Queen', 'Dairy queen'],
  ['Dairy Queen Grill & Chill', 'Dairy Queen Grill Chill'],
  ["Dominic's of New York", 'Dominics of New York'],
  ["Domino's Pizza", 'Dominos Pizza'],
  ['Dunkin Donuts', "Dunkin' Donuts"],
  ['Einstein Bros Bagels', 'Einstein Bros. Bagels'],
  ['Emidio & Sons Italian Restaurant', 'Emidio Sons Italian Restaurant'],
  ["Famous Dave's", 'Famous Daves'],
  ["Farlow's On The Water", 'Farlows on the Water'],
  ["Fazoli's", 'Fazolis'],
  ['Fireplace Restaurant & Lounge', 'Fireplace Restaurant Lounge'],
  ['Five Guys Burgers & Fries', 'Five Guys Burgers Fries'],
  ["Fox's Pizza Den", 'Foxs Pizza Den'],
  ["Freddy's Frozen Custard & Steakburgers",
   'Freddys Frozen Custard Steakburgers',
   "Freddy's Frozen Custard Steakburgers"],
  ["Frisch's Big Boy Restaurant",
   "1 Frisch's Big Boy Restaurant",
   "40 Frisch's Big Boy Restaurant",
   "1 Frisch's Big Boy Restaurant",
   "90 Frisch's Big Boy Restaurant"],
  ['Full Moon Bar B Que', 'Full Moon Bar-B-Que'],
  ["George's Gyros Spot", "George's Gyros Spot 2"],
  ['Grub Burger Bar', 'Bru Burger Bar'],
  ["Guthrie's", 'Guthries'],
  ['Gyro Express', 'Gyro X-Press'],
  ['Gyro Spot', 'Gyro Stop'],
  ["Hardee's", 'Hardees'],
  ["Hardee's Restaurant", "Hardee's Restaurants"],
  ["Hardee's/Red Burrito", "Hardee's/red Burrito", 'Hardees Red Burrito'],
  ['HomeTown Buffet', 'Hometown Buffet'],
  ['Hooters', 'Roosters'],
  ['Hot Dog On A Stick', 'Hot Dog on a Stick'],
  ['In-N-Out Burger', 'InNOut Burger'],
  ["Jack's", 'Jacks'],
  ["Jack's Hamburgers", "Zack's Hamburgers"],
  ["Jason's Deli", 'Jasons Deli'],
  ["Jersey Mike's Subs", 'Jersey Mikes Subs'],
  ["Jimmy John's", 'Jimmy Johns'],
  ['KFC', 'Kfc', 'KFC Kentucky Fried Chicken', 'KFC - Kentucky Fried Chicken'],
  ['Killer Burger', 'Killer Burgers'],
  ['L & L Hawaiian Barbecue', 'L L Hawaiian Barbecue',
   'LL Hawaiian Barbecue'],
  ["Long John Silver's", 'Long John Silvers'],
  ['Mai Tai Restaurant', 'Mai-Tai Restaurant'],
  ["Mary's Pizza Shack", 'Marys Pizza Shack'],
  ["Mc Donald's", "McDonald's", 'Mcdonalds', 'McDonalds'],
  ["McAlister's Deli", "Mcalister's Deli", 'McAlisters Deli'],
  ["Moe's Southwest Grill", 'Moes Southwest Grill'],
  ['Mr Hero', 'Mr. Hero'],
  ['Nicholas Restaurant', "Nicholas' Restaurant"],
  ["Papa John's Pizza", 'Papa Johns Pizza'],
  ['Peking Chinese Restaurant', 'Peking Chinese Restaurants'],
  ["Pietro's Pizza & Gallery of Games", "Pietro's Pizza Gallery of Games"],
  ["Popeye's Louisiana Kitchen", 'Popeyes Louisiana Kitchen'],
  ['Pot Belly Sandwich Works', 'Potbelly Sandwich Works'],
  ['QDOBA Mexican Eats', 'Qdoba Mexican Eats'],
  ['RUNZA', 'Runza'],
  ["Raising Cane's Chicken Fingers", 'Raising Canes Chicken Fingers'],
  ["Rally's", 'Rallys'],
  ["Rally's Hamburgers", 'Rallys Hamburgers'],
  ["Rick's on the River", 'Ricks on the River'],
  ["Ritter's Frozen Custard", 'Ritters Frozen Custard'],
  ["Rockne's", 'Rocknes'],
  ['Roosters', 'Hooters'],
  ['Runza', 'RUNZA'],
  ["Ryan's", 'Ryans'],
  ['SONIC Drive In',
   'Sonic Drive-In',
   'SONIC Drive-In',
   'Sonic DriveIn',
   'Sonic Drive-in'],
  ["STEAK 'N SHAKE",
   "Steak 'n Shake",
   'Steak N Shake',
   'Steak n Shake',
   "Steak 'N Shake"],
  ['SUBWAY', 'Subway'],
  ["Sara's Too", 'Saras Too'],
  ["Simple Simon's Pizza", 'Simple Simons Pizza'],
  ['Slice Of Life', 'Slice of Life'],
  ["Stanfield's Steakhouse", 'Stanfields Steak House'],
  ['T & L Hotdogs', 'T & L Hot Dogs'],
  ['Taco CASA', 'Taco Casa'],
  ['Taco Del Mar', 'Taco del Mar'],
  ["Taco John's", 'Taco Johns'],
  ['Taco Time', 'TacoTime'],
  ['Taste Of Buffalo Pizzeria', 'Taste of Buffalo Pizzeria'],
  ['Tom Drive-in', "Tom's Drive-In"],
  ["Topper's Pizza", 'Toppers Pizza'],
  ['WG Grinders', 'Wg Grinders'],
  ["Wendy's", 'Wendys'],
  ['Wg Grinders', 'WG Grinders'],
  ['Wing Street', 'Wingstreet'],
  ['Z-Pizza', 'zpizza'],
  ["Zack's Hamburgers", "Jack's Hamburgers"]]
 print("cleaned, matched restaurant name count:", len(most_similar_sorted))

 # let's sort them by the first element of each sublist
 def sortFirst(val):
     return val[0]

 # sorts the array in ascending according to 1st element
 most_similar_edited.sort(key = sortFirst)
 most_similar_edited

 match_name_dict = {}
 for row in most_similar_sorted:
     for similar_word in row:
         match_name_dict[similar_word] = row[0]
 match_name_dict

 names = ffd['name'].values
 print("size:", len(names))

 # replace names with their dictionary value
 for i in range(len(names)):
     if match_name_dict.get(names[i]) != None:
         names[i] = match_name_dict[names[i]]

 ffd['names'] = names



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
