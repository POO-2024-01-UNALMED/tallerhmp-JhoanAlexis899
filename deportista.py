class Deportista:

  def __init__(self, deporte:str, anosPracticando:int):
    self._deporte = deporte
    self._añosPracticando = anosPracticando

  def getDeporte(self):
    return self._deporte

  def setDeporte(self, deporte):
    self._deporte = deporte

  def getAñosPracticando(self):
    return self._añosPracticando
  
  def setAñosPracticando(self, anosPracticando):
    self._añosPracticando = anosPracticando
