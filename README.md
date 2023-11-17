# Herramienta de Sincronización de IP Dinámica

## Descripción

He creado este script en Python para mantener actualizados los registros DNS de Cloudflare al tener un servidor en casa con una dirección IP dinámica. La herramienta automatiza el proceso de sincronización para garantizar que los nombres de dominio estén siempre asociados a la dirección IP correcta.

## Cómo Funciona

1. **Archivo de Configuración:**
   - La configuración se gestiona a través del archivo `config.json`, donde se almacenan los detalles de Cloudflare y la información de los dominios que deseas gestionar.

2. **Obtención de la Dirección IP:**
   - Se obtiene la dirección IP pública actual utilizando 'https://checkip.amazonaws.com'.

3. **Comparación y Actualización:**
   - Compara la dirección IP obtenida con la última dirección IP registrada en la configuración.
   - Si hay una diferencia, el script actualiza automáticamente la configuración con la nueva IP.

4. **Actualización de Registro DNS en Cloudflare:**
   - Itera a través de la lista de dominios en la configuración y actualiza los registros DNS de Cloudflare con la nueva dirección IP.

## Configuración Personalizada

1. **Instalación de Dependencias:**
   - Asegúrate de tener Python instalado en tu servidor.
   - Instala las dependencias ejecutando:
     ```
     pip install requests
     ```

2. **Configuración Personal:**
   - Personaliza el archivo `config.example.json` con la información específica de tus dominios y tu cuenta de Cloudflare y renombra el archivo a config.json

3. **Ejecución del Script:**
   - Ejecuta el script con el comando:
     ```
     python main.py
     ```
   - Programa la ejecución periódica del script para mantener actualizados tus registros DNS.
   

