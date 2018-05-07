/**
 * Created by Usuario on 6/05/2018.
 */

var tempContainer = document.getElementById("temp");
var humContainer = document.getElementById("hum");
var npeopleContainer = document.getElementById("num-people")
var temp = "";
var hum = "";
var npeople = "";

$(document).ready(function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET','https://api.thingspeak.com/channels/240810/feeds.json?results=1');
    ourRequest.onload = function () {
        var ourData = JSON.parse(ourRequest.responseText);
        var data = ourData["feeds"];

        temp = data[0].field1;
        hum = data[0].field2;
        npeople = data[0].field3;

        console.log(temp,hum,npeople);

        tempContainer.insertAdjacentHTML('beforeend',temp);
        humContainer.insertAdjacentHTML('beforeend', hum);
        npeopleContainer.insertAdjacentHTML('beforeend', npeople);

    };

    ourRequest.send();
});

