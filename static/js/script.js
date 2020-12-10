$(document).ready(function () {
    $("select").formSelect();
    $(".sidenav").sidenav();
    $(".button-collapse").sidenav();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    
    var max_fields      = 10; //maximum input boxes allowed
	var ingredient_wrapper   		= $(".ingredient_fields_wrap"); //Fields wrapper
    var add_ingredient_button      = $(".add_ingredient_button"); //Add ingredient ID

	
	var ingredient_count = 1; //initial text box count
	$(add_ingredient_button).click(function(e){ //on add input button click
		e.preventDefault();
		if(ingredient_count < max_ingredient_fields){ //max input box allowed
			ingredient_count++; //text box increment
			$(wrapper).append('<div><input type="text" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
		}
	});
	
	$(ingredient_wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});