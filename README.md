# Alma Assisted Counseling Chatbot  
# Alma 辅助咨询聊天机器人

---

## English Introduction

### Project Introduction
Alma is a Python-based intelligent counseling chatbot designed to provide emotional support, psychological assistance, and information guidance.  
This folder contains the core application code, configuration files, data, and front-end templates, enabling quick deployment and usage.

### Directory Structure
```
my_app/
├── app/                # Core application
│   ├── __init__.py     # Flask app initialization
│   ├── config.py       # Project configuration
│   ├── models.py       # Data models
│   ├── routes.py       # Routes & business logic
│   ├── utils.py        # Utility functions
│   ├── static/         # Static resources (CSS, JS, images)
│   └── templates/      # HTML templates
├── data/               # Data files
├── requirements.txt    # Python dependencies
├── run.py              # Application entry point
└── structure.txt       # Project structure description
```

### Installation & Running

1. **Clone the repository**
```bash
git clone https://github.com/PeijiaBian/Alma-Assisted-Counseling-Chatbot.git
cd Alma-Assisted-Counseling-Chatbot/my_app
```

2. **Create virtual environment & install dependencies**
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

3. **Run the application**
```bash
python run.py
```
The application will be available at `http://127.0.0.1:5000`.

### Features
- **Intelligent Conversation**: NLP-powered natural language interactions.
- **Emotion Recognition**: Detects emotional tone from user input.
- **Extensibility**: Easy to add custom modules and APIs.
- **Visual Frontend**: Flask templates for a clean web interface.

---

## 中文介绍

### 项目简介
Alma 是一个基于 Python 的智能咨询聊天机器人，旨在为用户提供情感支持、心理咨询辅助和信息引导。  
该文件夹包含核心应用代码、配置文件、数据目录以及前端模板，方便快速部署和使用。

### 目录结构
```
my_app/
├── app/                # 核心应用目录
│   ├── __init__.py     # Flask 应用初始化
│   ├── config.py       # 项目配置
│   ├── models.py       # 数据模型
│   ├── routes.py       # 路由与业务逻辑
│   ├── utils.py        # 工具函数
│   ├── static/         # 静态资源（CSS、JS、图片）
│   └── templates/      # HTML 模板
├── data/               # 数据文件
├── requirements.txt    # Python 依赖
├── run.py              # 应用入口
└── structure.txt       # 项目结构说明
```

### 安装与运行

1. **克隆仓库**
```bash
git clone https://github.com/PeijiaBian/Alma-Assisted-Counseling-Chatbot.git
cd Alma-Assisted-Counseling-Chatbot/my_app
```

2. **创建虚拟环境并安装依赖**
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

3. **启动应用**
```bash
python run.py
```
应用将在 `http://127.0.0.1:5000` 运行。

### 功能特点
- **智能对话**：基于 NLP 的自然语言交互。
- **情绪识别**：识别用户输入的情绪倾向。
- **可扩展性**：支持自定义模块与数据接口。
- **可视化前端**：基于 Flask 模板构建简洁网页界面。

