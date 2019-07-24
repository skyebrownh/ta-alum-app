// DOM constants
const memberGroup = document.querySelector('.member-group');

// instantiate map object
const map = L.map('mapid').setView([38.0406, -84.5037], 5);

// add tile layer
L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=bZBPrAxMkP6v1Se4TGyK', {
  attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>',
}).addTo(map);

// create icon for marker
const icon = L.icon({
  iconUrl: '/static/images/ainc-logo-triangle-layer-red.png',
  iconSize: [40, 40],
});

// add marker and get popup info for each member
for (let i = 1; i <= num_members; i++) {
  // get this member's popup
  const popupInfo = memberGroup.querySelector(`#member_${i}`);

  // get lat, long and populate location to display marker
  const latlong = popupInfo.querySelector('.latlong');
  const latitude = parseInt(latlong.querySelector('#lat').textContent);
  const longitude = parseInt(latlong.querySelector('#long').textContent);
  
  // use latitude, longitude for marker location
  const marker = L.marker([latitude, longitude], {
    icon: icon,
    title: `${memberGroup.querySelector('.location-point')}`,
    alt: `${memberGroup.querySelector('.location-point')}`,
    riseOnHover: true,
  }).addTo(map);

  const boundMarker = marker.bindPopup(popupInfo);

  marker.addEventListener('click', () => {
    boundMarker.openPopup();
  });
}
