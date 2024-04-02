"""
    Clase Utilizada para el manejo de la parametrizacion del formulario , y las dimensiones
    Fecha:18/01/2024
"""
import pandas as pd
class Parametrizacion:
    
    #Declaracion de variables para el manejo del calculo final.
    MUNICIPIO_URBANO = 0.50
    MUNICIPIO_RURAL= 0.30
    MUNICIPIO_RURAL_DISPERSO = 0.20
    MUNICIPIO_CATEGORIA1 = 0.30
    MUNICIPIO_CATEGORIA2 = 0.25
    MUNICIPIO_CATEGORIA3 = 0.20
    MUNICIPIO_CATEGORIA4 = 0.10
    MUNICIPIO_CATEGORIA5 = 0.8
    MUNICIPIO_CATEGORIA6 = 0.4
    MUNICIPIO_CATEGORIA7 = 0.3

    PORCENTAJE_EXPERTOS=0.50
    PORCENTAJE_UNIVERSIDAD=0.30
    PORCENTAJE_CATEGORIA_MUNICIPIO=0.10
    PORCENTAJE_TIPO_MUNICIPIO=0.10

    DIMENSION_SALUD="Salud"
    DIMENSION_SALUD="Bienestar Material"
    DIMENSION_SALUD="Cuidado"
    DIMENSION_SALUD="Binestar Materno"
    DIMENSION_SALUD="Seguridad"
    
    
    def __init__(self) -> None:
        pass
    
    #valores para el tipo de municipio
    def DatosTipoMunicipio(self):
        dTipoMuncipio=pd.DataFrame()
        public_item= [1, 2, 3] 
        public_tipo= [self.MUNICIPIO_URBANO, self.MUNICIPIO_RURAL, self.MUNICIPIO_RURAL_DISPERSO] 
        dTipoMuncipio["TipoMunicipio"]=public_item
        dTipoMuncipio["Valor"]=public_tipo
        return dTipoMuncipio
    
    #valores para el tipo de Municipio
    def DatosCategoriaMunicipio(self):
        dCategoriaMuncipio=pd.DataFrame()
        public_item= [1, 2, 3,4,5,6,7] 
        public_categoria= [self.MUNICIPIO_CATEGORIA1, self.MUNICIPIO_CATEGORIA2, self.MUNICIPIO_CATEGORIA3,
                           self.MUNICIPIO_CATEGORIA4,self.MUNICIPIO_CATEGORIA5,self.MUNICIPIO_CATEGORIA6,
                           self.MUNICIPIO_CATEGORIA7] 
        dCategoriaMuncipio["TipoMunicipio"]=public_item
        dCategoriaMuncipio["Valor"]=public_categoria
        return dCategoriaMuncipio

    #Valor Experto
    @classmethod
    def DatosPorcentajes(cls):
        return cls.PORCENTAJE_EXPERTOS
    
    #valor Universidad
    @classmethod
    def DatosPorcentajes(cls):
        return cls.PORCENTAJE_UNIVERSIDAD
    
    #valor Categoria
    @classmethod
    def DatosPorcentajes(cls):
        return cls.PORCENTAJE_CATEGORIA_MUNICIPIO
    
    #valor Tipo
    @classmethod
    def DatosPorcentajes(cls):
        return cls.PORCENTAJE_TIPO_MUNICIPIO
    
    #valor Salud
    @classmethod
    def DatosPorcentajes(cls):
        return cls.PORCENTAJE_TIPO_MUNICIPIO
    
   