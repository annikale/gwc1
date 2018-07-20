// My Variables!
var map;
var ourLoc;
var view;

// Initialize a function
function init(){
  // longitude and latitude values
  ourLoc = ol.proj.fromLonLat([-84.3869,33.7739]);

  view = new ol.View({
    center: ourLoc,
    zoom: 18 // You can change this value for aesthetics
  });

  map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000 // 2000 milliseconds = 2 seconds
  });
}

// function panToCountry(){
//   var countryName = document.getElementById("country-name").value;
//
//   if(countryName === ""){
//     alert("You didn't enter a country name!");
//     return;
//   }
//
//   var lon = 0.0;
//   var lat = 0.0;
//
//   // Find variables from REST Countries API
//   var query = "https://restcountries.eu/rest/v2/name/"+countryName;
//   query = query.replace(/ /g, "%20")
//   alert(query);
//
//   var countryRequest = new XMLHttpRequest();
//   countryRequest.open('GET', query, false);
//   countryRequest.send();
//
//   // Show alerts for debugging
//   // alert("Ready State" + countryRequest.readyState);
//   // alert("Status" + countryRequest.status);
//   // alert("Response" + countryRequest.responseText);
//
//   if(countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === ""){
//     alert("Request had an error!");
//     return;
//   }
//
//   // use JSON to get requested information
//   var countryInformation = JSON.parse(countryRequest.responseText);
//
//   lat = countryInformation[0].latlng[0];
//   lon = countryInformation[0].latlng[1];
//
//   alert(countryName + ": Lon" + lon + "& Lat" + lat);
//
//   var location = ol.proj.fromLonLat([lon,lat]);
//
//   view.animate({
//     center: location,
//     duration: 2000
//   });
// }

function makeCountryRequest(){
  var countryName = document.getElementById("country-name").value;

  if(countryName === ""){
    alert("You didn't enter a country name!");
    return;
  }

  // Find variables from REST Countries API
  var query = "https://restcountries.eu/rest/v2/name/"+countryName+"?fullText=true" //;
  query = query.replace(/ /g, "%20")

  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, true);
  countryRequest.onload = processCountryRequest

  // Send the GET request
  countryRequest.send();
}

function processCountryRequest(){
  var lon = 0.0;
  var lat = 0.0;

  if(countryRequest.readyState != 4){
    return;
  }

  if(countryRequest.status != 200 || countryRequest.responseText === ""){
    alert("We were unable to find your requested country.");
    return;
  }

  // use JSON to get requested information
  var countryInformation = JSON.parse(countryRequest.responseText);

  lat = countryInformation[0].latlng[0];
  lon = countryInformation[0].latlng[1];

  // alert(countryName + ": Lon" + lon + "& Lat" + lat);

  var location = ol.proj.fromLonLat([lon,lat]);

  view.animate({
    center: location,
    duration: 2000
  });
}

window.onload = init;
