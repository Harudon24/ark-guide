from pathlib import Path

p = Path('beginner_base_2x2_stats.html')
text = p.read_text(encoding='utf-8')

marker = '''    <div class="ui-note">
      <b>アイテムを作る流れ：</b>'''

note = '''    <div class="ui-note">
      <b>エングラム取得時の注意：</b><br>
      エングラムポイントには限りがあり、レベルが上がってもすべてのエングラムを覚えられるわけではありません。<br>
      迷ったら、建築・道具・武器など<strong>今すぐ使うもの</strong>を優先して取得するのがおすすめです。<br>
      特に<strong>恐竜のサドルは、その恐竜をテイムしてから必要なものだけ取得すればOK</strong>です。
    </div>

'''

if 'エングラム取得時の注意：' not in text:
    if marker not in text:
        raise SystemExit('insert marker not found')
    text = text.replace(marker, note + marker, 1)
    p.write_text(text, encoding='utf-8')
