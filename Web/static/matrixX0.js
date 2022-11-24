matrixX0Create();

function matrixX0Create(){
  let x = document.getElementById("size").value;
  let matrixA = document.getElementById("matrixA");
  let matrixX0 = document.getElementById("matrixX0");
  let matrixb = document.getElementById("matrixb");
  while(matrixA.hasChildNodes()){
    matrixA.removeChild(matrixA.lastChild);
  }
  while(matrixX0.hasChildNodes()){
    matrixX0.removeChild(matrixX0.lastChild);
  }
  while(matrixb.hasChildNodes()){
    matrixb.removeChild(matrixb.lastChild);
  }
  for(var i = 0; i < x; i++){
    for(var j = 0; j < x; j++){
      var input = document.createElement("input");
      input.type = "text";
      input.name = "A"+i;
      input.size = "2";
      input.placeholder = "A"+i+""+j;
      matrixA.appendChild(input);
    }
    matrixA.appendChild(document.createElement("br"));
    var inputX0 = document.createElement("input");
    inputX0.type = "text";
    inputX0.name = "x"+i;
    inputX0.size = "2";
    inputX0.placeholder = "x"+i;
    matrixX0.appendChild(inputX0);
    matrixX0.appendChild(document.createElement("br"));
    var inputb = document.createElement("input");
    inputb.type = "text";
    inputb.name = "b"+i;
    inputb.size = "2";
    inputb.placeholder = "b"+i;
    matrixb.appendChild(inputb);
    matrixb.appendChild(document.createElement("br"));
  }
}