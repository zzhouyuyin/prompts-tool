# 简单的ChatGPT提示词生成工具
import random

# 定义提示词模板列表
prompt_templates = [
    "请帮我优化这段文字，使其更简洁易懂：{text}",
    "请解释这个编程概念，用新手能懂的语言：{concept}",
    "请为我制定一份{topic}的学习计划，分7天完成"
]

# 随机获取一个提示词模板
def get_random_prompt():
    return random.choice(prompt_templates)

# 示例使用
if __name__ == "__main__":
    random_prompt = get_random_prompt()
    print("生成的提示词模板：")
    print(random_prompt)
    # 示例：填充模板
    filled_prompt = random_prompt.format(text="我想学习Python，但是不知道从哪开始")
    print("\n填充后的提示词：")
    print(filled_prompt)
