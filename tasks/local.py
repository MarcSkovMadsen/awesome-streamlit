from invoke import task


@task
def deploy(c):
    c.run("git push azure-web-app master")


@task
def run_server(c):
    c.run("streamlit run src/app.py")
