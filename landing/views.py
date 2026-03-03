# landing/views.py
from django.shortcuts import render

def landing_view(request):
    """
    Renderiza la landing page Neo Simetry con secciones temáticas.
    Contexto expandido para tecnología, turismo y música.
    """
    context = {
        'page_title': 'NEO SIMETRY',
        'version': '1.0.1',
        
        # Sección Hero
        'hero': {
            'subtitle': 'Arquitectura Digital para Experiencias Únicas',
            'cta_text': 'EXPLORAR SISTEMA',
            'cta_link': '#servicios'
        },
        
        # Sección Tecnología
        'tech': {
            'title': 'TECNOLOGÍA',
            'description': 'Desarrollo de soluciones digitales con [PYTHON], [ANGULAR] y [LAYERCSS]. Código limpio, escalable y verificable.',
            'items': [
                {'icon': '⚡', 'title': 'Web Apps', 'desc': 'Django + Angular SPA'},
                {'icon': '🔐', 'title': 'Seguridad', 'desc': 'Criptografía y auditoría'},
                {'icon': '🎨', 'title': 'LayerCSS', 'desc': 'Estilos compilados desde .lyc'}
            ]
        },
        
        # Sección Turismo
        'tourism': {
            'title': 'TURISMO',
            'description': 'Rutas digitales hacia destinos físicos. Experiencias inmersivas con tecnología de vanguardia.',
            'items': [
                {'icon': '🗺️', 'title': 'Rutas', 'desc': 'Mapas interactivos y guías'},
                {'icon': '🏨', 'title': 'Alojamiento', 'desc': 'Reservas integradas'},
                {'icon': '🌿', 'title': 'Naturaleza', 'desc': 'Conexión con entornos reales'}
            ]
        },
        
        # Sección Música
        'music': {
            'title': 'MÚSICA',
            'description': 'Fusión de sonidos tradicionales colombianos con electrónica. Producción amateur con alma profesional.',
            'items': [
                {'icon': '🎧', 'title': 'Producción', 'desc': 'Trance + Folclor Zenú'},
                {'icon': '🎛️', 'title': 'Live Sets', 'desc': 'Integración con TikTok/Streaming'},
                {'icon': '🔊', 'title': 'Audio Tech', 'desc': 'Procesamiento en Lubuntu 4GB RAM'}
            ]
        },
        
        # Contacto
        'contact': {
            'title': 'CONECTAR',
            'email': 'contacto@neosimetry.dev',
            'location': 'Remoto / Colombia / Filipinas'
        }
    }
    return render(request, 'landing/index.html', context)