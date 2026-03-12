# 升级版 ChatGPT 提示词生成工具
# 支持：多场景分类、自定义参数填充、提示词保存
import random
import datetime

# 扩展提示词模板库（分更多实用场景）
PROMPT_TEMPLATES = {
    "编程辅助": [
        "请作为资深{language}工程师，帮我检查以下代码的语法错误和逻辑漏洞，并给出优化建议：\n{code}",
        "请用{language}实现一个{function}功能，要求代码简洁、注释清晰、兼容Python3.8+版本",
        "请解释{concept}这个编程概念，用新手能懂的语言举例说明，最好附带代码示例"
    ],
    "文案创作": [
        "请以{topic}为主题，写一篇{word_count}字左右的科普短文，语言通俗易懂，适合{audience}阅读",
        "请帮我优化这段文字，使其更{style}：\n{text}",
        "请为{product}写3条吸引人的社交媒体文案，风格{style}（幽默/专业/温馨）"
    ],
    "学习总结": [
        "请用思维导图的形式，总结{subject}的核心知识点，分点清晰，突出重点",
        "请为我制定一份{topic}的学习计划，分{days}天完成，每天明确学习目标和资源",
        "请列出学习{skill}的常见误区，并给出避开这些误区的建议"
    ],
    "职场办公": [
        "请帮我写一封{type}邮件，收件人是{recipient}，核心内容是{content}",
        "请优化这份{document_type}的结构，使其逻辑更清晰，重点更突出",
        "请为{meeting_topic}会议制定一份15分钟的议程，包含核心讨论点和时间分配"
    ]
}

def get_random_prompt(scene=None):
    """
    获取随机提示词模板
    :param scene: 指定场景（如"编程辅助"），None则随机选场景
    :return: 选中的场景、随机提示词模板
    """
    # 选择场景
    if scene and scene in PROMPT_TEMPLATES:
        selected_scene = scene
    else:
        selected_scene = random.choice(list(PROMPT_TEMPLATES.keys()))
    
    # 选择该场景下的随机模板
    selected_prompt = random.choice(PROMPT_TEMPLATES[selected_scene])
    return selected_scene, selected_prompt

def fill_prompt_template(prompt_template, **kwargs):
    """
    填充提示词模板中的占位符
    :param prompt_template: 原始模板
    :param kwargs: 要填充的参数（如language="Python", code="print('hello')"）
    :return: 填充后的完整提示词
    """
    try:
        filled_prompt = prompt_template.format(**kwargs)
        return filled_prompt
    except KeyError as e:
        return f"填充失败：缺少参数 {e}，请补充后重试"

def save_prompt(prompt, filename="generated_prompts.txt"):
    """
    保存生成的提示词到文件
    :param prompt: 要保存的提示词内容
    :param filename: 保存的文件名
    """
    with open(filename, "a", encoding="utf-8") as f:
        # 添加时间戳，方便管理
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}]\n{prompt}\n{'='*50}\n")
    print(f"提示词已保存到 {filename}")

# 交互式使用示例
if __name__ == "__main__":
    print("=== ChatGPT 提示词生成工具（升级版）===\n")
    
    # 1. 展示所有可用场景
    print("可用场景：")
    for i, scene in enumerate(PROMPT_TEMPLATES.keys(), 1):
        print(f"{i}. {scene}")
    
    # 2. 选择场景（示例）
    user_choice = input("\n请输入场景序号（直接回车则随机）：")
    scene_list = list(PROMPT_TEMPLATES.keys())
    if user_choice.isdigit() and 1 <= int(user_choice) <= len(scene_list):
        selected_scene = scene_list[int(user_choice)-1]
    else:
        selected_scene = None
    
    # 3. 获取并填充提示词
    scene, prompt = get_random_prompt(selected_scene)
    print(f"\n【{scene}】随机提示词模板：")
    print(prompt)
    
    # 示例填充（可根据实际需求修改参数）
    if scene == "编程辅助":
        filled = fill_prompt_template(prompt, language="Python", concept="装饰器")
    elif scene == "文案创作":
        filled = fill_prompt_template(prompt, topic="AI工具使用技巧", word_count=500, audience="新手")
    else:
        filled = fill_prompt_template(prompt, topic="Python基础语法", days=7)
    
    print("\n填充后的完整提示词：")
    print(filled)
    
    # 4. 保存提示词（可选）
    save_choice = input("\n是否保存该提示词？(y/n)：")
    if save_choice.lower() == "y":
        save_prompt(filled)
        print("保存成功！")

print("\n工具使用完成 ✨")
