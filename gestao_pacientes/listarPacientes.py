<!DOCTYPE html>
<html>
<head>
    <title>Lista de Pacientes</title>
</head>
<body>
    <h1>Lista de Pacientes</h1>
    <ul>
        {% for paciente in pacientes %}
            <li>{{ paciente.nome }} - {{ paciente.idade }} anos - {{ paciente.email }} - {{ paciente.telefone }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'adicionar_paciente' %}">Adicionar Novo Paciente</a>
</body>
</html>

