let guess = parseInt(prompt("texminizini yazin"))
let i, j;


for (i = 1; i <= guess; i++) {
    for (j = 1; j <= i; j++) {
        document.write('* ');
    }
    document.write('<br/>');
}