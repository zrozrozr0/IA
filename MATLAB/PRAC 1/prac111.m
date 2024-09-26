m = mobiledev;
m.PositionSensorEnabled = 1;
m.Logging = 1;

pause(10);

% Obtener las últimas posiciones
lat = m.latitude;
lon = m.longitude;

% Trazar el recorrido en un mapa web
webmap('OpenStreetMap');
wmline(lat, lon);
