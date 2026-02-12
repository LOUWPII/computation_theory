class Estado:
    def __init__(self, nombre_estado, es_final = False):
        #nmbres de estados para claridad
        self.nombre_estado = nombre_estado
        #para saber si el estado es final y saber si se aceptará o no
        self.es_final = es_final
        self.transiciones = {}

    def agregar_transicion(self, simbolo, estado_destino):
        """
        :param simbolo: este vendría siendo un elemento del alfabeto
        :param estado_destino: el estado al que va la arista
        :return: no retorna nada, solo agrega la conexión al estado
        """
        self.transiciones[simbolo] = estado_destino

class Automata:
    def __init__(self):
        #A continuacion se instanciaran todos los estados
        self.q1 = Estado("inicio")
        self.q2 = Estado("usuario")
        self.q3 = Estado("arroba")
        self.q4 = Estado("dominio")
        self.q5 = Estado("punto")
        self.q6 = Estado("extension", es_final = True)

        #Aqui se agregaran las transiciones entre los estados
        #arista que va de inicio - usuario, representa que el usuario escribe su usuario
        self.q1.agregar_transicion("L", self.q2)

        #arista que es un bucle, ya que en el usuario se escribe letra tras letra, se vuelve al mismo estado
        self.q2.agregar_transicion("L", self.q2)

        #arista que permite que al escribir un punto se permanezca en el mismo estado, permitir que el usuario tenga puntos
        self.q2.agregar_transicion(".", self.q2)

        #arista que representa cuando se escribe una arroba, se pasa del estado usuario al estado arroba
        self.q2.agregar_transicion("@", self.q3)

        #arista ue representa cuando se escribe una letra y se pasa al estado del dominio
        self.q3.agregar_transicion("L", self.q4)

        #arista que representa un bucle, ya que se escribe letra tras letra y se vuelve al mismo estado
        self.q4.agregar_transicion("L", self.q4)

        #arista que representa cuando se pasa al estado del punto
        self.q4.agregar_transicion(".", self.q5)

        #arista que representa cuando se pasa a escribir la extension
        self.q5.agregar_transicion("L", self.q6)

        #arista que representa que al escribir una letra mas se vuelve al mismo estado
        self.q6.agregar_transicion("L", self.q6)

        #arisa qyue permite que al escribir un punto en la extension no haya ningun problema y permanezca en el msimo estado
        self.q6.agregar_transicion(".", self.q6)

        self.estado_actual = self.q1

        self.alfabeto = "_,¿?+-%&/()=!¡*"

    def validar(self, correo):
        self.estado_actual = self.q1

        for caracter in correo:
            tipo = "L" if caracter.isalnum() or caracter in self.alfabeto else caracter

            if tipo in self.estado_actual.transiciones:
                self.estado_actual = self.estado_actual.transiciones[tipo]
            else:
                self.estado_actual = Estado("error", es_final=False)
                break

        return self.estado_actual.es_final

automata = Automata()
correo = "pipe_gomezl2006@javeriana.edu.co"
if automata.validar(correo):
    print("El correo es valido")
else:
    print("El correo no es valido")






