/**
 * Created by Usuario on 6/05/2018.
 */

var tempContainer = document.getElementById("temp");
var humContainer = document.getElementById("hum");
var npeopleContainer = document.getElementById("num-people")
var temp = "";
var hum = "";
var npeople = "";

$(document).ready(function getThingspeak() {

    $.getJSON('https://api.thingspeak.com/channels/240810/feeds.json?results=1', function thingGet(ourData) {

        var data = ourData["feeds"];

        temp = data[0].field1;
        hum = data[0].field2;
        npeople = data[0].field3;

        if (temp == null){
            temp = 0;
        }else if(hum == null){
            hum = 0;
        }else if(npeople == null){
            npeople = 0;
        }

        console.log(temp,hum,npeople);

        tempContainer.innerHTML = temp;
        humContainer.innerHTML = hum;
        npeopleContainer.innerHTML = npeople;

        setTimeout(getThingspeak,60000);

    });
});

