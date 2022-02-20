/**
* Différent "layer" avec fond de carte...
*/
let layerOSM = {
   url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
   attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors'
};

let layerOSMNB = {
   url: 'http://{s}.www.toolserver.org/tiles/bw-mapnik/{z}/{x}/{y}.png',
   attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors'
};

let layerSatellite = {
   url: 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
   attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
};
function markColor(color = 'blue') {
   return L.icon({
      iconUrl: `img/marker-${color}.svg`,
      iconSize: [25, 41],
      iconAnchor: [12, 82],
      popupAnchor: [0, -41]
   });
}
