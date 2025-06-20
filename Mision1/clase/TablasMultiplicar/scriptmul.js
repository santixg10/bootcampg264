let resultado;
function multiplicar(){
    nume=prompt("digite el numero de la tabla quiere saber")
     console.log("La tabla que se va a mostrar es: "+nume);
    for (let i=1;i<=10;i++){
       
        resultado=nume*i;
        console.log(nume+" * "+i+" =", resultado);
    }
}
/* window.onload=multiplicar; */
/* function mostraralerta(){
           multiplicar;
        }
        function hacerclic(){
            document.getElementsByTagName("h1")[0].onclick = mostraralerta;

} */
function btnclic(){
    document.getElementsByTagName("h1")[0].onclick = multiplicar;
}
window.onload = btnclic; 