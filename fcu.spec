# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['function.py','逢甲大學搶課系統.py'],
    pathex=['C:\\Users\\jeff0\\Desktop\\fcu_course'],
    binaries=[],
    datas=[
       ('data/*.json', 'data'),   
       ('image/*.jpg', 'image'),
	   ('./onnxruntime_providers_shared.dll','onnxruntime\\capi'),
	   ('./common.onnx', 'ddddocr'),
	   ('./common_old.onnx', 'ddddocr'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='fcu',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='fcu',
)
