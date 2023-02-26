def webp_t():
    ffmpeg_path = "D:/ffmpeg/ffmpeg.exe"

    import os
    for file in os.listdir("../input"):
        name = file.split('.')[0]
        os.system(f"{ffmpeg_path} -i \"../input/{file}\" \"../meme/{name}.webp\"")
    print("已完成")

def qq2md():
    import re, json
    md_cot: list = []

    with open("./transf/input.txt", "r", encoding="utf-8") as f:
        raw_cot = f.readlines()
    title = input("请输入标题:\n")
    md_cot.append(f"# {title}")
    md_cot.append(" ")

    chara_vs: dict = json.load(open("./transf/chara.json", "r", encoding="utf-8"))
    md_line = "- "
    for line in raw_cot:
        if("2022" in line):
            isFound = False
            for raw_name in chara_vs.keys():
                if raw_name in line:
                    md_line += f"{chara_vs.get(raw_name)}: "
                    isFound = True
                else:
                    continue
            if(not isFound):
                raise Exception(f"此段缺少人物:\n{line}")
        elif(line == '\n'):
            if(md_line == "- "):
                continue
            md_line += "  "
            md_cot.append(md_line)
            md_line = "- "
        else:
            md_line += line
    
    md_cot.append("\n")
    with open("out.md", "w", encoding="utf-8") as f:
        f.writelines(md_cot)
    

if __name__ == "__main__":
    choice = input("请选择模式:\n1.webp批量转换\n2.聊天记录文本转Markdown\n")
    if(choice == "1"):
        webp_t()
    else:
        qq2md()