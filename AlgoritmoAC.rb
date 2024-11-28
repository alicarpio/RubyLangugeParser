# Declaración de variables
x = 10
y = 20
result = 0

# Condicional
if x < y
  result = x + y
elsif x == y
  result = x * y
else
  result = x - y
end

# Impresión del resultado
puts "Resultado: #{result}"

# Bucle 'while'
counter = 0
while counter < 5
  puts "Contador: #{counter}"
  counter += 1
end

numeros = [1, 2, 3, 4, 5]

for numero in numeros do
  puts "Número: #{numero}"
end

