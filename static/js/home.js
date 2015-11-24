$(document).ready(function(){

	/* Image resizing */
    $('image').each(function(i, img) {
        if (img.height()/img.width() > $(document).height()/$(document).width())
            img.addClass("fill-width");
        else
            img.addClass("fill-height");
    });


    /*

	//Aisle menu dropdown
	$("#main_aisle").mouseenter(function(){
		$("#aisle_nav").show();
		$("#recipe_nav").hide();
		$("#diet_nav").hide();
		$("#specials_nav").hide();
	});

    */

});