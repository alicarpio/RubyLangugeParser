# Clase Estudiante que contiene información básica de cada estudiante
class Estudiante
  attr_accessor :nombre, :edad, :promedio, :materias

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
    puts "Materias: #{@materias.join(', ')}"
  end
end

# Hash para almacenar estudiantes por su ID (como clave)
estudiantes = {}

# Creación de dos estudiantes y almacenamiento en el hash
estudiantes[:est1] = Estudiante.new("Ana", 20, 8.5, ["Matemáticas", "Historia", "Ciencias"])
estudiantes[:est2] = Estudiante.new("Juan", 22, 9.0, ["Inglés", "Arte", "Física"])

# Método para calcular el promedio general de todos los estudiantes
def calcular_promedio_general(estudiantes)
  total = 0.0
  estudiantes.each do |key, estudiante|
    total += estudiante.promedio
  end
  promedio_general = total / estudiantes.size
  puts "Promedio general de la clase: #{promedio_general}"
end

# Muestra la información de cada estudiante
estudiantes.each do |id, estudiante|
  puts "ID del Estudiante: #{id}"
  estudiante.mostrar_informacion
  puts "-------------------------"
end

# Llamada al método para calcular el promedio general
calcular_promedio_general(estudiantes)
