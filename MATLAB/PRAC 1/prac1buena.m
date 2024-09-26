%zrozrozrozrozrozrozrozrozrozrozro
% Inicializar el dispositivo móvil
m = mobiledev;
m.PositionSensorEnabled = 1;
m.Logging = 1;

% Configurar el mapa web
webmap('OpenStreetMap');

% Obtener las coordenadas iniciales
lat = m.Latitude;
lon = m.Longitude;

% Inicializar el marcador en el mapa web
marker = wmmarker(lat, lon);

% Inicializar los arrays para almacenar las coordenadas
latitudes = [lat];
longitudes = [lon];

% Bucle para actualizar la posición y trazar la ruta en tiempo real
while true
    
    % Obtener las coordenadas actuales
    lat = m.Latitude;
    lon = m.Longitude;

    % Añadir las coordenadas actuales al array
    latitudes = [latitudes, lat];
    longitudes = [longitudes, lon];
    
    % Trazar la ruta con los puntos almacenados
    wmline(latitudes, longitudes,"Color","green");
    
    % Esperar un breve intervalo antes de volver a actualizar la posición
    pause(1);
end
