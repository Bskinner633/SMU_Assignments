### Lesson 1 - Data Visualization with Leaflet  
* Understand advantages gained by visualizing data in a geographical context
* Basics of creating maps and plotting data with Leaflet.js library
* Gain an understanding of GeoJSON format
* Understand concepts of layers and layer controls and how to use them to add interactivity to our maps


1) 01-Ins_Basic_Map  
* Map Object L.map two arguments  
    a) id of HTML element Leaflet insert map into  
    b) object containing initial options for the new map ("center" and zoom" for this example)  
* Tile Layer use various tile layer APIs here using Mapbox API  
    a) passing formatted queryURL to tileLayer method  
    b) add layer to map with addTo method.  Invoke this method when want to add something to map  
* API Key config.js must be referenced before logic.js in HTML file     
**Additional Resources**  
[Mapping the Spread of Drought Across the U.S.](https://www.nytimes.com/interactive/2014/upshot/mapping-the-spread-of-drought-across-the-us.html?_r=0)  
[Understand and Predict Zika In Brazil With Spatial Analysis](https://carto.com/blog/understand-and-predict-zika-in-brazil/)  
[Spotify - Musical Map of the World](https://insights.spotify.com/us/2016/12/07/musical-map-of-the-world-2-0/)  
[Leaflet.js web-page](https://leafletjs.com/)  
[leafLet quick start](https://leafletjs.com/examples/quick-start/)  
[mapbox](https://www.mapbox.com/)  
[mapbox token](https://account.mapbox.com/access-tokens/)  
[mapbox API documentation](https://docs.mapbox.com/api/#maps)  

2) 02-Ins_Markers  
* add new marker to map by creating marker object and using addTo() method  
* pass coordinates to marker adding ability to make `draggable` and added a `title`  
* Also can add popups to markers using `marker.bindPopup('Hello There!')`  
**Additional Resources**  
[Leaflet marker documentation](https://leafletjs.com/reference-1.0.3.html#marker-option)  

3) 03-Stu_City_Markers  
* notice used loop statement to create the markers  
* `bindPopup` method to attach popups to marker objects
* `addTo` method used to add markers to map  
* `L.marker` receives coordinates for new marker and any otehr config want to pass to new marker such as `title` or `draggable`  

4) 04-Ins_Other_Markers  
* Leaflet allows us to define and plot SVG shapes to use as markers.  SVG layers refered to as 'vector layers' in Leaflet API.  
*  various SVG layers able to add `L.circle`, `L.polygon`, `L.polyline`, `L.rectangle`  
**Additional Resources**  
[Path Options](https://leafletjs.com/reference-1.5.0.html#path)  

5) 05-Stu_Other_Markers  
* practice with markers and vector shapes.  
    * arguments vectors layers accept:  array of coordinates for where vector should appear  
    * style options applied to vector shapes

6) 06-Ins_City_Population **Basic homework example**  
* replacing orginal marker with vector layer whose size is proportional to pop of city represents,  
* controlled size of circle vector layer by adjusting `radius`  using a defined function markerSize

7) 07-Stu_Country_World_Cup  
* practice from previous example  

8) 08-Ins_Layers **Homework Optional basic example**  
* **layer control** allows us to toggle between layers  
* Two types of layers with Leaflet:  
    * Base Layers - mutually exclusive to one another.  Can only see one or the other at a given time  
    * Overlays - these go **over** base layers and can be turned off entirely.  
* `L.layerGroup` allows us to toggle on or off related markers as a group  
* add layer control to map `L.control.layers(baseMaps, overlayMaps).addTo(myMap);`  
**Additional Resources**  
[The Layer Group and Layers Control](https://leafletjs.com/examples/layers-control/)  

9) 09-Stu_City_Population_Layers  
* practice previous example

10) 10-Stu_Geo-Json  
* GeoJSON open standard format for representing simple geographical features along with non-spatial attributes. `L.geoJSON` method will know what kind of marker should make and where to place it.  
* Geographical features represented by coordinates and can have other properties associacted with them
* different types of features  
    a) Point  
    b) LineString  
    c) Polygon  
    d) MultiPoint  
    e) MultiLineString  
    f) MultiPolygon  
    
**Additional Resources**  
[Earthquake JSON](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson)  
[USGS Documentation](https://earthquake.usgs.gov/data/comcat/data-eventterms.php)  


### Lesson 2 - GeoJSON & Leaflet Plugins  
* Able to grasp mapping with GeoJSON
* Learn and practice using Leaflet plugins and third-party libraries
* Learn different maps can visualize different datasets


1) 01-Evr_BasicNYCBoroughs  
* GeoJSON contains array of `features` both geographic data (geometry) and descriptive information (properties).  
* Features styled like paths, changing border, fill, color, opacity, etc.    
    a. Logic 2 - basic style object  
    b. Logic 3 - advanced style with function using switch to style individual features based on properties `features.properties.borough`    
    c. Logic 4 - add `onEachFunction` for interaction, specifically mouse events `fitbounds()` - Sets a map view that contains the given geographical bounds with the maximum zoom level possible.   
    
