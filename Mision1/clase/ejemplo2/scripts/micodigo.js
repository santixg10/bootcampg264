 function mostraralerta(){
            alert('Hizo clic')
        }
        function hacerclic(){
            document.getElementsByTagName("p")[0].onclick = mostraralerta;
        }
        window.onload = hacerclic;/* cuando termine de cargar el documento, ejecute esto */