"""
    Clase Utilizada para la el cargue de los datos de los diferentes archivos de excel
"""

import pandas as pd


class CargueDatos:

    def __init__(self) -> None:
        pass

    # Cargar datos en el dataFrame
    @staticmethod
    def CargarDatosCategorias():
        return pd.read_excel('datasets\CategorizacionMunicipio.xlsx', sheet_name="Categoria")

    # Cargar datos en el dataFrame
    @staticmethod
    def CargarDatosTipos():
        return pd.read_excel('datasets\Distancias.xlsx', sheet_name="Distancia")


    # Cargar datos en el dataFrame Sin procesar Salud (Sin organizar)
    @staticmethod
    def CargarDatosExpertosSaludOrigen():
        return pd.read_excel('datasets\SaludSinProcesar.xlsx', sheet_name="Salud")

    @staticmethod
    def CargarDatosExpertosSaludDestino():
        """
        Cargar datos en el dataFrame Destino Salud (organizados)
        :return:
        """
        return pd.read_excel('datasets/Salud/SaludProcesado.xlsx', index_col=None)


    @staticmethod
    def CargarDatosExpertosBienestarMaterialDestino():
        """
        Cargar datos en el dataFrame Destino  Bienestar material (organizados)
        """
        return pd.read_excel('datasets/BienestarMaterial/BienestarProcesado.xlsx', index_col=None)

    # Cargar datos en el dataFrame Origen  (Sin organizar)
    @staticmethod
    def CargarDatosUniversidadOrigen():
        return pd.read_excel(r"datasets\Universidad.xlsx", sheet_name="Otras Dimensiones")


    # Cargar datos en el dataFrame Destino  (organizados)
    @staticmethod
    def CargarDatosUniversidadDestino():
        return pd.read_excel(r"datasets\UniversidadOrganizados.xlsx", sheet_name="Salud_dataset")

