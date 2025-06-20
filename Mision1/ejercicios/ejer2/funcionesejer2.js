let contador = 0;
function contar(){
    
    const resultadodiv=document.getElementById("resultado");
    contador=contador+1;
    console.log(contador);
    resultadodiv.innerHTML=`<h2>Ha dado esta cantidad de clicks:  ${contador}</h2>`;

}