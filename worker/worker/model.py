def run_forecast():
    # Simulação inicial (depois conectamos API real)
    swell_direction = "SE"
    swell_size = 1.8
    wind = "W"

    if swell_direction in ["E", "SE"] and wind in ["W", "NW"]:
        return f"🔥 Condição clássica detectada! Swell {swell_direction} {swell_size}m com vento {wind}"
    
    return None