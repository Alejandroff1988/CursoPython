
# Obtener la fecha actual:

from datetime import datetime
hoy = datetime.now()
print(hoy)

# Obtener la fecha de mañana:

from datetime import timedelta
mañana = datetime.now() + timedelta(days=1)
print(mañana)


