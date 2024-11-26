# Clase Estudiante que contiene información básica de cada estudiante
class Estudiante
  # Constructor para inicializar los atributos de la clase
  def initialize(nombre, edad, promedio, materias)
    @nombre = nombre               # String
    @edad = edad                   # Integer
    @promedio = promedio           # Float
    @materias = materias           # Array de strings
  end

  # Método para obtener información del estudiante
  def mostrar_informacion
    puts "Nombre: #{@nombre}"
    puts "Edad: #{@edad}"
    puts "Promedio: #{@promedio}"
  end
end

# Hash para almacenar estudiantes por su ID (como clave)
estudiantes = {}

# Método para calcular el promedio general de todos los estudiantes
def calcular_promedio_general(estudiantes)
  total = 0

  promedio_general = total / estudiantes.size
  puts "Promedio general de la clase: #{promedio_general}"
end

# Llamada al método para calcular el promedio general
calcular_promedio_general(estudiantes)
