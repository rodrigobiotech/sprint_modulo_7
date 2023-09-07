
// grafico Dashboard


// Datos para el gráfico de barras
var barChartData = {
    labels: ['Pendientes', 'En Progreso', 'Terminadas', 'Canceladas'],
    datasets: [{
        label: 'Tareas por Estado',
        backgroundColor: ['red', 'blue', 'green', 'gray'],
        data: [contTareasPendientes, contTareasEnProgreso, contTareasTerminadas, contTareasCanceladas]
    }]
};
// Datos para el gráfico de torta
var pieChartData = {
    labels: ['Pendientes', 'En Progreso', 'Terminadas', 'Canceladas'],
    datasets: [{
        data: [contTareasPendientes, contTareasEnProgreso, contTareasTerminadas, contTareasCanceladas],
        backgroundColor: ['red', 'blue', 'green', 'gray']
    }]
};

// Configuración común para ambos gráficos
var chartConfig = {
    responsive: true
};

// Crear gráfico de barras
var barChartCtx = document.getElementById('barChart').getContext('2d');
new Chart(barChartCtx, {
    type: 'bar',
    data: barChartData,
    options: chartConfig
});

// Crear gráfico de torta
var pieChartCtx = document.getElementById('pieChart').getContext('2d');
new Chart(pieChartCtx, {
    type: 'pie',
    data: pieChartData,
    options: chartConfig
});



