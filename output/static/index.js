var date = new Date();

function setDate() {
  let date = new Date();
  date = date.toLocaleString('en-GB', { timeZone: 'UTC' });
  let dateElement = document.getElementById('footer-date');
  dateElement.innerHTML = date;
}

setDate();
