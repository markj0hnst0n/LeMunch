window.onload = function(){ document.querySelector("#preloader").style.display = "none"; }

$(document).ready(function () {
    /*
    jQuery code to initalize some of the js funtionality in Materialize framework
    */
    $("select").formSelect();
    $(".sidenav").sidenav();
    $(".button-collapse").sidenav();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    $('.fixed-action-btn').floatingActionButton();

    /*
    Tim Nelson's jQuery function that validates recipe type selections and makes sure the user chooses a recipe type
    */

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
    
    /*
    jQuery functions from Sanwebe.com which create and remove ingredient and method steps boxes dynamically on the screen
    */

    const max_fields      = 10; //maximum input boxes allowed
    const ingredient_wrapper   		= $("#ingredient_fields_wrapper"); // Ingredients fields wrapper
    const method_fields_wrapper   		= $("#method_fields_wrapper"); // Method fields wrapper
    const add_ingredient_button      = $("#add_ingredient_button"); //Add ingredient ID
    const add_method_step_button      = $("#add_method_step_button"); //Add step to method ID
    let ingredient_count = 1; //initial ingredient count
    let method_step_count = 1; //initial method step count
	
	$(add_ingredient_button).click(function(e){ //on add ingredient button click
		e.preventDefault();
		if(ingredient_count < max_fields){ //max input box allowed
			ingredient_count++; //ingredient increment
			$(ingredient_wrapper).append('<div><i class="material-icons prefix">edit</i><input type="text" name="ingredients" class="validate"/><a href="#" class="btn-small btn-colour remove_field">Remove</a></div>'); //add ingredient box
		}
	});
	
	$(ingredient_wrapper).on("click",".remove_field", function(e){ //user click on remove ingredient
		e.preventDefault(); $(this).parent('div').remove(); ingredient_count--;
    })
    
    $(add_method_step_button).click(function(e){ //on add method step button click
		e.preventDefault();
		if(method_step_count < max_fields){ //max method step box allowed
			method_step_count++; //method step box increment
			$(method_fields_wrapper).append('<div><i class="material-icons prefix">short_text</i><input type="text" name="method" class="validate"/><a href="#" class="btn-small btn-colour remove_field">Remove</a></div>'); //add method step box
		}
	});
	
	$(method_fields_wrapper).on("click",".remove_field", function(e){ //user click on remove method step
		e.preventDefault(); $(this).parent('div').remove(); method_step_count--;
    })
});