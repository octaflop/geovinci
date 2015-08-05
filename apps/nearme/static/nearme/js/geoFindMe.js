function geoFindMe(map) {
  var output = document.getElementById("info");

  if (!navigator.geolocation){
    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
    return;
  }

  function success(position) {
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;

    map.setView([latitude, longitude], 13);
    var marker = L.marker([latitude, longitude], {
    icon: L.mapbox.marker.icon({
      'marker-color': '#31708f'
      }),
    draggable: true
    });
    console.debug(latitude, longitude);

    marker.on('dragend', function(e){
      console.debug(marker.getLatLng());
      latlng = marker.getLatLng();
      window.location.href = window.location.origin + window.location.pathname + "?lat=" + latlng.lat + "&lng=" + latlng.lng;
    });
    output.innerHTML = "<p>Location from HTML5: <code>" + latitude + ", " + longitude + "</code></p>";
    marker.addTo(map);
  };

  function error() {
    output.innerHTML = "Unable to retrieve your location via HTML5";
  };

  output.innerHTML = "<p>Locating…</p>";

  navigator.geolocation.getCurrentPosition(success, error);
}