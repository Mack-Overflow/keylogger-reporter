# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['keystrokes.py'],
             pathex=['C:\\Users\\Kenneth\\Desktop\\Programming\\Cý̶͠b̧e̴͘̕ŕs̵͏e͏̕c͡u̸r̸i̡t̸̴̛y̢͝\\Keylogging'],
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
          name='keystrokes',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='keystrokes')
