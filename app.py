import pandas as pd
import streamlit as st 
from PIL import Image

st.set_page_config(
    layout="wide",
    page_title="Solicitação Ressonância Magnética SMS RJ",
    page_icon="🧐"
)

image_button_aprov = Image.open('.venv/button_apr.png')
image_button_neg = Image.open('.venv/button_neg.png')
image_button_pend = Image.open('.venv/button_pend.png')
image = Image.open('.venv/banner.png')

st.image(image, caption=None, output_format="JPEG")



# Initialize session state
if 'show_patient_data' not in st.session_state:
    st.session_state.show_patient_data = False

if 'show_request_form' not in st.session_state:
    st.session_state.show_request_form = False

def main():
    # INPUT CALCULADORA
    with st.form(key='calculator_form'):
        # Ingresa el valor
        cpf_paciente = st.text_input("CPF/CNS")
        nome_paciente = st.text_input("Nome do Usuário")
        nome_mae_paciente = st.text_input("Nome da Mãe")
        submit_button = st.form_submit_button(label='Pesquisar', use_container_width=True)

    if submit_button:
        st.session_state.show_patient_data = True

    if st.session_state.show_patient_data:
        st.markdown("<h1 style='text-align: center; color: black;'>Dados do Paciente </h1>", unsafe_allow_html=True)
        #st.title("Dados do Paciente")
        st.write("CNS: xxxxxxxxxxx")
        st.write("Nome: xxxxxxxxxxx")
        st.write("Nome da Mãe: xxxxxxxxxxx")
        st.write("Sexo: xxxxxxxxxxx")
        st.write("Data de Nascimento: xxxxxxxxxxx")

        if st.button("Iniciar Solicitação", type="primary"):
            st.session_state.show_request_form = True

    if st.session_state.show_request_form:
        st.markdown("<h1 style='text-align: center; color: black;'>Informações de Solicitação</h1>", unsafe_allow_html=True)
        #st.title("Informações de Solicitação")

        cid_paciente = st.text_input("Qual o CID suspeito?")

        options_purpose = ['Follow up / acompanhamento', 'Rastreamento', 'Suspeita', 'Estadiamento', 'Esclarecer diagnóstico']
        purpose = st.selectbox('Qual a finalidade da solicitação desse exame?', [''] + options_purpose)

        # Function to handle purpose selection
        if purpose == 'Follow up / acompanhamento':
            display_follow_up_options()
        elif purpose == 'Rastreamento':
            display_screening_options()
        elif purpose == 'Suspeita':
            display_suspect_options()
        elif purpose == 'Estadiamento':
            display_staging_options()
        elif purpose == 'Esclarecer diagnóstico':
            display_diagnostic_options()

def display_follow_up_options():
    options_follow_up = ['Câncer Renal', 'Câncer Próstata', 'Câncer Bexiga', 'Câncer Testículo', 'Tumor osso primário em ossos do quadril', 'Outra']
    follow_up = st.selectbox('Tipo de acompanhamento:', [''] + options_follow_up)
    
    if follow_up in ['Câncer Renal', 'Câncer Próstata', 'Câncer Bexiga', 'Câncer Testículo', 'Tumor osso primário em ossos do quadril']:
        #st.write("Aprovado")
        st.image(image_button_aprov, caption=None, output_format="JPEG")
    elif follow_up == 'Outra':
        #st.write("Negado")
        st.image(image_button_neg, caption=None, output_format="JPEG")
        

def display_staging_options():
    options_staging = ['Câncer Coloretal', 'Câncer de Ovário', 'Câncer de Vagina', 'Câncer na Vulva', 'Doença Trofoblástica Gestacional', 'Outra']
    staging = st.selectbox('Tipo de estadiamento:', [''] + options_staging)
    
    if staging == 'Câncer Coloretal':
        display_colorectal_options()
    elif staging == 'Câncer de Ovário':
        display_ovarian_options()
    elif staging == 'Câncer de Vagina':
        display_vaginal_options()
    elif staging == 'Câncer na Vulva':
        display_vulvar_options()
    elif staging == 'Doença Trofoblástica Gestacional':
        display_gtg_options()
    elif staging == 'Outra':
        #st.write("Negado")
        st.image(image_button_neg, caption=None, output_format="JPEG")

