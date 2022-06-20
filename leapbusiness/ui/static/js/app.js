const start = () => {
  console.log("Start");
  document.getElementById("start").setAttribute('disabled', '');
  const request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
  const url = "/start";
  request.open("GET", url, true);
  request.send();
  request.onload = () => {
    if(request.status == 200){
      const status = JSON.parse(request.responseText);
      document.getElementById("status").innerHTML = status.status;
      document.getElementById("start").removeAttribute('disabled');
    }
  }
}