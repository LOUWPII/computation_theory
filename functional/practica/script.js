console.log("¡El archivo JS está conectado correctamente!");

const universidades = [
    {
        nombre: "U. Nacional",
        facultades: [
            {
                nombre: "Ingeniería",
                profesores: [
                    { nombre: "Jorge", edad: 52, cargo: "Full Professor", publicaciones: [5, 12, 8] },
                    { nombre: "Elena", edad: 29, cargo: "Assistant", publicaciones: [1, 2] }
                ]
            },
            {
                nombre: "Artes",
                profesores: [
                    { nombre: "Beatriz", edad: 41, cargo: "Associate", publicaciones: [10] }
                ]
            }
        ]
    },
    {
        nombre: "U. Distrital",
        facultades: [
            {
                nombre: "Ciencias",
                profesores: [
                    { nombre: "Ricardo", edad: 60, cargo: "Full Professor", publicaciones: [20, 15, 30] }
                ]
            }
        ]
    }
];

console.log("Datos cargados:", universidades);