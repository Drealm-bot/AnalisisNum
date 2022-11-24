arrayCreate();

  function arrayCreate(){
    let x = document.getElementById("size").value;
    let arrayX = document.getElementById("arrX");
    let arrayY = document.getElementById("arrY");
    while(arrayX.hasChildNodes()){
      arrayX.removeChild(arrayX.lastChild);
    }
    while(arrayY.hasChildNodes()){
      arrayY.removeChild(arrayY.lastChild);
    }
    for(var i = 0; i < x; i++){
        var inputx = document.createElement("input");
        inputx.type = "text";
        inputx.name = "x"
        inputx.size = "3";
        inputx.placeholder = "x"+i;
        arrayX.appendChild(inputx);
    }
    arrayX.appendChild(document.createElement("br"));
    for(var i = 0; i < x; i++){
      var inputy = document.createElement("input");
      inputy.type = "text";
      inputy.name = "y";
      inputy.size = "3";
      inputy.placeholder = "y"+i;
      arrayY.appendChild(inputy);
    }
    arrayY.appendChild(document.createElement("br"));
  }