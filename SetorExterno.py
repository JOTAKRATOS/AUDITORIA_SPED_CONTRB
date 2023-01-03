import pandas as pd
import streamlit as st
import pyttsx3
import speech_recognition as sr

# AUDITORIA

# TABULAÇÃO

import AuditoriaSpedContribuicoes_Geral


# CONTABILIDADE

# MENU AUDITORIA
st.sidebar.title('CONTROLE INTERNO CONTÁBIL')

MenuItensContabAuditoria=['','Sped Contribuicoes']
ItensEscolhaContabAuditoria=st.sidebar.selectbox('Auditoria',MenuItensContabAuditoria)


# ESCOLHA DAS OPÇÕES	

# CONTABILIDADE


# AUDITORIA
if ItensEscolhaContabAuditoria=='Sped Contribuicoes':
	st.title('Auditoria Sped Contribuições')
	AuditoriaSpedContribuicoes_Geral.AuditoriaSpedContribuicoes()


	


	