def display_colorectal_options():
    confirmed_diagnosis = st.selectbox('Paciente tem diagnóstico confirmado?', ['', 'Sim', 'Não'])
    
    if confirmed_diagnosis == 'Sim':
        neoadjuvant = st.selectbox('Realizou QT neoadjuvante?', ['', 'Sim', 'Não'])
        if neoadjuvant == 'Sim':
            #st.write("Aprovado")
            st.image(image_button_aprov, caption=None, output_format="JPEG")

        elif neoadjuvant == 'Não':
            #st.write("Negado")
            st.image(image_button_neg, caption=None, output_format="JPEG")
    elif confirmed_diagnosis == 'Não':
        #st.write("Negado")
        st.image(image_button_neg, caption=None, output_format="JPEG")

def display_ovarian_options():
    treatment = st.selectbox('Já realizou tratamento?', ['', 'Sim', 'Não'])
    
    if treatment == 'Sim':
        recurrence = st.selectbox('Suspeita de recidiva?', ['', 'Sim', 'Não'])
        if recurrence == 'Sim':
            #st.write("Aprovado")
            st.image(image_button_aprov, caption=None, output_format="JPEG")

        elif recurrence == 'Não':
            #st.write("Negado")
            st.image(image_button_neg, caption=None, output_format="JPEG")
    elif treatment == 'Não':
        #st.write("Aprovado")
        st.image(image_button_aprov, caption=None, output_format="JPEG")


def display_vaginal_options():
    treatment = st.selectbox('Já realizou tratamento?', ['', 'Sim', 'Não'])
    
    if treatment == 'Sim':
        recurrence = st.selectbox('Suspeita de recidiva?', ['', 'Sim', 'Não'])
        if recurrence == 'Sim':
            #st.write("Aprovado")
            st.image(image_button_aprov, caption=None, output_format="JPEG")

        elif recurrence == 'Não':
            #st.write("Negado")
            st.image(image_button_neg, caption=None, output_format="JPEG")
    elif treatment == 'Não':
        #st.write("Aprovado")
        st.image(image_button_aprov, caption=None, output_format="JPEG")


def display_vulvar_options():
    treatment = st.selectbox('Já realizou tratamento?', ['', 'Sim', 'Não'])
    
    if treatment == 'Sim':
        recurrence = st.selectbox('Suspeita de recidiva?', ['', 'Sim', 'Não'])
        if recurrence == 'Sim':
            #st.write("Aprovado")
            st.image(image_button_aprov, caption=None, output_format="JPEG")

        elif recurrence == 'Não':
            #st.write("Negado")
            st.image(image_button_neg, caption=None, output_format="JPEG")
    elif treatment == 'Não':
        #st.write("Aprovado")
        st.image(image_button_aprov, caption=None, output_format="JPEG")


def display_gtg_options():
    confirmed_diagnosis = st.selectbox('Diagnóstico confirmado?', ['', 'Sim', 'Não'])
    
    if confirmed_diagnosis == 'Sim':
        #st.write("Aprovado")
        st.image(image_button_aprov, caption=None, output_format="JPEG")

    elif confirmed_diagnosis == 'Não':
        #st.write("Negado")
        st.image(image_button_neg, caption=None, output_format="JPEG")

def display_screening_options():
    options_screening = ['Câncer Coloretal', 'Câncer de Ovário', 'Câncer de Útero', 'Câncer de Trompas', 'Câncer Bexiga', 'Câncer de Ureteres', 'Câncer de Rins', 'Outra']
    screening = st.selectbox('Tipo de rastreamento:', [''] + options_screening)
    
    if screening:
        #st.write("Negado")
        st.image(image_button_neg, caption=None, output_format="JPEG")

