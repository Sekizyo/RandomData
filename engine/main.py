from engine.dateTimeGen import dateTimeGenerator

def run():
    gen = dateTimeGenerator()
    print(gen.get("isoDateTime"))