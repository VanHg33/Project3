console.log("logic-Van-heatmap.js")

// Build base map
// Use https://leaflet-extras.github.io/leaflet-providers/preview/
// basemap is Esri.WorldGrayCanvas
let basemap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',
	maxZoom: 16
});

// geomap is Esri.NatGeoWorldMap
var geomap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',
	maxZoom: 16
});

let myMap = L.map("map", {
    center: [
        -27, 133
    ],
    zoom: 3
});

geomap.addTo(myMap);

// Build the menu
let baseMaps = {
    "Data Jobs Heatmap": basemap,
    "Australia Map": geomap
};

// Get Labels on Aus Map with Stadia.StamenTerrainLabels
let mapLabels = new L.LayerGroup();
let heatmap = new L.LayerGroup();

let overlays = {
    "Map Labels": mapLabels,
    "Australia Data Jobs OutLook": heatmap
};

L
    .control
    .layers(baseMaps, overlays, { collapsed: false })
    .addTo(myMap);


   