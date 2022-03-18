function intcheck () {
  var form = document.getElementById("price","interest","term");
  var form_value = form.value;
  
  if (form_value.match(/[0-9]+/g) != form_value ) {
  	alert('数値以外やめてください');
    form.value = '';
  } 
}

