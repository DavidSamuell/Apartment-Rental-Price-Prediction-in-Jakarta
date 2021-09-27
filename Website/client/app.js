
function getTotalBedroom() {
    var uiBedroom = document.getElementsByName("uiBedroom");
    for(var i in uiBedroom) {
      if(uiBedroom[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var bedroom = getTotalBedroom();
    var apt_size = document.getElementById('uiApartSize');
    var max_watt = document.getElementById('uiWatt');
    var furnish_type = document.getElementById("uiFurnishType");
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_home_price"; 
    // var url = "/api/predict_home_price";
  
    $.post(url, {
        bedroom: bedroom,
        apt_size: parseInt(apt_size.value),
        max_watt: parseInt(max_watt.value),
        furnish_type: furnish_type.value,
        location: location.value
    }
    ,function(data, status) {
        console.log(bedroom)
        estPrice.innerHTML = "<h2> Rp. " + data.estimated_price.toString() + "</h2>";
        console.log(status);
    });
  }

function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; 
    // var url = "/api/get_location_names";

    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }

  window.onload = onPageLoad;