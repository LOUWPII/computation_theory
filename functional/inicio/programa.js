//Imprimir elementos uno por uno
posts.forEach(post => console.log(post));

//Se imprimen solo los títulos
const titulos = posts.map(post => post.title);
titulos.forEach(titulo => console.log(titulo));

//Se imprimen solo los títulos de los posts cuyo userId es 1
posts.
    filter(post => post.userId === 1)
    .map(post => post.title)
    .forEach(titulo => console.log(titulo));

//Imprimir el promedio de latitud de los usuarios
console.log(users.map(user => parseFloat(user.address.geo.lat)).reduce((total, numero) => total + numero, 0)) / users.lenght;