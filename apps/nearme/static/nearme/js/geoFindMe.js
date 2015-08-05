function geoFindMe(map) {
  var output = document.getElementById("info");

  if (!navigator.geolocation){
    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
    return;
  }

  function success(position) {
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;

    map.setView([latitude, longitude], 8);
    var marker = L.marker([latitude, longitude], {
    icon: L.mapbox.marker.icon({
      'marker-color': '#f86767'
      })
    });
    marker.addTo(map);
  };

  function error() {
    output.innerHTML = "Unable to retrieve your location via HTML5";
  };

  output.innerHTML = "<p>Locating…</p>";

  navigator.geolocation.getCurrentPosition(success, error);
}