const request = (url) => {
  document.querySelectorAll('button').forEach(e => e.setAttribute('disabled', '')) ;
  const request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
  request.open("GET", url, true);
  request.send();
  request.onload = () => {
    if(parseInt(parseInt(request.status)/100) != 2){
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Something went wrong while updating the data',
      })
      document.querySelectorAll('button').forEach(e => e.removeAttribute('disabled'));
    }else{
      document.querySelectorAll('button').forEach(e => e.removeAttribute('disabled'));
    }
  }
}

const gameData = () => {
  request("/api/game-data")
}

const metacritic = () => {
  request("/api/metacritic")
}

const steamPrice = () => {
  request("/api/steamprice")
}

const steamCharts = () => {
  request("/api/steamcharts")
}

const fullUpdate = () => {
  request("/api/full-update")
}