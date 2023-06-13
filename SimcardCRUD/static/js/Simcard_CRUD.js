// $('#myModal').on('shown.bs.modal', function () {
//   $('#myInput').trigger('focus')
// })

var myModal = document.getElementById('myModal');
var myInput = document.getElementById('myInput');

// window.onload=function(){
//     var mb = document.getElementById("b");
//     mb.addEventListener("click", handler);
//     mb.addEventListener("click", handler2);
// }

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})


// var myDropdown_item = document.getElementById('dropdown-item');
// var ServiceType_input = document.getElementById('ServiceType-name');

// function hello(inputtext) {
// 	alert("It is working");
// 	alert(ServiceType_input);
// 	ServiceType_input.value = "Super";
// 	alert(myDropdown_item);
// }



// document.getElementById("dropdown-item").addEventListener("click", hello);

// myDropdown_item.onclick = function(){
// 	alert("It is working");
// 	// ServiceType_input.setAttribute('value', myDropdown_item.innerHTML);
// };