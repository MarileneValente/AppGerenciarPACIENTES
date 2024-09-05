<!DOCTYPE html>
<html>
<head>
    <title>Adicionar Paciente</title>
</head>
<body>
    <h1>Adicionar Paciente</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Adicionar</button>
    </form>
</body>
</html>