def display_suspect_options():
    st.write("Não aprovado - Critérios não preenchidos para suspeita")

def display_diagnostic_options():
    alteration_exam = st.selectbox('Queixas ou alteração no exame físico?', ['','Sim, Quais?', 'Não possui', 'Não avaliado'])
    
    if alteration_exam == 'Sim, Quais?':
        body_part = st.selectbox('Qual parte do corpo?', ['','Cabeça e pescoço', 'Aparelho respiratório', 'Aparelho cardiovascular', 'Abdome', 'Aparelho geniturinário'])
        
        if body_part in ['Cabeça e pescoço', 'Aparelho respiratório', 'Aparelho cardiovascular']:
            #st.write("Negado")
            st.image(image_button_neg, caption=None, output_format="JPEG")
        elif body_part == 'Abdome':
            abdomen_condition = st.selectbox('Qual condição?', ['','Massa abdominal palpável', 'Dor abdominal', 'Hérnia'])
            
            if abdomen_condition == 'Massa abdominal palpável':
                tc_pelvis = st.selectbox('Realizou TC prévia?', ['','Sim', 'Não'])
                if tc_pelvis == 'Sim':
                    tc_result = st.selectbox('Resultado foi esclarecedor?', ['','Sim', 'Não'])
                    if tc_result == 'Sim':
                        #st.write("Negado")
                        st.image(image_button_neg, caption=None, output_format="JPEG")
                    elif tc_result == 'Não':
                        topography = st.selectbox('Qual topografia?', ['','Quadrante inferior direito', 'Quadrante inferior esquerdo', 'Hipogástrio inferior/esquerdo/alça'])
                        if topography in ['Quadrante inferior direito', 'Quadrante inferior esquerdo']:
                            #st.write("Aprovado")
                            st.image(image_button_aprov, caption=None, output_format="JPEG")

                        elif topography == 'Hipogástrio inferior/esquerdo/alça':
                            #st.write("Aprovado")
                            st.image(image_button_aprov, caption=None, output_format="JPEG")

                elif tc_pelvis == 'Não':
                    #st.write("Negado")
                    st.image(image_button_neg, caption=None, output_format="JPEG")
            elif abdomen_condition == 'Dor abdominal':
                evolution_time = st.selectbox('Qual tempo de evolução?', ['','Aguda', 'Crônica'])
                if evolution_time == 'Aguda':
                    alteration_lab = st.selectbox('Possui alteração no exame laboratorial de neutrófilos?', ['','Sim', 'Não'])
                    if alteration_lab == 'Sim':
                        #st.write("Aprovado")
                        st.image(image_button_aprov, caption=None, output_format="JPEG")

                    elif alteration_lab == 'Não':
                        tc_pelvis = st.selectbox('Realizou TC prévia?', ['','Sim', 'Não'])
                        if tc_pelvis == 'Sim':
                            tc_result = st.selectbox('Resultado foi esclarecedor?', ['','Sim', 'Não'])
                            if tc_result == 'Sim':
                                #st.write("Negado")
                                st.image(image_button_neg, caption=None, output_format="JPEG")
                            elif tc_result == 'Não':
                                #st.write("Aprovado")
                                st.image(image_button_aprov, caption=None, output_format="JPEG")

                        elif tc_pelvis == 'Não':
                            #st.write("Negado")
                            st.image(image_button_neg, caption=None, output_format="JPEG")
                elif evolution_time == 'Crônica':
                    #st.write("Negado")
                    st.image(image_button_neg, caption=None, output_format="JPEG")
            elif abdomen_condition == 'Hérnia':
                hernia_confirmed = st.selectbox('Diagnóstico confirmado?', ['','Sim', 'Não'])
                if hernia_confirmed == 'Sim':
                    pre_op = st.selectbox('É necessária para preparo pré-operatório?', ['','Sim', 'Não'])
                    if pre_op == 'Sim':
                        #st.write("Aprovado")
                        st.image(image_button_aprov, caption=None, output_format="JPEG")

                    elif pre_op == 'Não':
                        st.write("Negado")
                        #st.image(image_button_neg, caption=None, output_format="JPEG")
                elif hernia_confirmed == 'Não':
                    #st.write("Negado")
                    st.image(image_button_neg, caption=None, output_format="JPEG")
        elif body_part == 'Aparelho geniturinário':
            genitourinary_condition = st.selectbox('Qual condição?', ['','Prolapso urogenital', 'Hematúria', 'Sangramento uterina anormal', 'Dor pélvica'])
            
            if genitourinary_condition == 'Prolapso urogenital':
                #st.write("Negado")
                st.image(image_button_neg, caption=None, output_format="JPEG")
            elif genitourinary_condition == 'Hematúria':
                usg_tc = st.selectbox('Realizou USG ou TC prévia?', ['','Sim', 'Não'])
                if usg_tc == 'Sim':
                    usg_tc_result = st.selectbox('Resultado foi esclarecedor?', ['','Sim', 'Não'])
                    if usg_tc_result == 'Sim':
                        #st.write("Negado")
                        st.image(image_button_neg, caption=None, output_format="JPEG")
                    elif usg_tc_result == 'Não':
                        #st.write("Aprovado")
                        st.image(image_button_aprov, caption=None, output_format="JPEG")

                elif usg_tc == 'Não':
                    #st.write("Negado")
                    st.image(image_button_neg, caption=None, output_format="JPEG")
            elif genitourinary_condition == 'Sangramento uterina anormal':
                pregnant = st.selectbox('Gestante?', ['','Sim', 'Não'])
                if pregnant == 'Sim':
                    usg = st.selectbox('Realizou USG prévia?', ['','Sim', 'Não'])
                    if usg == 'Sim':
                        usg_result = st.selectbox('Resultado foi esclarecedor?', ['','Sim', 'Não'])
                        if usg_result == 'Sim':
                            #st.write("Negado")
                            st.image(image_button_neg, caption=None, output_format="JPEG")
                        elif usg_result == 'Não':
                            #st.write("Aprovado")
                            st.image(image_button_aprov, caption=None, output_format="JPEG")

                    elif usg == 'Não':
                        #st.write("Negado")
                        st.image(image_button_neg, caption=None, output_format="JPEG")
                elif pregnant == 'Não':
                    #st.write("Negado")
                    st.image(image_button_neg, caption=None, output_format="JPEG")
            elif genitourinary_condition == 'Dor pélvica':
                pelvic_pain_time = st.selectbox('Qual tempo de evolução?', ['','Aguda', 'Crônica'])
                if pelvic_pain_time == 'Aguda':
                    usg = st.selectbox('Realizou USG prévia?', ['','Sim', 'Não'])
                    if usg == 'Sim':
                        usg_result = st.selectbox('Resultado foi esclarecedor?', ['','Sim', 'Não'])
                        if usg_result == 'Sim':
                            #st.write("Negado")
                            st.image(image_button_neg, caption=None, output_format="JPEG")
                        elif usg_result == 'Não':
                            #st.write("Aprovado")
                            st.image(image_button_aprov, caption=None, output_format="JPEG")

                    elif usg == 'Não':
                        #st.write("Negado")
                        st.image(image_button_neg, caption=None, output_format="JPEG")
                elif pelvic_pain_time == 'Crônica':
                    #st.write("Negado")
                    st.image(image_button_neg, caption=None, output_format="JPEG")
    elif alteration_exam in ['Não possui', 'Não avaliado']:
        #st.write("Negado")
        st.image(image_button_neg, caption=None, output_format="JPEG")

if __name__ == "__main__":
    main()
