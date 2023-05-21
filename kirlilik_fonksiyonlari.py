def cop_ayristirma(cop_turu):
    sari_kutu = ['ambalajlar', 'yoğurt kutusu', 'meyve suyu']
    mavi_kutu = ['kağıt atıkları', 'kartonlar', 'gazeteler']
    siyah_kutu = ['porselen', 'hijyenik ürünler', 'kirli ambalajlar']

    
    if cop_turu == 'Sarı':
        return 'Ambalajlar, Yoğurt kutusu, Meyve Suyu'
    elif cop_turu == 'Mavi':
        return 'Kağıt, Atıklar,Kartonlar,Gazeteler'
    elif cop_turu == 'Siyah':
        return 'Porselen,Hijyenik ürünler,Kirli ambalajlar'
    else:
        return 'Bilemedim \U0001F92F'
