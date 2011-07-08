#Fuel info - from James Allen UBS Strategy
fuel={'consumption':29.9,'penalty':0.038,'laps':52,'lapdistance':5.891,'racedistance':36.227,'pitloss':12,'pitStopTotal':16}

#Practice Data
fp1times=[['1', 'S. VETTEL', '1', '9:05:51', '2', '23:01.547', '3', '1:52.726', '4', '1:49.853', '5', '1:49.390', '6', '2:00.643', '7', '1:49.076', '8', '1:48.794', '9', '2:08.016', '10', '1:50.313', '11', '1:52.606', '12', '21:11.626', '13', '1:49.602', '14', '1:50.832', '15', '1:48.996', '16', '1:49.726', '17', '1:50.447', '18', '1:48.864', '19', '1:46.396', '20', '7:27.803', '21', '2:18.735'], ['2', 'M. WEBBER', '1', '9:08:56', '2', '13:59.686', '3', '1:51.659', '4', '1:50.032', '5', '2:08.633', '6', '25:52.734', '7', '2:40.955', '8', '1:48.185', '9', '1:50.886', '10', '1:51.377', '11', '15:37.980', '12', '1:49.166', '13', '1:47.553', '14', '1:55.660', '15', '1:46.881', '16', '1:50.716', '17', '1:46.603', '18', '1:54.878'], ['3', 'L. HAMILTON', '1', '9:12:06', '2', '15:32.098', '3', '1:53.505', '4', '1:50.427', '5', '1:49.577', '6', '1:53.985', '7', '1:49.429', '8', '1:52.654', '9', '14:13.113', '10', '2:46.919', '11', '10:28.332', '12', '1:51.066', '13', '1:55.747', '14', '1:50.942', '15', '1:52.429', '16', '9:04.946', '17', '1:48.549', '18', '1:56.480', '19', '1:48.964', '20', '1:51.395', '21', '1:51.347'], ['4', 'J. BUTTON', '1', '9:05:00', '2', '15:04.891', '3', '2:26.364', '4', '1:53.081', '5', '1:51.041', '6', '1:50.354', '7', '1:49.651', '8', '2:05.493', '9', '1:49.203', '10', '2:01.886', '11', '12:43.384', '12', '2:22.447', '13', '1:51.292', '14', '1:49.110', '15', '1:52.042', '16', '1:49.601', '17', '1:48.841', '18', '1:58.518', '19', '21:41.537', '20', '2:01.963', '21', '1:51.524', '22', '1:48.955', '23', '1:58.629'], ['5', 'F. ALONSO', '1', '9:06:45', '2', '18:14.055', '3', '1:54.152', '4', '1:50.571', '5', '2:11.954', '6', '2:47.209', '7', '14:49.676', '8', '7:09.852', '9', '1:48.952', '10', '1:48.161', '11', '2:03.367', '12', '11:31.936', '13', '1:55.861', '14', '2:54.595', '15', '1:55.854', '16', '8:59.073'], ['6', 'F. MASSA', '1', '9:06:00', '2', '27:10.538', '3', '1:52.073', '4', '1:50.105', '5', '1:49.174', '6', '2:20.454', '7', '39:34.599', '8', '1:48.438', '9', '1:52.935', '10', '1:48.109', '11', '2:24.458', '12', '1:47.562', '13', '2:02.828'], ['7', 'M. SCHUMACHER', '1', '9:11:58', '2', '11:23.608', '3', '1:51.782', '4', '1:49.220', '5', '10:00.773', '6', '1:49.585', '7', '1:59.846', '8', '1:48.388', '9', '1:54.709', '10', '1:48.278', '11', '1:51.647', '12', '14:58.815', '13', '1:50.269', '14', '1:49.534', '15', '15:44.720', '16', '1:48.517', '17', '1:48.499', '18', '2:02.952', '19', '1:47.263', '20', '1:58.304'], ['8', 'N. ROSBERG', '1', '9:06:58', '2', '13:32.782', '3', '1:51.590', '4', '2:00.863', '5', '11:54.647', '6', '1:49.982', '7', '1:50.762', '8', '1:59.468', '9', '2:25.724', '10', '1:49.467', '11', '2:01.797', '12', '1:48.904', '13', '2:07.887', '14', '15:39.143', '15', '1:49.787', '16', '1:58.868', '17', '1:49.671', '18', '2:05.240', '19', '10:01.991', '20', '1:47.758', '21', '1:55.733', '22', '1:48.011', '23', '1:59.518'], ['9', 'N. HEIDFELD', '1', '9:16:19', '2', '15:22.052', '3', '1:56.273', '4', '1:54.366', '5', '1:53.313', '6', '1:55.969', '7', '2:29.436', '8', '1:52.211', '9', '1:59.346', '10', '1:51.319', '11', '1:50.639', '12', '1:57.671', '13', '28:12.724', '14', '1:53.324', '15', '2:22.906', '16', '1:50.402', '17', '2:07.388', '18', '1:49.309', '19', '1:48.941', '20', '1:58.364'], ['10', 'V. PETROV', '1', '9:05:58', '2', '2:04.830', '3', '42:04.260', '4', '1:55.135', '5', '1:53.686', '6', '1:51.985', '7', '1:50.921', '8', '1:55.628', '9', '2:06.424', '10', '20:50.293', '11', '1:50.917', '12', '1:59.841', '13', '1:51.513', '14', '1:49.603', '15', '1:55.160'], ['11', 'R. BARRICHELLO', '1', '9:07:13', '2', '14:53.347', '3', '1:55.548', '4', '1:52.687', '5', '11:57.375', '6', '1:51.349', '7', '1:55.809', '8', '1:50.648', '9', '1:59.658', '10', '2:56.202', '11', '1:50.536', '12', '1:49.965', '13', '1:59.451', '14', '1:49.501', '15', '1:59.375', '16', '20:45.452', '17', '2:01.748', '18', '1:52.067', '19', '1:49.463', '20', '2:02.149', '21', '1:56.605', '22', '1:47.347', '23', '1:54.275'], ['12', 'P. MALDONADO', '1', '9:04:48', '2', '38:20.283', '3', '1:56.530', '4', '1:52.258', '5', '2:01.222', '6', '1:50.548', '7', '1:53.703', '8', '1:49.526', '9', '1:56.928', '10', '23:40.792', '11', '1:54.593', '12', '1:49.132', '13', '1:50.187', '14', '1:49.237', '15', '1:48.809', '16', '1:49.888', '17', '1:58.779'], ['14', 'N. HULKENBERG', '1', '9:04:51', '2', '25:06.627', '3', '1:55.371', '4', '1:52.264', '5', '1:50.607', '6', '1:58.934', '7', '1:50.451', '8', '1:56.593', '9', '17:42.964', '10', '1:52.463', '11', '1:57.211', '12', '1:51.622', '13', '1:51.086', '14', '13:53.777', '15', '1:50.146', '16', '1:49.138', '17', '1:48.598', '18', '1:55.318', '19', '1:47.844'], ['15', 'P. DI RESTA', '1', '9:02:01', '2', '34:34.363', '3', '1:52.223', '4', '1:50.962', '5', '1:58.348', '6', '1:50.826', '7', '1:49.904', '8', '1:59.938', '9', '10:33.646', '10', '1:49.321', '11', '1:52.232', '12', '1:51.283', '13', '1:54.794', '14', '16:14.136', '15', '1:48.730', '16', '1:52.661', '17', '1:48.851', '18', '1:48.990', '19', '1:49.837'], ['16', 'K. KOBAYASHI', '1', '9:05:33', '2', '2:18.197', '3', '27:03.834', '4', '1:53.966', '5', '1:54.432', '6', '1:50.848', '7', '2:03.007', '8', '1:50.133', '9', '1:50.543', '10', '16:02.352', '11', '1:52.339', '12', '1:52.955', '13', '1:52.203', '14', '1:52.409', '15', '1:55.903', '16', '1:51.217'], ['17', 'S. PEREZ', '1', '9:08:25', '2', '2:03.962', '3', '29:20.303', '4', '2:32.413', '5', '1:53.715', '6', '1:52.241', '7', '1:50.682', '8', '1:49.612', '9', '1:59.436', '10', '1:49.541', '11', '1:57.555', '12', '1:48.497', '13', '10:03.476', '14', '1:51.851', '15', '1:50.876', '16', '1:51.671', '17', '1:52.261', '18', '9:58.800', '19', '1:48.809', '20', '2:01.698', '21', '1:47.422', '22', '2:03.541'], ['18', 'S. BUEMI', '1', '9:02:11', '2', '21:30.969', '3', '1:59.263', '4', '17:55.946', '5', '1:52.190', '6', '1:51.155', '7', '1:50.622', '8', '1:49.736', '9', '1:49.653', '10', '1:52.518', '11', '24:16.146', '12', '1:51.372', '13', '1:49.193', '14', '1:57.715', '15', '1:48.778', '16', '1:57.774', '17', '1:48.851', '18', '1:54.409'], ['19', 'J. ALGUERSUARI', '1', '9:02:38', '2', '16:47.059', '3', '2:04.184', '4', '7:29.669', '5', '1:56.270', '6', '1:50.613', '7', '1:50.302', '8', '1:50.907', '9', '18:54.885', '10', '1:49.247', '11', '1:48.678', '12', '1:55.084', '13', '1:50.553', '14', '1:49.954', '15', '1:50.619', '16', '12:41.165', '17', '1:53.978', '18', '1:53.275', '19', '1:52.947', '20', '1:52.766', '21', '1:52.002', '22', '1:51.765'], ['20', 'K. CHANDHOK', '1', '9:06:55', '2', '13:34.743', '3', '7:56.371', '4', '2:39.980', '5', '10:35.995', '6', '1:59.068', '7', '1:54.373', '8', '1:53.436', '9', '1:52.301', '10', '1:53.116', '11', '1:54.997', '12', '1:59.961', '13', '29:12.313', '14', '1:51.119', '15', '1:56.020', '16', '1:51.279', '17', '1:57.522'], ['21', 'J. TRULLI', '1', '9:06:43', '2', '13:38.146', '3', '7:48.844', '4', '2:26.065', '5', '11:53.182', '6', '1:54.739', '7', '2:00.389', '8', '1:53.594', '9', '1:52.357', '10', '1:52.616', '11', '2:08.839', '12', '1:50.653', '13', '1:50.222', '14', '2:08.745'], ['22', 'D. RICCIARDO', '1', '9:03:40', '2', '21:27.802', '3', '2:03.701', '4', '2:00.183', '5', '1:59.187', '6', '2:02.578', '7', '1:57.370', '8', '1:57.119', '9', '1:56.445', '10', '1:55.915', '11', '12:03.866', '12', '1:57.934', '13', '1:55.151', '14', '1:54.878', '15', '1:55.724', '16', '1:59.799', '17', '1:54.628', '18', '16:54.349', '19', '1:55.184', '20', '1:54.334', '21', '1:59.743', '22', '1:58.641', '23', '2:00.143', '24', '1:53.615'], ['23', 'V. LIUZZI', '1', '9:03:35', '2', '27:28.248', '3', '2:02.762', '4', '2:01.764', '5', '1:58.951', '6', '1:56.482', '7', '1:55.967', '8', '2:09.942', '9', '11:59.255', '10', '1:54.844', '11', '1:54.862', '12', '2:03.473', '13', '1:56.976', '14', '2:02.805', '15', '18:15.895', '16', '1:53.836', '17', '1:53.782', '18', '1:53.143', '19', '1:59.096', '20', '2:00.491'], ['24', 'T. GLOCK', '1', '9:03:07', '2', '11:52.130', '3', '28:55.789', '4', '1:55.027', '5', '1:53.854', '6', '2:01.436', '7', '1:53.482', '8', '1:53.333', '9', '2:09.543', '10', '17:21.332', '11', '1:56.201', '12', '1:55.297', '13', '8:03.667', '14', '1:52.550', '15', '2:00.306', '16', '1:52.470', '17', '1:53.048'], ['25', "J. D'AMBROSIO", '1', '9:02:29', '2', '11:30.714', '3', '2:03.001', '4', '2:05.025', '5', '8:10.207', '6', '1:57.356', '7', '1:57.014', '8', '1:56.454', '9', '1:56.066', '10', '2:00.887', '11', '27:25.954', '12', '1:59.356', '13', '1:59.144', '14', '1:58.199', '15', '1:57.960', '16', '1:56.780', '17', '2:01.365', '18', '2:01.688', '19', '2:02.860', '20', '1:55.091', '21', '1:54.403', '22', '1:59.416', '23', '1:53.860', '24', '1:53.469', '25', '1:55.471', '26', '1:55.054']]
fp1classification=[['1', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:46.603', '198.939', '10:29:25', '19'], ['2', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:47.263', '0.660', '197.715', '10:30:06', '20'], ['3', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:47.347', '0.744', '0.084', '197.561', '10:30:09', '23'], ['4', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:47.422', '0.819', '0.075', '197.423', '10:30:30', '22'], ['5', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari', '1:47.562', '0.959', '0.140', '197.166', '10:30:18', '13'], ['6', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:47.758', '1.155', '0.196', '196.807', '10:27:24', '23'], ['7', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari', '1:48.161', '1.558', '0.403', '196.074', '9:59:19', '16'], ['8', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:48.549', '1.946', '0.388', '195.373', '10:24:40', '21'], ['9', '14', 'N. HULKENBERG', 'GER', 'Force India F1 Team', '1:48.598', '1.995', '0.049', '195.285', '10:25:59', '19'], ['10', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:48.678', '2.075', '0.080', '195.141', '9:58:59', '22'], ['11', '15', 'P. DI RESTA', 'GBR', 'Force India F1 Team', '1:48.730', '2.127', '0.052', '195.048', '10:24:02', '18'], ['12', '18', 'S. BUEMI', 'SUI', 'Scuderia Toro Rosso', '1:48.778', '2.175', '0.048', '194.962', '10:26:26', '18'], ['13', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:48.794', '2.191', '0.016', '194.933', '9:40:03', '21'], ['14', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:48.809', '2.206', '0.015', '194.906', '10:29:22', '17'], ['15', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:48.841', '2.238', '0.032', '194.849', '10:00:08', '23'], ['16', '9', 'N. HEIDFELD', 'GER', 'Lotus Renault GP', '1:48.941', '2.338', '0.100', '194.670', '10:31:27', '20'], ['17', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:49.603', '3.000', '0.662', '193.494', '10:30:03', '15'], ['18', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:50.133', '3.530', '0.530', '192.563', '9:44:28', '17'], ['19', '21', 'J. TRULLI', 'ITA', 'Team Lotus', '1:50.222', '3.619', '0.089', '192.408', '9:57:53', '14'], ['20', '20', 'K. CHANDHOK', 'IND', 'Team Lotus', '1:51.119', '4.516', '0.897', '190.854', '10:26:12', '17'], ['21', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:52.470', '5.867', '1.351', '188.562', '10:30:43', '17'], ['22', '23', 'V. LIUZZI', 'ITA', 'HRT F1 Team', '1:53.143', '6.540', '0.673', '187.440', '10:28:58', '20'], ['23', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:53.469', '6.866', '0.326', '186.902', '10:29:05', '26'], ['24', '22', 'D. RICCIARDO', 'AUS', 'HRT F1 Team', '1:54.334', '7.731', '0.865', '185.488', '10:25:26', '24']]