**Additional Resources**  
[BetaNYC data documentation](http://data.beta.nyc/dataset/pediacities-nyc-neighborhoods)  
[BetaNYC dataset](http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson)  
[Leaflet references](https://leafletjs.com/reference-1.5.0.html)  

2) 02-Evr_CrimeHeatmap  
* Plugins for Leaflet for additional features  
* learning how to read documentation  

**Additional Resources**  
[Leaflet Plugins](https://leafletjs.com/plugins.html)  
[San Francisco Data](https://datasf.org/opendata/)  
[San Fran data for exercise](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry)  
[San Fran Police API](https://dev.socrata.com/foundry/data.sfgov.org/tmnf-yvry)  
[Leaflet.heat](https://github.com/Leaflet/Leaflet.heat)  

3) 03-Stu_MarkerClusters  
* Building API query URL  
* creating marker group clusters  `L.markerClusterGroup()`
* step wise functions and loop to build graph  

**Additional Resources**  
[Leaflet markerClusterGroup](https://github.com/Leaflet/Leaflet.markercluster)  
[date format and other parameters for end point](https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9)
[generic soda $ parameters](https://dev.socrata.com/docs/queries/)

4) 04-Par_MoneyChoropleth  

**Additional Resources**
[Leaflet choropleth](https://github.com/Leaflet/Leaflet.markercluster)  


### Lesson 3 - More Leaflet  
* Gain mastery of Leaflet by completing in-class project
* Form project 2 teams and draft project 2 proposals


1) 01-Stu_CitiBike
* Basic Activity: combining leaflet with API `GET` request to render map
* Advanced Activity: Calling two API `GET` requests to garner additional information on station status.  
    * expanded css style sheet to include legend and use leaflet.extra-markers styling
    * expanded index.html to include additional styling and js script incorporation  
    * calling two api's  
//Perform an API call to the Citi Bike Station Information endpoint
d3.json("https://gbfs.citibikenyc.com/gbfs/en/station_information.json", function(infoRes) {  
//When the first API call is complete, perform another call to the Citi Bike Station Status endpoint  
  d3.json("https://gbfs.citibikenyc.com/gbfs/en/station_status.json", function(statusRes) {  
    var updatedAt = infoRes.last_updated;  
    var stationStatus = statusRes.data.stations;  
    var stationInfo = infoRes.data.stations;  

**Additional Resources**  
[CitiBike API](https://www.citibikenyc.com/system-data)  
[CitiBike Information Endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json)  
[CitiBike Station Status Endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_status.json)
    


# Leaflet Homework - Visualizing Data with Leaflet

## Background

![1-Logo](Images/1-Logo.png)

Welcome to the United States Geological Survey, or USGS for short! The USGS is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment; and the impacts of climate and land-use change. Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes. As a new hire, you will be helping them out with an exciting new project!

The USGS is interested in building a new set of tools that will allow them visualize their earthquake data. They collect a massive amount of data from all over the world each day, but they lack a meaningful way of displaying it. Their hope is that being able to visualize their data will allow them to better educate the public and other government organizations (and hopefully secure more funding..) on issues facing our planet.

### Before You Begin

1. Create a new repository for this project called `leaflet-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. Inside your local git repository, create a directory for the Leaflet challenge. Use the folder names to correspond to the challenges: **Leaflet-Step-1** and **Leaflet-Step-2**.

4. This homeworks utilizes both **html** and **Javascript** so be sure to add all the necessary files. These will be the main files to run for analysis.

5. Push the above changes to GitHub or GitLab.

## Your Task

### Level 1: Basic Visualization

![2-BasicMap](Images/2-BasicMap.png)

Your first task is to visualize an earthquake data set.

1. **Get your data set**

   ![3-Data](Images/3-Data.png)

   The USGS provides earthquake data in a number of different formats, updated every 5 minutes. Visit the [USGS GeoJSON Feed](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) page and pick a data set to visualize. When you click on a data set, for example 'All Earthquakes from the Past 7 Days', you will be given a JSON representation of that data. You will be using the URL of this JSON to pull in the data for our visualization.

   ![4-JSON](Images/4-JSON.png)

2. **Import & Visualize the Data**

   Create a map using Leaflet that plots all of the earthquakes from your data set based on their longitude and latitude.

   * Your data markers should reflect the magnitude of the earthquake in their size and color. Earthquakes with higher magnitudes should appear larger and darker in color.

   * Include popups that provide additional information about the earthquake when a marker is clicked.

   * Create a legend that will provide context for your map data.

   * Your visualization should look something like the map above.

- - -

### Level 2: More Data (Optional)

![5-Advanced](Images/5-Advanced.png)

The USGS wants you to plot a second data set on your map to illustrate the relationship between tectonic plates and seismic activity. You will need to pull in a second data set and visualize it along side your original set of data. Data on tectonic plates can be found at <https://github.com/fraxen/tectonicplates>.

In this step we are going to..

* Plot a second data set on our map.

* Add a number of base maps to choose from as well as separate out our two different data sets into overlays that can be turned on and off independently.

* Add layer controls to our map.

- - -

### Assessment

Your final product will be assessed on the following metrics:

* Completion of assigned tasks

* Visual appearance

* Professionalism

**Good luck!**

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
