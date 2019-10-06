from invoke import task


@task
def run_server(c):
    c.run(
        "cp .streamlit/config.prod.toml ~/.streamlit/config.toml & cp .streamlit/credentials.prod.toml ~/.streamlit/credentials.toml & streamlit run src/app.py"
    )
