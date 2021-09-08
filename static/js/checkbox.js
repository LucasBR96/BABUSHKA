$( ".pais_opt" ).click( function(){

    let foo  = x => true;
    let cul = $( this ).val()
    if ( cul != "Todos" ){
        foo = x => ( x == cul )
    };

    $( function(){
        $(".card").each( function(){
            $(".cul").ready( function(){
            let cul_nome = $( this ).text();
            console.log( cul_nome );})
        })
    })
})