$(document).ready(function () {
    $("select").formSelect();
    $(".sidenav").sidenav();
    $(".button-collapse").sidenav();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    $('.fixed-action-btn').floatingActionButton();
    
    var max_fields      = 10; //maximum input boxes allowed
    var ingredient_wrapper   		= $(".ingredient_fields_wrapper"); // Ingredients fields wrapper
    var method_fields_wrapper   		= $(".method_fields_wrapper"); // Method fields wrapper
    var add_ingredient_button      = $(".add_ingredient_button"); //Add ingredient ID
    var add_method_step_button      = $(".add_method_step_button"); //Add step to method ID
    var ingredient_count = 1; //initial ingredient count
    var method_step_count = 1; //initial method step count
	
	$(add_ingredient_button).click(function(e){ //on add ingredient button click
		e.preventDefault();
		if(ingredient_count < max_fields){ //max input box allowed
			ingredient_count++; //ingredient increment
			$(ingredient_wrapper).append('<div><input type="text" name="ingredients" class="validate"/><a href="#" class="btn-small btn-colour remove_field">Remove</a></div>'); //add ingredient box
		}
	});
	
	$(ingredient_wrapper).on("click",".remove_field", function(e){ //user click on remove ingredient
		e.preventDefault(); $(this).parent('div').remove(); ingredient_count--;
    })
    
    $(add_method_step_button).click(function(e){ //on add method step button click
		e.preventDefault();
		if(method_step_count < max_fields){ //max method step box allowed
			method_step_count++; //method step box increment
			$(method_fields_wrapper).append('<div><input type="text" name="method" class="validate"/><a href="#" class="btn-small btn-colour remove_field">Remove</a></div>'); //add method step box
		}
	});
	
	$(method_fields_wrapper).on("click",".remove_field", function(e){ //user click on remove method step
		e.preventDefault(); $(this).parent('div').remove(); method_step_count--;
    })
});