function mostrarTabla(){
    const numero = document.getElementById("numero").value;
    const resultadodiv=document.getElementById("resultado");
    if (numero===""){    /* triple igual valida si se esta igualando un txt con un txt o numero con un numero */
        resultadodiv.innerHTML="<p class='error'> ingresa un número</p> "/* si el usuarioo no ingresa ningun numero va a salir un mensaje avisandole que lo haga */
        return;/* si el usuario no inserta un numero el codigo parara hast aca osea se devolvera */
    }
    let resultado =`<h2>Tabla del ${numero}</h2>`;     /* alt gr+ }} 2 veces */
    for(let i=1;i<=10;i++){
        resultado+=`<p>${numero} x ${i} = ${numero*i}</p>`;
    }
    resultadodiv.innerHTML=resultado;
}