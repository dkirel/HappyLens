$(document).ready(function(){

    /* Masonry JS */

    var leftRightMargin = 0.1
    var imagesPerRow = 3;
    var paddingBetweenImages = 0.01
    var columnWidth = Math.round($('.grid').innerWidth()/imagesPerRow);
    var deckIsInitialized = false;

    var $grid = $('.grid').masonry({
        columnWidth: columnWidth,
        isFitWidth: true
    });

    $('.grid-item').width(columnWidth - 0.01*$('body').width());

    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function() {
        $grid.masonry('layout');
    });


    /* Deck.js JS */

    //Activate and/or show deck
    $(".grid-item").click(function() {

        if (deckIsInitialized == false) {
            $.deck('.slide');
            deckIsInitialized = true;
        }

        jQuery.fx.off = true;
        $.deck('go', $(this).attr('id'));
        $('#toggle-visibility').show();
        jQuery.fx.off = false;

    });

    //Hide deck
    $(".exit-deck").click(function() {
        $('#toggle-visibility').hide();
    });


    console.log('Project.js file was successfully loaded!');

});