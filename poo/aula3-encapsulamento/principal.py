from conta import Conta
minhaConta = Conta(123, "Rubim", 20000, 300)

#minhaConta.relatorio()
minhaConta.saldo = 80500
minhaConta.exibirSaldo()

print("Seu limite é ",minhaConta.getLimite())
minhaConta.setLimite(1400)
print("Seu limite é ",minhaConta.getLimite())