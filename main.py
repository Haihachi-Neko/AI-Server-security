import ollama
import subprocess
import json

def main() :
    ps_output = subprocess.check_output(["ps", "ax", "--sort=-pcpu"]).decode("utf-8")
    response = ollama.chat(
    model='qwen3.5:0.8b',
    messages=[{
        'role': 'system',
        'content': 'あなたは優秀な熟練のインフラエンジニアです。以下の指示にしたがってください。 \
        サーバーの情報やログを確認し、またツールを呼び出して必要な情報を確認することで不審なプロセスやユーザーがいないか確認し、もし不審なプロセス、ユーザーを発見したらそれを通知することをゴールとします。 \
        ## 出力形式 \
        出力形式は必ずJSON形式で、以下の例の通り出力してください。余計な解説は不要です。必ずこのJSONのみになるよう出力してください。 \
        {{"status": "OK / WARN / CRITICAL", "cause": "問題を引き起こした原因となるユーザー、プロセスを簡潔に説明", "reason": "通知した理由を簡潔に説明"}}'
    },
    {
        'role': 'user',
        'content': f'以下のログを確認し、不審なプロセスやユーザーがいないか確認してください。\nps axの結果: {ps_output}'
    }],
    think=False,
    format='json'
    )

    print(response.message.content)

if __name__ == '__main__':
    main()