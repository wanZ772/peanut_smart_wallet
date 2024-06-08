var retrieve_data = new XMLHttpRequest();

current_position = "";

function show_position(position){
    coordinate = position.coords;
    current_position = coordinate.latitude +","+ coordinate.longitude;
}



function check_wallet()
{
    // navigator.geolocation.getCurrentPosition(show_position);
    user_alert = new Audio('/alert.mp3');
    // user_alert.autoplay = true;
    try {
        retrieve_data.open( "GET", window.location.href + "/check", false ); // false for synchronous request
        retrieve_data.send( null );
       if (retrieve_data.responseText == "True")    {
        navigator.geolocation.getCurrentPosition(show_position);
        // alert(current_position);
        document.getElementById("wallet_status").innerHTML = "Wallet Connection:\t" + retrieve_data.responseText;
       }    else    {
        
        document.getElementById("wallet_status").innerHTML = "Wallet Connection:\t" + retrieve_data.responseText + "<br>Last Location: " + current_position;
        user_alert.play();
        clearInterval(keep_checking);
       
       }
    }   catch(e)    {
        clearInterval(keep_checking);
    } 
   
}

function test() {
    alert(1);
}

var keep_checking = setInterval(check_wallet, 500);