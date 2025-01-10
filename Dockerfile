# 使用官方的 Python 基础镜像
FROM python:3.9-slim
# 设置环境变量以防止 Python 写入 .pyc 文件并强制 stdout 和 stderr 不使用缓冲
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#docker常见的命令
# 设置工作目录
WORKDIR /code
# 将 requirements.txt 复制到工作目录
COPY requirements.txt /code/
# 安装 Python 依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 复制 Django 项目代码到工作目录
COPY . /code/
# 暴露 Gunicorn 将要监听的端口
EXPOSE 8888
RUN python manage.py collectstatic --noinput
# 使用 Gunicorn 启动 Django 应用
CMD ["gunicorn", "--chdir", "warehouse_management","warehouse_management.wsgi:application", "--bind", "0.0.0.0:8888"]