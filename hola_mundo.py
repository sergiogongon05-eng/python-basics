"""
Mi primer script Python
Autor: Sergio González
Fecha: 16 Feb 2026
Objetivo: Data Engineer 2029
"""

def mostrar_roadmap():
    """Muestra mi roadmap a Data Engineer."""
    print("=" * 60)
    print("🎖️  SERGIO GONZÁLEZ - ROADMAP DATA ENGINEER")
    print("=" * 60)
    
    perfil = {
        "edad": 30,
        "background": "Militar del Ejército del Aire",
        "formacion_actual": "FP superior administración y finanzas + FP DAW",
        "objetivo_2029": "Data Engineer",
        "ingles": "B2-C1"
    }
    
    print("\n👤 PERFIL:")
    for key, value in perfil.items():
        print(f"   {key}: {value}")
    
    certs_objetivo = [
        ("2026", "PCEP - Python Entry-Level", "€50"),
        ("2027", "AWS Solutions Architect Associate", "€150"),
        ("2028", "Google Cloud Professional Data Engineer", "€200"),
        ("2028", "Databricks Certified Data Engineer", "€200")
    ]
    
    print("\n📜 CERTIFICACIONES ROADMAP:")
    for año, cert, precio in certs_objetivo:
        print(f"   [{año}] {cert} ({precio})")
    
    tech_stack_2029 = ["Python", "SQL", "Git", "AWS", "Spark", "Airflow", "Docker"]
    
    print("\n🛠️  TECH STACK OBJETIVO:")
    print(f"   {', '.join(tech_stack_2029)}")
    
    print("\n✅ Primer script Python completado!")
    print("🚀 Próximo paso: Cisco Python Essentials 1\n")

if __name__ == "__main__":
    mostrar_roadmap()