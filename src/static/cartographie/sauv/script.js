// document.addEventListener("DOMContentLoaded", function(){
//     chargerDonnees();
// });
// async function chargerDonnees(){
//   let urlData= 'https://opendata.hauts-de-seine.fr/api/records/1.0/search/?dataset=communes&q=&rows=21&sort=code_insee&facet=nom_comm&facet=ept';

//   let resp = await fetch(urlData);
//   let datas = await resp.json();
// //   console.log(datas);

  
// }
let centre = {lat: 48.9070, lng: 2.2468};
let map = L.map('mapid').setView(centre, 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
  
L.marker(centre).addTo(map);
L.marker({lat: 48.9070, lng: 2.2437}).addTo(map);
L.marker([48.9070,2.2403]).addTo(map);

map.on('click', function(e) {
   let lat = parseFloat(e.latlng.lat).toFixed(4);
   let lng = parseFloat(e.latlng.lat).toFixed(4);
    console.log(lat, lng) ;
});

