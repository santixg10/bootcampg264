function imc(){
    const estatura = document.getElementById("numeestatura").value;
    const peso = document.getElementById("numepeso").value;
    const resultadodiv=document.getElementById("resultado");
    if(estatura===""){
        resultadodiv.innerHTML="<p class='error'> ingresa su estatura</p> "
    } else if(peso===""){
        resultadodiv.innerHTML="<p class='error'> ingresa su peso</p> "
    }else{
        calimc= peso/(estatura*estatura);
        calimc+=`<p> su indice de masa corporal(IMC) es: ${calimc}</p>`;
    }
    resultadodiv.innerHTML=calimc;
}
