import requests
import streamlit as st
from streamlit_lottie import st_lottie
# find more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":rocket:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
       return None
    return r.json()

def load_lottieurl_2(url):
    n = requests.get(url)
    if n.status_code !=200:
       return None
    return n.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#--- LOAD---

lottie_coding_1 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_dtjpftcu.json")
lottie_coding_2 = load_lottieurl_2("https://assets7.lottiefiles.com/packages/lf20_q8oE6pkvKV.json")

# --- HEADER SECTION----
with st.container():
			st.subheader("Salut, Je m'appelle Moustapha :wave:")
			st.title("Je suis un passionné de la Technologie")
			st.write(
                    """
                    Intéressé par les outils d'automatisation Open Source | Python est mon LangageLover ❤
                    - Je suis à la recherche d'un poste en Admin Systeme Linux | DevOps 
                    - Disponibilité : Juillet 2023

                    """
                      )

# ---Body #

with st.container():
   st.write("---")
   left_column, right_column = st.columns(2)
   with left_column:
        st.header("Mes compétences")
        st.write("###")
        st.write(
            """
          - Environnement: Linux ( Redhat, CentOS, Debian, Ubuntu), Windows Server
          - Virtualisation  : Vmware, Hyper V, Virtualbox
          - Serveur applicatif : Apache, Tomcat
          - Bases de Données: SQL, PostgreSQL, Mysql, Active Directory
          - Langage: Shell , Python
          - Conteneurisation: Docker , Kubernetes
          - Gestion de configuration: Ansible , Packer (template)
          - Gestionnaire de code source : Git , Gitlab , Github
          - CI/CD: Jenkins, Gitlab CI
          - Ordonnancement : Dollar U, Control M
          - Supervision: PRTG, Nagios
          - Gestion de projet: Jira 
          - Cloud : AWS
                    """
             )
   with right_column:
         st_lottie(lottie_coding_1, height=300, key=("coding"))



with st.sidebar:
           #"""with st.echo():"""
              st.header('Mes Links')
              st.write(
                """
                En perpétuel apprentissage et de partage de connaissance, j'ai créer un blog pour exposer mes projets et me motiver à apprendre en profondeur 
                
                - Langues : Anglais , Français , Wolof
                """
                )
              st.header('Langues')
              st.write(
                """
                  - Anglais 
                  - Français 
                  - Wolof
                """
                )
with st.container():
        st.write("----")
        st.header("Pour plus d'informations")
        st.write("###")
 
      #---Contact form doc: https://formsubmit.co/
        contact_form = """
        <form action="https://formsubmit.co/kamaldossier@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value"false">
             <input type="text" name="name" placeholder="NOM et PRENOM" required>
             <input type="email" name="email" placeholder= "Email" required>
             <textarea name= "message" placeholder= " Ecris ici ton message" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
                  st_lottie(lottie_coding_2, height=300, )
        with right_column:
                  st.markdown(contact_form, unsafe_allow_html=True)

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    video_file = open('movie_discipline.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
  with right_column: 
    st.empty()