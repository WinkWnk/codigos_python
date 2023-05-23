from funcionario import Funcionario 

f1 = Funcionario("Rubim Barriquelo","Programador Senior")

print(f"Seu nome é , {f1.getNome()}")
f1.setNome("Marcos")
print(f"Seu nome é , {f1.getNome()}")

print(f"seu nome é {f1.cargo}")

f1.cargo = "Gerente"

print(f"Seu cargo é {f1.cargo}")