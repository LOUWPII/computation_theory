//EJERCICIO 1
const mayores_edad = (nombre_uni, edad) => {
    const profesores_filtro = universityData.find(u => u.university_name === nombre_uni).schools.flatMap(s => s.professors.filter(p => p.age > edad))
    console.log(profesores_filtro)
}
mayores_edad('Global Tech University', 40)

//EJERCICIO 2
const promedio_edad = (nombre_uni, nombre_facultad) => {
    const profes = universityData.find(u => u.university_name === nombre_uni).schools.find(s => s.school_name === nombre_facultad).professors;
    const promedio = profes.reduce((acumulador, p) => acumulador + p.age, 0) / profes.length;
    console.log(promedio)
}
promedio_edad('Global Tech University', 'School of Computer Science')

//EJERCICIO 3
const cargo_existe = (nombre_uni, nombre_facultad, cargo) => {
    const cargo_existe = universityData.find(u => u.university_name === nombre_uni).schools.find(s => s.school_name === nombre_facultad).professors.some(p => p.position === cargo);
    console.log(cargo_existe)
}

mayores_edad('Global Tech University', 30)
//La salida deberia ser 3
promedio_edad('Global Tech University', 'School of Engineering')
//La salida debería ser 45.66
cargo_existe('Global Tech University', 'School of Computer Science', 'Full Professor')
//Deberia ser true

