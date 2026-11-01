from pathlib import Path
import json,shutil,unicodedata,hashlib
root=Path(__file__).resolve().parent.parent
out=root/'soundboard/dist'
rules=[('👋','挨拶・返事','おは|あざ|ただいま|帰還|うい|okey|ごめん'),('✨','わくわく・喜び','waku|waka|わく|うれし|スターライト|おでけけ|song'),('😲','驚き・困った','びっくり|大事件|怖|AHHH|Ueeww|Ah anya|嫌|下手'),('🥜','食べもの','peanut|ピーナッツ|お菓子|minduim'),('💬','友だち・呼びかけ','ちち|ルカ|ちう|キム|涼介|そういちろう|ゆいか|もとき|仲良|可愛|かわい|名前'),('🎭','ツッコミ・いたずら','くび|くそ|くさい|正体|乳|世界|ことない')]
import re
items=[]
for i,p in enumerate(sorted(root.rglob('*.mp3'))):
 if 'soundboard' in p.parts: continue
 name=unicodedata.normalize('NFC',p.stem).replace('[Anya]','').strip()
 cat=next((c for _,c,pat in rules if re.search(pat,name,re.I)),'内容確認')
 dest=f'audio/{i:03}.mp3';shutil.copy2(p,out/dest)
 items.append(dict(id=str(i),title=name,category=cat,src=dest,original=str(p.relative_to(root)),basis='ファイル名から推定' if cat!='内容確認' else '内容未確認'))
(out/'sounds.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
print(len(items),'files packaged')
