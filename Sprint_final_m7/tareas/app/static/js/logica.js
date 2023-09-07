// animacion para los imput del formulario de contacto del index
var inputs = document.getElementsByClassName('formulario__input');
for (var i = 0; i < inputs.length; i++) {
  inputs[i].addEventListener('keyup', function(){
    
    if(this.value != null ) {
      this.nextElementSibling.classList.add('fijar');
    } else {
      this.nextElementSibling.classList.remove('fijar');
    }
  });
}
