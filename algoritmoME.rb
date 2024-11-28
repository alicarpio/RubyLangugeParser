# Definición de una función
def calcular_promedio(numeros)
  suma = 0
  promedio = suma / numeros.length
  return promedio
end

# Declaración de un arreglo
numeros = [10, 20, 30, 40, 50]

# Uso de la función
promedio = calcular_promedio(numeros)
puts "El promedio es: #{promedio}"

# Declaración de un hash
persona = { nombre: "Juan", edad: 30, profesion: "Ingeniero" }
puts "Información de la persona:"
puts "Nombre: #{persona[:nombre]}"
puts "Edad: #{persona[:edad]}"
puts "Profesión: #{persona[:profesion]}"

until index < 0
  puts "Número invertido: #{numeros[index]}"
  index = index - 1
end
