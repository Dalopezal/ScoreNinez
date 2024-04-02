"""
    Clase Utilizada para el manejo de la categoria de los municipios.
    Daniel Alejandro Lopez
    Fecha:18/01/2024
"""

import pandas as pd
import numpy as np

class CargueDatos:
    
    def __init__(self) -> None:
     pass
 
    #Cargar datos en el dataFrame
    def CargarDatosCategorias(self):
        df = pd.DataFrame()
        df=pd.read_excel('datasets\CategorizacionMunicipio.xlsx',sheet_name="Categoria")
        return df
    
    #Cargar datos en el dataFrame
    def CargarDatosTipos(self):
        df = pd.DataFrame()
        df=pd.read_excel('datasets\Distancias.xlsx',sheet_name="Distancia")
        return df
    
    #Cargar datos en el dataFrame Sin procesar Salud (Sin organizar)
    def CargarDatosExpertosSaludOrigen(self):
        df = pd.DataFrame()
        df=pd.read_excel('datasets\SaludSinProcesar.xlsx',sheet_name="Salud")
        return df
    
    #Cargar datos en el dataFrame Procesado salud  (organizados)
    def CargarDatosExpertosSaludDestino(self):
        df = pd.DataFrame()
        df=pd.read_excel('datasets\SaludProcesado.xlsx',index_col=None)
        return df
    
    #Cargar datos en el dataFrame Sin procesar Bienestar material (Sin organizar)
    def CargarDatosExpertosBienestarOrigen(self):
        df = pd.DataFrame()
        df=pd.read_excel('datasets\BienestarSinProcesado.xlsx')
        return df
    
    #Cargar datos en el dataFrame Destino  Bienstar material (organizados)
    def CargarDatosExpertosBienestarDestino(self):
        df = pd.DataFrame()
        df=pd.read_excel('datasets\BienestarProcesado.xlsx',index_col=None)
        return df
    
    
     #Cargar datos en el dataFrame Origen  (Sin organizar)
    def CargarDatosUniversidadOrigen(self):
        df = pd.DataFrame()
        df=pd.read_excel(r"datasets\Universidad.xlsx",sheet_name="Otras Dimensiones")
        return df
    
        #Cargar datos en el dataFrame Destino  (organizados)
    def CargarDatosUniversidadDestino(self):
        df = pd.DataFrame()
        df=pd.read_excel(r"datasets\UniversidadOrganizados.xlsx",sheet_name="Salud_dataset")
        return df