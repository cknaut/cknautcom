function refresh_reading(){   
    $.getJSON( "/temp/temp_ajax/", function( data ) {
      $('#temp').html(data.temp);
      $('#hum').html(data.hum);
      $('#timestamp').html(data.timestamp);
    });
};
setInterval(function () {refresh_reading()}, 60000);