fp2times=[['1', 'S. VETTEL', '1', '14:15:40', '2', '1:57.564', '3', '1:54.545', '4', '2:00.953'], ['2', 'M. WEBBER', '1', '14:09:35', '2', '1:54.340', '3', '1:53.537', '4', '1:59.651', '5', '1:52.587', '6', '1:51.921'], ['3', 'L. HAMILTON', '1', '14:22:20', '2', '1:57.900', '3', '1:54.713', '4', '2:00.114', '5', '1:51.438', '6', '1:52.235'], ['4', 'J. BUTTON', '1', '14:17:07', '2', '2:08.132', '3', '7:24.106', '4', '1:54.580', '5', '1:51.518', '6', '2:12.661'], ['5', 'F. ALONSO', '1', '14:10:41', '2', '1:55.426', '3', '3:00.024', '4', '1:54.274', '5', '1:52.869', '6', '2:20.422', '7', '6:27.077', '8', '2:32.420'], ['6', 'F. MASSA', '1', '14:16:43', '2', '1:58.547', '3', '1:54.919', '4', '2:03.358', '5', '1:53.593', '6', '1:57.770', '7', '2:49.249', '8', '1:49.967', '9', '1:52.199'], ['7', 'M. SCHUMACHER', '1', '13:57:19', '2', '1:56.820', '3', '1:55.397', '4', '1:55.175', '5', '1:58.859', '6', '8:09.885', '7', '1:53.024', '8', '1:58.000', '9', '9:52.287', '10', '1:52.325', '11', '1:52.977', '12', '2:01.912'], ['8', 'N. ROSBERG', '1', '13:53:58', '2', '2:03.754', '3', '2:02.218', '4', '2:03.471', '5', '1:58.200', '6', '2:01.301', '7', '1:56.420', '8', '1:55.942', '9', '2:01.269', '10', '11:45.421', '11', '1:52.700', '12', '2:29.119', '13', '1:57.392', '14', '1:50.744', '15', '1:54.990'], ['9', 'N. HEIDFELD', '1', '14:09:21', '2', '1:56.848', '3', '2:03.936', '4', '1:59.489', '5', '2:34.414', '6', '10:23.095', '7', '1:54.023', '8', '1:58.662'], ['10', 'V. PETROV', '1', '14:09:10', '2', '1:57.159', '3', '1:55.874', '4', '1:57.422', '5', '2:01.497', '6', '1:58.460', '7', '10:14.315', '8', '1:52.198', '9', '1:54.193'], ['11', 'R. BARRICHELLO', '1', '13:59:55', '2', '1:59.630', '3', '2:06.166', '4', '1:56.074', '5', '2:00.924', '6', '1:54.561', '7', '2:00.576', '8', '12:03.052', '9', '1:58.538', '10', '1:54.254', '11', '1:54.792', '12', '1:51.992', '13', '1:58.912'], ['12', 'P. MALDONADO', '1', '13:56:03', '2', '2:09.616', '3', '1:57.856', '4', '2:27.221', '5', '1:55.155', '6', '2:13.626', '7', '20:05.785', '8', '2:05.021'], ['14', 'A. SUTIL', '1', '13:50:23', '2', '2:05.096', '3', '2:00.384', '4', '1:58.609', '5', '1:56.664', '6', '1:56.035', '7', '2:03.316', '8', '2:38.449', '9', '1:53.676', '10', '1:54.126', '11', '5:41.553', '12', '1:55.376', '13', '1:56.013', '14', '1:57.326', '15', '7:40.139', '16', '1:52.261', '17', '1:51.738', '18', '2:01.727'], ['15', 'P. DI RESTA', '1', '14:13:33', '2', '1:57.081', '3', '1:55.215', '4', '1:54.708', '5', '9:36.789', '6', '1:51.781', '7', '1:59.711'], ['16', 'K. KOBAYASHI', '1', '13:16:19', '2', '36:25.323', '3', '2:03.185', '4', '2:02.483', '5', '1:56.766', '6', '2:05.038', '7', '6:42.901', '8', '2:06.427', '9', '1:55.317', '10', '1:56.380', '11', '9:02.489', '12', '1:55.110', '13', '1:55.552', '14', '2:00.150', '15', '1:51.395', '16', '1:58.179'], ['17', 'S. PEREZ', '1', '13:52:09', '2', '2:03.169', '3', '2:14.110', '4', '14:21.575', '5', '1:55.230', '6', '2:03.246', '7', '2:03.150', '8', '1:59.731', '9', '7:55.510', '10', '1:53.944', '11', '1:52.169', '12', '2:12.397'], ['18', 'S. BUEMI', '1', '13:09:34', '2', '41:24.170', '3', '2:02.354', '4', '1:58.323', '5', '1:57.654', '6', '1:56.527', '7', '1:57.491', '8', '1:54.678', '9', '1:54.101', '10', '1:53.727', '11', '1:53.619', '12', '2:04.640', '13', '6:48.514', '14', '1:57.950', '15', '2:03.983', '16', '1:54.997', '17', '1:54.037', '18', '1:53.369', '19', '1:57.840', '20', '1:52.189', '21', '1:56.273'], ['19', 'J. ALGUERSUARI', '1', '13:07:55', '2', '2:30.560', '3', '39:05.296', '4', '2:04.096', '5', '2:01.984', '6', '1:57.384', '7', '1:55.583', '8', '1:55.399', '9', '1:54.274', '10', '2:03.141', '11', '12:25.617', '12', '1:55.733', '13', '1:54.473', '14', '1:56.346', '15', '1:54.806', '16', '1:58.691'], ['20', 'H. KOVALAINEN', '1', '14:00:09', '2', '2:00.771', '3', '1:59.711', '4', '2:00.346', '5', '1:57.860', '6', '1:59.135', '7', '1:58.228', '8', '1:57.732', '9', '1:57.582', '10', '2:01.398', '11', '6:04.248', '12', '1:54.708', '13', '1:53.997', '14', '1:53.017', '15', '1:52.578', '16', '1:56.908'], ['21', 'J. TRULLI', '1', '14:00:01', '2', '2:04.098', '3', '2:06.663', '4', '2:02.812', '5', '1:57.782', '6', '2:09.312', '7', '8:48.914', '8', '1:59.697', '9', '5:22.150', '10', '1:55.809', '11', '1:55.155', '12', '2:09.584'], ['22', 'D. RICCIARDO', '1', '14:15:03', '2', '2:04.922', '3', '2:04.891', '4', '1:58.145', '5', '1:57.580', '6', '1:57.356', '7', '2:03.179', '8', '1:56.698', '9', '1:55.828', '10', '2:03.850'], ['23', 'V. LIUZZI', '1', '14:23:23', '2', '2:11.476', '3', '1:57.183', '4', '2:01.770', '5', '1:56.037', '6', '2:03.126'], ['24', 'T. GLOCK', '1', '13:05:18', '2', '14:15:51', '3', '1:59.837', '4', '2:01.442', '5', '1:57.697', '6', '1:59.945', '7', '1:57.149', '8', '2:21.461', '9', '1:55.549', '10', '2:01.235'], ['25', "J. D'AMBROSIO", '1', '14:01:49', '2', '2:04.705', '3', '2:01.910', '4', '2:08.946', '5', '2:03.433', '6', '2:00.962', '7', '1:59.865', '8', '9:26.235', '9', '1:56.706', '10', '1:55.383', '11', '2:01.409', '12', '1:54.714', '13', '2:07.364']]

