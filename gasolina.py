pinicial = float(input())
linicial = float(input())
pfinal = float(input())
lfinal = float(input())

kml = (pfinal-pinicial) / (lfinal-linicial)
if kml < 0:
    kml *= -1

print(f'{kml:.1f}')
