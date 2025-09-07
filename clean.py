import os
import shutil


assets_dir = './assets'
journal_dir = './journals'
pages_dir = './pages'
to_delete_dir = './to_delete'

if not os.path.exists(to_delete_dir):
    os.makedirs(to_delete_dir)

assets_files = os.listdir(assets_dir)
referenced_files = []


for dirname in [journal_dir, pages_dir]:
    for filename in os.listdir(dirname):
        if filename.endswith('.md'):
            # 打开 .md 文件
            with open(os.path.join(dirname, filename),encoding="utf-8") as f:
                # 遍历文件中的每一行
                for line in f:
                    # 遍历 assets 目录中的所有文件
                    for asset in assets_files:
                        # 如果这一行包含了 assets 目录中的某个文件的名称，则将这个文件的名称加入到 referenced_files 列表中
                        if asset in line:
                            referenced_files.append(asset)


for asset in assets_files:
    if asset not in referenced_files and not asset.endswith(".edn"):
        print(asset)
        shutil.move(os.path.join(assets_dir, asset), to_delete_dir)