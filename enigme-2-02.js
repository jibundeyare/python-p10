// # 2. Entiers consécutifs
// # 198, 199, 200, 201 et 202 sont des entiers consécutifs dont la somme est égale à 1000.
// # Trouvez d'autres entiers consécutifs dont la somme vaut 1000.

// # [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
// # [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
// # [198, 199, 200, 201, 202]

function sum(list) {
    let my_sum = 0;

    for (let key in list) {
        my_sum += list[key];
    }

    return my_sum;
}

let sumFunction = (accumulator, currentValue) => {
    return accumulator + currentValue
};

let somme = 0;
let nombres = [];

for (let i = 1; i < 500; i++) {
    nombres.push(i)
    somme = sum(nombres);
    // méthode alternative pour obtenir une somme de la liste
    // somme = nombres.reduce(sumFunction);

    while (somme > 1000) {
        nombres.shift();
        somme = sum(nombres);
        // méthode alternative pour obtenir une somme de la liste
        // somme = nombres.reduce(sumFunction);
    }

    if (somme == 1000) {
        console.log(nombres);
    }
}
