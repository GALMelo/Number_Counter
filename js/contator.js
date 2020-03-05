var entrada = window.document.getElementsByName("entrada");

var list_numbers = window.document.getElementsByClassName("list_numbers");

var list_quant = window.document.getElementsByClassName("list_quant");

var list_entradas = [];

var map_number = new Map();

function add() {
    let num = new String(entrada[0].value);

        console.log(num.length);

        for ( let i = 0; i < num.length; i++) {
            if (num.charAt(i) == new Number(num.charAt(i)) && num.charAt(i) !== " " ) {
                list_entradas.push(num.charAt(i));
            }
        }

        console.log(list_entradas);

        list_entradas.forEach(num => {
            if ( num > 0) {
                if ( map_number[num] === undefined ) {
                    map_number[num] = 1;
                } else {
                    map_number[num] += 1;
                }
            }
        })

        list_entradas.forEach(num => {
            
            updateList(num);
            updateQuant(num);
        })       
}

function updateList(num) {

    let p = window.document.createElement('p');

    p.textContent = num;

    list_numbers[0].appendChild(p);

}

function updateQuant(num) {

    let x = window.document.getElementById(num);
    
    if ( x == null) {
        let p = window.document.createElement('p');
        p.id = num;
        p.textContent = `O número ${num} se repete ${map_number[num]}`;
        list_quant[0].appendChild(p);
    } else {
        x.textContent = `O número ${num} se repete ${map_number[num]}`;
    }

    

    

}