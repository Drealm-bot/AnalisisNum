matrixCreate();

  function matrixCreate(){
    let x = document.getElementById("size").value;
    let matrixA = document.getElementById("matrixA");
    let matrixb = document.getElementById("matrixb");
    while(matrixA.hasChildNodes()){
      matrixA.removeChild(matrixA.lastChild);
    }
    while(matrixb.hasChildNodes()){
      matrixb.removeChild(matrixb.lastChild);
    }
    for(var i = 0; i < x; i++){
      for(var j = 0; j < x; j++){
        var input = document.createElement("input");
        input.type = "text";
        input.name = "A"+i;
        input.size = "3";
        input.placeholder = "A"+i+""+j;
        matrixA.appendChild(input);
      }
      matrixA.appendChild(document.createElement("br"));
      var inputb = document.createElement("input");
      inputb.type = "text";
      inputb.name = "b"+i;
      inputb.size = "3";
      inputb.placeholder = "b"+i;
      matrixb.appendChild(inputb);
      matrixb.appendChild(document.createElement("br"));
    }
  }