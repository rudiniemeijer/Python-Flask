<!doctype html>
<title>Dit is een servicebericht van Flask</title>
{% if begroetingsnaam %}
  <h1>Hallo {{ begroetingsnaam }}!</h1>
{% else %}
  <h1>Hallo, vreemdeling-waarvan-we-de-naam-niet-kennen!</h1>
{% endif %}
