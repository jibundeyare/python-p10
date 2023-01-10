// pour exécuter le script: nodejs for-loop.js

// boucle de type for == pour
// i++ est équivalent à i += 1
for (let i = 0; i < 10; i++) {
    console.log(`i = ${i}`)
}

let fruits = ['abricot', 'baie', 'cerise']

fruits[10] = 'datte';

console.log(fruits.length);

// boucle for classique
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// boucle foreach par clé
for (let key in fruits) {
    console.log(`${key} : ${fruits[key]}`);
}

// bouclde foreach par valeur
for (let fruit of fruits) {
    console.log(fruit);
}

let legumes = new Array('artichaut', 'betterave', 'céléri');
legumes.push('carotte');

// méthode forEach qui attend une fonction de call back
legumes.forEach(function (value, index, list) {
    console.log(`${index} : ${value}`);

    if (value == 'artichaut') {
        list[index] = 'tomate';
    }
});

console.log(legumes);

legumes.forEach((value, index, list) => {
    console.log(`${index} : ${value}`);
});

let forEachLog = (value, index, list) => {
    console.log(`${index}: ${value}`);
};

legumes.forEach(forEachLog);

// Maintenant on peut réutiliser la fonction anonymes forEachLog avec d'autres boucle forEach()
// fruits.forEach(forEachLog);
// pattiseries.forEach(forEachLog);
