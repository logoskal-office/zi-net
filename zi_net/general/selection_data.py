from django.db import models

CountryList = {
    "JP": "Japan",
    "US": "United States",
    "DE": "Germany",
    "CN": "China",
    "IN": "India",
    "IT": "Italy",
    "MX": "Mexico",
    "KR": "South Korea",
    "BR": "Brazil",
    "FR": "France",
    "ES": "Spain",
    "CA": "Canada",
    "UK": "United Kingdom",
    "RU": "Russia",
    "TR": "Turkey",
    "NN": "Other"
}


VehicleBodyTypeList = {
    "SD": "Sedan",
    "SV": "SUV",
    "HB": "Hatchback",
    "CP": "Coupe",
    "CM": "Compact",
    "CV": "Convertible",
    "MV": "Minivan",
    "PU": "Pickup Truck",
    "SC": "Sports Car",
    "LC": "Luxury Car",
    "CN": "Construction Vehicle",
    "LM": "Limousine",
    "NN": "Other"
}


VehicleBodyColorList = {
    "BK": "Black",
    "WT": "White",
    "SV": "Silver",
    "RD": "Red",
    "BL": "Blue",
    "GY": "Gray",
    "BG": "Beige",
    "BN": "Brown",
    "BZ": "Bronze",
    "CA": "Caramel",
    "CH": "Charcoal",
    "CP": "Copper",
    "CY": "Cyan",
    "EM": "Emerald",
    "FC": "Fuchsia",
    "GD": "Gold",
    "GN": "Green",
    "IV": "Ivory",
    "LM": "Lime",
    "MT": "Mint",
    "NV": "Navy",
    "OG": "Orange",
    "PN": "Pink",
    "PU": "Purple",
    "TQ": "Turquoise",
    "YL": "Yellow",
    "NN": "Other"
}

VehicleCondition = {
    "S": "Brand New",
    "A": "Excellent",
    "B": "Good",
    "C": "Sub-Optimal",
    "D": "Bad",
    "F": "Non-Working",
    "NN": "Other"
}

VehicleFuelType = {
    "BN": "Benzene",
    "DS": "Diesel",
    "EL": "Electric",
    "HY": "Hybrid",
    "NN": "Other"
}
