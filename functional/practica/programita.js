/*Escribe una función que reciba una universidad y 
devuelva un arreglo con los nombres de todos sus 
profesores, sin importar la facultad.
*/

const profesores = universidades
    .find(u => u.nombre === "U. Nacional")
    .facultades
    .flatMap(f => f.profesores);
console.log(profesores);