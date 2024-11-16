# Definición de un método de evaluación
def evaluar_numero(n)
  if n > 10
    return "Mayor que 10"
  elsif n == 10
    return "Es igual a 10"
  else
    return "Menor que 10"
  end
end

# Declaración de un hash
persona = {
  "nombre" => "Juan",
  "edad" => 25,
  :pais => "México",
  :activo => true
}

# Usamos el método y almacenamos el resultado
resultado = evaluar_numero(12)  # Evaluando si el número es mayor que 10

# Iteración sobre el hash
persona.each do |clave, valor|
  if clave.is_a?(String)
    puts "Clave (String): #{clave} => Valor: #{valor}"
  else
    puts "Clave (Symbol): #{clave} => Valor: #{valor}"
  end
end

# Llamada a método de comparación
puts resultado  # Imprime "Mayor que 10"

# Uso de operador lógico
edad_valida = persona["edad"] >= 18 && persona["activo"] == true  # Verificando que la persona sea mayor de edad y activa

puts "Edad válida y activo: #{edad_valida}"