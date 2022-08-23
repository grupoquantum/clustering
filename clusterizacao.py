from Neuraline.Utilities.chart import Chart
chart = Chart()
clusters = [[[1, 2], [3, 4], [5, 6], [7, 8]], [[10, 20], [30, 40], [50, 60], [70, 80]], [[100, 200], [300, 400], [500, 600], [700, 800]]]
chart.plotCLUSTERING(clusters=clusters, clusters_name=['unidades', 'dezenas', 'centenas'], title='Clusterização de Dados')