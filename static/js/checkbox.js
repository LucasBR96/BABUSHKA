/*
    Esse script gerencia o checkbox que filtra os cards, por país, de receitas e restaurantes.
    Esse filtro tem dois modos: "Todos" e "Alguns".

    1 - No modo "Todos" o checkbox homônimo é marcado, e não há filtragem de restaurantes ou receitas
        baseado em nacionalidade. Um exemplo.

        [ X ] Todos
        [   ] Hungria
        [   ] Sérvia
        [   ] Croácia
    
    2 - No outro modo, apenas os países com checkbox marcado tem suas receitas e restaurantes expostos
        pelos seus cards. Usando a lista acima, tem-se 3 exemplos

        [   ] Todos                [   ] Todos                [   ] Todos
        [ X ] Hungria              [ X ] Hungria              [   ] Hungria 
        [   ] Sérvia               [ X ] Sérvia               [   ] Sérvia
        [ X ] Croácia              [   ] Croácia              [ X ] Croácia
*/

const TODOS  = 1;
const ALGUNS = 0;
var status = TODOS;

function setTodos(){

    
}

function setAlguns(){}
function updateModo( toogle ){

    if( toogle ){
        setTodos();
        return;
    }

    let par = document.getElementById( 'check-b' );
    let seq = [];
    for ( let u of par.children ){
        let m = u.firstElementChild;
        if ( m.id === "Todos"){
            continue;
        }

        seq.push( m.checked );
    }

    let lst1 = seq.reduce( ( x , y ) => x && y );
    let lst2 = !( seq.reduce( ( x , y ) => x || y ) );
    if( lst1 || lst2 ){
        setTodos();
        return;
    }
    setTodos();
}

// ------------------------------------------------------------------------
// Método para testes

function dummy(){

    let par = document.getElementById( 'check-b' );
    for ( let u of par.children ){
        let m = u.firstElementChild;
        let s = m.id + " " + String( m.checked );
        console.log( s );
    }
}