# ==========================================
# 📄 SIMULADOR DE DECLARAÇÃO DE IMPOSTO
# 🇧🇷 Receita Federal (Simulação Educacional)
# Autor: Vinícius Knabben
# ==========================================

def calcular_imposto(renda_anual):
    """
    Cálculo simplificado baseado em faixas fictícias
    Apenas para fins educacionais
    """
    
    imposto = 0
    
    if renda_anual <= 22847.76:
        imposto = 0
    elif renda_anual <= 33919.80:
        imposto = renda_anual * 0.075
    elif renda_anual <= 45012.60:
        imposto = renda_anual * 0.15
    elif renda_anual <= 55976.16:
        imposto = renda_anual * 0.225
    else:
        imposto = renda_anual * 0.275
    
    return imposto


def main():
    
    print("========================================")
    print("   📄 DECLARAÇÃO DE IMPOSTO DE RENDA")
    print("   (Simulador Educacional)")
    print("========================================")
    
    try:
        nome = input("Nome completo: ")
        cpf = input("CPF (somente números): ")
        renda = float(input("Renda anual (R$): "))
        dependentes = int(input("Número de dependentes: "))
        gastos_saude = float(input("Gastos com saúde (R$): "))
        gastos_educacao = float(input("Gastos com educação (R$): "))
        
        # Deduções simplificadas
        deducao_dependentes = dependentes * 2275.08
        total_deducoes = deducao_dependentes + gastos_saude + gastos_educacao
        
        base_calculo = renda - total_deducoes
        
        if base_calculo < 0:
            base_calculo = 0
        
        imposto_devido = calcular_imposto(base_calculo)
        
        # Relatório final
        print("\n========================================")
        print("            📊 RESUMO DA DECLARAÇÃO")
        print("========================================")
        print(f"Contribuinte: {nome}")
        print(f"CPF: {cpf}")
        print(f"Renda Anual: R$ {renda:,.2f}")
        print(f"Total de Deduções: R$ {total_deducoes:,.2f}")
        print(f"Base de Cálculo: R$ {base_calculo:,.2f}")
        print(f"Imposto Devido: R$ {imposto_devido:,.2f}")
        
        if imposto_devido == 0:
            print("\n✅ Isento de imposto.")
        else:
            print("\n💰 Imposto a pagar.")
        
        print("========================================")
    
    except ValueError:
        print("⚠ Erro: Digite valores válidos.")

        
if __name__ == "__main__":
    main()