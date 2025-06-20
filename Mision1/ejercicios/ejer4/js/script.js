function cambiarColor(){
    let color = "#" + Math.floor(Math.random()*16777215).toString(16); /* ese numero es el mas alto en hexadecimal */
    /* #ffffff*/
    console.log(color);
    document.body.style.backgroundColor = color;
}
   