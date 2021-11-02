import csv
from numpy import printoptions
import requests
import pandas as pd
import os


class Artista:
    
    def buscar_informacoes_artista(self, artista):
        context = {}
        response = requests.get(f'https://theaudiodb.com/api/v1/json/1/search.php?s={artista}')
        response = response.json()
        if response['artists']:
            nome_artista = response['artists'][0]['strArtist']
            biografia_artista = response['artists'][0]['strBiographyPT']
            thumb_artista = response['artists'][0]['strArtistThumb']
            estilo_musical = response['artists'][0]['strGenre']
            ano_nascimento = response['artists'][0]['intBornYear']
            ano_falecimento = response['artists'][0]['intDiedYear']
            artista_logo = response['artists'][0]['strArtistLogo']
            thumb_wide_artista = response['artists'][0]['strArtistWideThumb']
            fanart_primary_artista = response['artists'][0]['strArtistFanart']
            fanart_second_artista = response['artists'][0]['strArtistFanart2']
            fanart_try_artista = response['artists'][0]['strArtistFanart3']
            nacionalidade_artista = response['artists'][0]['strCountry']
            site_artista = response['artists'][0]['strWebsite']
            facebook_artista = response['artists'][0]['strFacebook']
            twitter_artista = response['artists'][0]['strTwitter']
            if not biografia_artista:
                biografia_artista = response['artists'][0]['strBiographyEN']
            if not ano_falecimento:
                ano_falecimento = '2021'
            print(nome_artista)
            context = {
                'situacao': 'disp',
                'nome': nome_artista,
                'biografia': biografia_artista,
                'thumb': thumb_artista,
                'estilo': estilo_musical,
                'nascimento': ano_nascimento,
                'falecimento': ano_falecimento,
                'logo': artista_logo,
                'nacionalidade': nacionalidade_artista,
                'site': site_artista,
                'facebook': facebook_artista,
                'twitter': twitter_artista,
                'imagens': {
                    'thumb_wide': thumb_wide_artista,
                    'farnart_primary': fanart_primary_artista,
                    'farnart_second' : fanart_second_artista,
                    'farnart_try' : fanart_try_artista
                }
            }
        else:
            context = {
                'situacao': 'indi'
            }    
        return context
        