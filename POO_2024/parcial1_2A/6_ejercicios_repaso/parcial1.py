while True:
    nombre = input("Nombre del paciente: ")
    tipo_sangre = input("Tipo de sangre: ")

    sistolica_total = 0
    diastolica_total = 0
    for i in range(3):
        sistolica = int(input(f"Medición parcial {i + 1} - Sistólica: "))
        diastolica = int(input(f"Medición parcial {i + 1} - Diastólica: "))
        sistolica_total += sistolica
        diastolica_total += diastolica

    promedio_sistolica = sistolica_total / 3
    promedio_diastolica = diastolica_total / 3

    sistolica_final = int(input("Medición final - Sistólica: "))
    diastolica_final = int(input("Medición final - Diastólica: "))

    sistolica_promedio_final = (promedio_sistolica + sistolica_final) / 2
    diastolica_promedio_final = (promedio_diastolica + diastolica_final) / 2

    print(f"\nPaciente: {nombre}")
    print(f"Tipo de sangre: {tipo_sangre}")
    print(f"Promedio de las presiones parciales: Sistólica = {promedio_sistolica:.2f}, Diastólica = {promedio_diastolica:.2f}")
    print(f"Presión arterial final: Sistólica = {sistolica_promedio_final:.2f}, Diastólica = {diastolica_promedio_final:.2f}")
    
    if sistolica_promedio_final <=120 and diastolica_promedio_final <= 80:
        print("El paciente presenta presión normal.")
    else:
        print("El paciente NO presenta presión normal, favor de ir con un especialista")