function ajax_get_update(){
   $.get(url, function(results){
      var table = $("table", results);
      var span = $("span.step-links", results);

      $('#ajax_table_result').html(table);
      $('.step-links').html(span);
    }, "html");
}

$( document ).ready( function() {
    $( '.step-links #prev' ).click( function(e) {
        e.preventDefault();
        url = ($( '.step-links #prev' )[0].href);
        ajax_get_update();
    });
    $( '.step-links #next' ).click( function(e) {
        e.preventDefault();
        url = ($( '.step-links #next' )[0].href);
        ajax_get_update();

    });
});

$( document ).ajaxStop( function() {
    $( '.step-links #prev' ).click( function(e) {
        e.preventDefault();
        url = ($( '.step-links #prev' )[0].href);
        ajax_get_update();
    });
    $( '.step-links #next' ).click( function(e) {
        e.preventDefault();
        url = ($( '.step-links #next' )[0].href);
        ajax_get_update();
    });
});
