saldo_total = int(input())
valor_saque = int(input())

if valor_saque <= saldo_total:
    saldo = saldo_total - valor_saque
    print(f"Saque realizado com sucesso. Novo saldo: {saldo}")

else:
    print("Saldo insuficiente. Saque nao realizado!")