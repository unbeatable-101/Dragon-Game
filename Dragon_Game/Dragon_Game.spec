# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['E:/Python/Dragon_Game/Dragon_Game/Dragon_Game.py'],
             pathex=['E:\\Python\\Dragon_Game\\Dragon_Game'],
             binaries=[],
             datas=[('E:/Python/Dragon_Game/Dragon_Game/pyfiglet/fonts', 'fonts/'), ('E:/Python/Dragon_Game/Dragon_Game/pyfiglet', 'pyfiglet/')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Dragon_Game',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
