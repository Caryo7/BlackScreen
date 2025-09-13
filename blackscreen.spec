# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['blackscreen.py'],
    #pathex=[],
    #binaries=[],
    #datas=[],
    #hiddenimports=[],
    #hookspath=[],
    #hooksconfig={},
    #runtime_hooks=[],
    #excludes=[],
    #noarchive=False,
    #optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    #exclude_binaries=True,
    name='blackscreen',
    debug=False,
    #bootloader_ignore_signals=False,
    #strip=False,
    upx=True,
    console=False,
    #disable_windowed_traceback=False,
    #argv_emulation=False,
    #target_arch=None,
    #codesign_identity=None,
    #entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    #upx=True,
    #upx_exclude=[],
    name='blackscreen',
)

print('Config file copy...')
for fp, to in [('mkdir', 'dist/blackscreen/config'),
               ('config/default.ini', 'dist/blackscreen/config/default.ini'),
               ('readme.md', 'dist/blackscreen/readme.md'),
               ('LICENSE', 'dist/blackscreen/LICENSE'),
               ]:
               
    if fp == 'mkdir':
        os.mkdir(to)
    else:
        f = open(fp, 'rb')
        ft = open(to, 'wb')
        ft.write(f.read())
        f.close()
        ft.close()
