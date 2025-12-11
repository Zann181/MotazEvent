# core/email_utils.py (PLANTILLA MOCOA BEATS, FIX COLOR <strong> + FLYER EMBEBIDO)

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
import logging
import os
from email.mime.image import MIMEImage

logger = logging.getLogger(__name__)

def enviar_email_bienvenida(asistente):
    """Envía email de bienvenida con QR al asistente"""
    logger.info("[EMAIL OFF] No se envía correo de bienvenida en esta versión")
    return False
    try:
        # Datos básicos y fallbacks seguros
        primer_nombre = (asistente.nombre or "").split()[0] if getattr(asistente, "nombre", None) else "Invitado"
        correo = getattr(asistente, "correo", None)
        cc = getattr(asistente, "cc", "")
        categoria_nombre = getattr(getattr(asistente, "categoria", None), "nombre", "General")
        qr_field = getattr(asistente, "qr_image", None)
        qr_path = getattr(qr_field, "path", None) if qr_field else None

        # HTML tema oscuro + IndaJungle minimalista + <strong> hereda color + FLYER embebido
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="x-apple-disable-message-reformatting">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                /* Reset básico para consistencia en clientes de correo */
                body, p, h1, h2, h3, h4, h5, h6 {{ margin: 0; padding: 0; }}
                img {{ border: 0; outline: none; text-decoration: none; max-width: 100%; }}
                table {{ border-collapse: collapse; }}
                a {{ color: #00baff; text-decoration: none; }}

                body {{
                    background-color: #040404;
                    color: #dcdcdc;
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    line-height: 1.7;
                    margin: 0;
                    padding: 0;
                    -webkit-font-smoothing: antialiased;
                    -moz-osx-font-smoothing: grayscale;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background: #0b0b0c;
                    border-radius: 14px;
                    overflow: hidden;
                    border: 1px solid #181818;
                }}
                .header {{
                    text-align: center;
                    background: linear-gradient(135deg, #050505, #0d0f16);
                    padding: 48px 24px 32px 24px;
                    color: #f5f5f0;
                    border-bottom: 1px solid #181818;
                }}
                .header h1 {{
                    font-size: 2.1em;
                    letter-spacing: 1px;
                    color: #f5f5f5;
                    font-weight: 600;
                    margin: 0;
                }}
                .header .subhead {{
                    font-size: 1em;
                    letter-spacing: 4px;
                    text-transform: uppercase;
                    color: #7cf3d0;
                    margin-top: 10px;
                }}
                .header .eyebrow {{
                    text-transform: uppercase;
                    letter-spacing: 3px;
                    font-size: 0.78em;
                    color: #8a8a8a;
                    margin-bottom: 14px;
                }}
                .content {{
                    padding: 32px 28px 36px;
                    color: #c8c8c8;
                    font-size: 15px;
                }}
                h2 {{
                    color: #f1f1f1;
                    margin-top: 0;
                    font-size: 1.3em;
                    font-weight: 500;
                }}
                .event-info {{
                    margin: 28px 0;
                    background: #070708;
                    border: 1px solid #1a1a1a;
                    border-left: 3px solid #7cf3d0;
                    border-radius: 10px;
                    padding: 20px 24px;
                }}
                .event-info h3 {{
                    color: #7cf3d0;
                    margin: 0 0 8px 0;
                    font-size: 1.1em;
                    font-weight: 600;
                }}
                .qr-info {{
                    text-align: center;
                    margin: 28px 0 12px 0;
                    padding: 24px 20px;
                    border: 1px dashed #7cf3d0;
                    border-radius: 10px;
                    background: #060606;
                }}
                .footer {{
                    text-align: center;
                    font-size: 0.9em;
                    color: #7d7d7d;
                    padding: 25px;
                    border-top: 1px solid #1f1f22;
                }}
                /* FIX: que <strong> NO cambie el color (hereda del padre) */
                strong {{ color: inherit; font-weight: 700; }}
                .highlight {{ color: #7cf3d0; font-weight: 600; }}
                /* Aseguramos el color base de párrafos y listas dentro de content */
                .content p, .content li {{ color: #c8c8c8; }}
                .content .lede {{ font-size: 1.05em; color: #f4f4f4; margin-bottom: 18px; }}
                .content .accent {{ color: #7cf3d0; font-weight: 600; }}
                .flyer-wrapper {{ text-align:center; margin: 24px 0 10px 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <p class="eyebrow">Mocoa · La Rochela · 06 Dic</p>
                    <h1>Mocoa se viste de negro</h1>
                    <p class="subhead">𖠢ꚳꛎꛕⵅ▹𐤠ꚡⵦⵉ · IndaJungle </p>
                </div>
                <div class="content">
                    <h2>Hola {primer_nombre},</h2>

                    <p class="lede">Mocoa se viste de negro ! 𖠢ꚳꛎꛕⵅ▹𐤠ꚡⵦⵉ IndaJungle Edición Especial 🐈‍⬛presentando por primera vez directamente desde Roma🏺🇮🇹 a el corazón de la selva a <strong>@dinosabatiniofficial</strong> — el arquitecto futurista de la electrónica romana. Su instinto  tribal y su precisión minimalista tejen atmósferas elegantes y cinematográficas que despiertan los sentidos🫦🧠</p>

                    <p>El templo⛩ La Rochela será escenario de este viaje vanguardista: una experiencia única donde la elegancia italiana🇮🇹 se funde con la energía selvática del sur de Colombia🇨🇴🍃 Una noche para los oídos más finos el próximo sábado <strong>6 de Diciembre</strong> 🕯🕯</p>

                    <p class="accent">Lugar: La Rochela · Fecha: 6 de diciembre · Dresscode: Night in Black</p>

                    <!-- FLYER EMBEBIDO -->
                    <div class="flyer-wrapper">
                        <img src="cid:flyer_mocoabeats" alt="Flyer IndaJungle Edición Especial" style="border-radius:12px; max-width:100%; height:auto;" />
                    </div>

                    <div class="event-info">
                        <h3>Detalles del Evento</h3>
                        <p><strong>Evento:</strong> 𖠢ꚳꛎꛕⵅ▹𐤠ꚡⵦⵉ · IndaJungle · Edición Especial</p>
                        <p><strong>Invitado:</strong> Dino Sabatini LIVE</p>
                        <p><strong>Fecha:</strong> Sábado 6 de Diciembre</p>
                        <p><strong>Lugar:</strong> La Rochela, Mocoa · Putumayo</p>
                    </div>

                    <div class="qr-info">
                        <p><strong>Nombre:</strong> {asistente.nombre}</p>
                        <p><strong>Cédula:</strong> {cc}</p>
                        <p><strong>Categoría:</strong> {categoria_nombre}</p>
                        <p><strong>Precio: </strong> {asistente.consumos_disponibles}</p>
                        <p style="color:#7cf3d0;font-weight:bold;">📱 Tu código QR está adjunto a este correo</p>
                        <p><small>Preséntalo junto a tu cédula en la entrada del evento.</small></p>
                    </div>

                    <p>Nos vemos en el templo.<br>
                    <span class="highlight">Elegancia italiana + energía selvática · Night in Black</span></p>
                </div>
                <div class="footer">
                    <p>Equipo 𖠢ꚳꛎꛕⵅ▹𐤠ꚡⵦⵉ</p>
                    <p><small>Correo automático — conserva tu QR hasta el día del evento.</small></p>
                </div>
            </div>
        </body>
        </html>
        """

        subject = f"🖤 𖠢ꚳꛎꛕⵅ▹𐤠ꚡⵦⵉ · IndaJungle · Tu acceso para La Rochela, {primer_nombre}"

        if not correo:
            raise ValueError("El asistente no tiene correo definido.")

        # Usamos EmailMultiAlternatives para mejor control de MIME multipart/related
        text_content = f"Hola {primer_nombre}, tu entrada para 𖠢ꚳꛎꛕⵅ▹𐤠ꚡⵦⵉ ·IndaJungle · La Rochela (6 de diciembre) está lista."
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
            to=[correo],
        )
        email.attach_alternative(html_content, "text/html")
        email.mixed_subtype = "related"

        # Adjuntar QR si existe
        if qr_path and os.path.exists(qr_path):
            try:
                with open(qr_path, "rb") as qr_file:
                    email.attach(f"QR_{primer_nombre}_{cc}.png", qr_file.read(), "image/png")
            except Exception as e:
                logger.warning(f"No se pudo adjuntar QR: {e}")

        # Adjuntar flyer embebido (inline)
        try:
            flyer_path = os.path.join(settings.BASE_DIR, "static", "images", "flyer.png")
            # Si tu carpeta es “imagen” en vez de “images”, cámbialo
            if not os.path.exists(flyer_path):
                flyer_path = os.path.join(settings.BASE_DIR, "static", "imagen", "flyer.png")
            if os.path.exists(flyer_path):
                with open(flyer_path, "rb") as f:
                    flyer = MIMEImage(f.read())
                    flyer.add_header("Content-ID", "<flyer_mocoabeats>")
                    flyer.add_header("Content-Disposition", "inline", filename="flyer.png")
                    email.attach(flyer)
            else:
                logger.warning(f"Flyer no encontrado en {flyer_path}")
        except Exception as e:
            logger.warning(f"No se pudo adjuntar flyer inline: {e}")

        # Enviar
        email.send()
        logger.info(f"Email enviado a {correo} ({primer_nombre})")
        return True

    except Exception as e:
        logger.error(f"Error enviando email a {getattr(asistente, 'correo', 'sin_correo')}: {str(e)}")
        print(f"Error detallado: {e}")
        return False
