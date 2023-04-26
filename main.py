import zapv2

target = 'url'
zap = zapv2.ZAPv2()

zap.core.new_session()
zap.core.access_url(target)
zap.ascan.enable_all_scanners()
zap.ascan.set_option_max_depth(5)
zap.ascan.set_option_thread_per_host(5)

scan_id = zap.ascan.scan(target)

while int(zap.ascan.status(scan_id)) < 100:
    print('Прогресс сканирования: ' + zap.ascan.status(scan_id) + '%')
    time.sleep(5)

alerts = zap.core.alerts()
if len(alerts) == 0:
    print('Сканирование завершено. Уязвимости не обнаружены.')
else:
    print('Сканирование завершено. Обнаружены следующие уязвимости:')
    for alert in alerts:
        print('- ' + alert.get('name') + ' (' + alert.get('risk') + ')')
