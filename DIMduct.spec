# -*- mode: python -*-

block_cipher = None

dlls = [
    ('D:\\Python3\\Lib\\site-packages\\numpy\\.libs\\libopenblas.UWVN3XTD2LSS7SFIFK6TIQ5GONFDBJKU.gfortran-win32.dll', '.'),
    ('D:\\Python3\\Lib\\site-packages\\scipy\\extra-dll', '.')
]

a = Analysis(['.\\DIMduct.py', '.\\dim\\mainwindow.py', '.\\dim\\arbitraria.py', '.\\dim\\constante1.py',
              '.\\dim\\constante2.py', '.\\dim\\estatica.py', '.\\dim\\resultados.py', '.\\dim\\erro.py'],
             pathex=['C:\\Users\\gabri\\OneDrive\\Documentos\\apprtest'],
             binaries= dlls,
             datas=[('.\\imgs\\icon.ico', '.\\imgs'), ('.\\manual.pdf', '.')],
             hiddenimports=['PyQt5.sip', 'scipy._lib.messagestream'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='DIMduct',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='DIMduct')
