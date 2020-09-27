# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None


a = Analysis(['D:\\#my_code\\Projects\\2020\\kivy\\simpCalc\\main.py'],
             pathex=['D:\\#my_code\\Projects\\2020\\kivy\\simpCalc\\package'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Calc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='D:\\#my_code\\Projects\\2020\\kivy\\simpCalc\\icon.ico')
coll = COLLECT(exe, Tree('D:\\#my_code\\Projects\\2020\\kivy\\simpCalc\\assets\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
							 *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Calc v1.0')
