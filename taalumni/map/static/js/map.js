// DOM constants
const memberGroupList = document.querySelector('.member-group>ul');

// instantiate map object
const map = L.map('mapid').setView([38.0406, -84.5037], 4);

// add tile layer
L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=bZBPrAxMkP6v1Se4TGyK', {
  attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>',
}).addTo(map);

// create icon for marker
const icon = L.icon({
  iconUrl: '/static/images/ainc-logo-triangle-layer-red.png',
  iconSize: [40, 40],
});

// create marker cluster to group duplicate/geographically close markers
const markerCluster = L.markerClusterGroup();

// get collection of memberGroupList child divs
const memberCollection = memberGroupList.getElementsByClassName('popup-info');

// add marker and get popup info for each member
for (let i = 0; i < memberCollection.length; i++) {
  // get member popup
  const popupInfo = memberCollection[i];

  // get lat, long and populate location to display marker
  const latlong = popupInfo.querySelector('.latlong');
  const latitude = parseInt(latlong.querySelector('#lat').textContent);
  const longitude = parseInt(latlong.querySelector('#long').textContent);
  
  // use latitude, longitude for marker location
  const marker = L.marker([latitude, longitude], {
    icon: icon,
    title: `${popupInfo.querySelector('.location-point')}`,
    alt: `${popupInfo.querySelector('.location-point')}`,
    riseOnHover: true,
    riseOffset: 250
  });

  // add to marker cluster
  markerCluster.addLayer(marker);

  const boundMarker = marker.bindPopup(popupInfo);

  marker.addEventListener('click', () => {
    boundMarker.openPopup();
  });
}

map.addLayer(markerCluster);