fp2classification=[['1', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari', '1:49.967', '192.854', '14:31:10', '9'], ['2', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:50.744', '0.777', '191.501', '14:29:56', '16'], ['3', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:51.395', '1.428', '0.651', '190.381', '14:30:17', '16'], ['4', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:51.438', '1.471', '0.043', '190.308', '14:30:04', '6'], ['5', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:51.518', '1.551', '0.080', '190.171', '14:30:25', '6'], ['6', '14', 'A. SUTIL', 'GER', 'Force India F1 Team', '1:51.738', '1.771', '0.220', '189.797', '14:31:44', '18'], ['7', '15', 'P. DI RESTA', 'GBR', 'Force India F1 Team', '1:51.781', '1.814', '0.043', '189.724', '14:30:48', '7'], ['8', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:51.992', '2.025', '0.211', '189.367', '14:31:35', '13'], ['9', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:52.169', '2.202', '0.177', '189.068', '14:30:31', '12'], ['10', '18', 'S. BUEMI', 'SUI', 'Scuderia Toro Rosso', '1:52.189', '2.222', '0.020', '189.034', '14:30:54', '21'], ['11', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:52.198', '2.231', '0.009', '189.019', '14:31:07', '9'], ['12', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:52.325', '2.358', '0.127', '188.805', '14:28:51', '12'], ['13', '20', 'H. KOVALAINEN', 'FIN', 'Team Lotus', '1:52.578', '2.611', '0.253', '188.381', '14:31:40', '16'], ['14', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:52.587', '2.620', '0.009', '188.366', '14:17:15', '6'], ['15', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari', '1:52.869', '2.902', '0.282', '187.895', '14:19:24', '8'], ['16', '9', 'N. HEIDFELD', 'GER', 'Lotus Renault GP', '1:54.023', '4.056', '1.154', '185.994', '14:30:13', '8'], ['17', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:54.274', '4.307', '0.251', '185.585', '14:01:20', '16'], ['18', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:54.545', '4.578', '0.271', '185.146', '14:19:32', '4'], ['19', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:54.714', '4.747', '0.169', '184.873', '14:31:23', '13'], ['20', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:55.155', '5.188', '0.441', '184.165', '14:04:33', '8'], ['21', '21', 'J. TRULLI', 'ITA', 'Team Lotus', '1:55.155', '5.188', '0.000', '184.165', '14:30:23', '12'], ['22', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:55.549', '5.582', '0.394', '183.537', '14:30:04', '10'], ['23', '22', 'D. RICCIARDO', 'AUS', 'HRT F1 Team', '1:55.828', '5.861', '0.279', '183.095', '14:31:02', '10'], ['24', '23', 'V. LIUZZI', 'ITA', 'HRT F1 Team', '1:56.037', '6.070', '0.209', '182.765', '14:31:29', '6']]



fp3times=[]

fp3classification=[]


#Qualifying
qualitimes=[]

qualiclassification=[]

qualisectors=[]
qualitrap=[]
qualispeeds=[]

#Race
stops=[]
analysis=[]
chart=[]
history=[]
speeds=[]
sectors=[]
trap=[]
classification=[]

#Drivers
driverShort={'1':"VET",'2':"WEB",'3':"HAM",'4':"BUT",'5':"ALO",'6':"MAS",'7':"SCH",'8':"ROS",'9':"HEI",'10':"PET",'11':"BAR",'12':"MAL",'14':"SUT",'15':"RES",'16':"KOB",'17':"PER",'18':"BUE",'19':"ALG",'20':"TRU",'21':"KOV",'22':"KAR",'23':"LIU",'24':"GLO",'25':"AMB"}


#Tyre data from Pirelli
tyres=[]