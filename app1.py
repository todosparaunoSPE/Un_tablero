# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 11:35:24 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime, timedelta
import random

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Profesional",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para hacer el dashboard más impresionante
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    
    .stMetric {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e1e5e9;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: white;
    }
    
    .metric-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .big-font {
        font-size: 3rem !important;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    
    .title-gradient {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .success-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .info-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .skill-badge {
        display: inline-block;
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 100%);
        color: #333;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.25rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .sidebar .stButton > button {
        background: linear-gradient(45deg, #ff6b6b 0%, #ee5a24 100%);
        width: 100%;
        margin: 0.5rem 0;
    }
    
    .animated-bg {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# Función para generar datos simulados
@st.cache_data
def generar_datos_rendimiento():
    fechas = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    datos = pd.DataFrame({
        'fecha': fechas,
        'ventas': np.random.normal(1000, 200, len(fechas)).astype(int),
        'usuarios_activos': np.random.normal(500, 100, len(fechas)).astype(int),
        'conversion': np.random.normal(0.15, 0.05, len(fechas))
    })
    return datos

@st.cache_data
def generar_datos_tecnologias():
    return pd.DataFrame({
        'Tecnología': ['Python', 'JavaScript', 'React', 'Node.js', 'SQL', 'Docker', 'AWS', 'Machine Learning'],
        'Experiencia (años)': [5, 4, 3, 3, 4, 2, 2, 3],
        'Proyectos': [15, 12, 8, 10, 20, 6, 4, 7],
        'Nivel': [95, 90, 85, 80, 90, 75, 70, 85]
    })

# Título principal con animación
st.markdown('<h1 class="title-gradient">🚀 Dashboard Profesional Interactivo</h1>', unsafe_allow_html=True)
st.markdown('<div class="success-box"><h3>💼 Desarrollador Full Stack | Data Scientist | Python Expert</h3></div>', unsafe_allow_html=True)

# Sidebar con controles
st.sidebar.markdown("## 🎛️ Panel de Control")
st.sidebar.markdown("---")

# Botones interactivos en sidebar
if st.sidebar.button("🔄 Actualizar Datos", key="refresh"):
    st.sidebar.success("✅ Datos actualizados!")
    st.cache_data.clear()

if st.sidebar.button("📊 Generar Reporte", key="report"):
    st.sidebar.success("✅ Reporte generado!")

if st.sidebar.button("💾 Exportar Dashboard", key="export"):
    st.sidebar.success("✅ Dashboard exportado!")

if st.sidebar.button("⚡ Optimizar Rendimiento", key="optimize"):
    st.sidebar.success("✅ Sistema optimizado!")

if st.sidebar.button("🔍 Análisis Avanzado", key="analysis"):
    st.sidebar.success("✅ Análisis completado!")

if st.sidebar.button("🌐 API Status", key="api"):
    st.sidebar.success("✅ API funcionando!")

if st.sidebar.button("🛡️ Security Check", key="security"):
    st.sidebar.success("✅ Seguridad verificada!")

# Selectores
modo_vista = st.sidebar.selectbox("🎨 Modo de Vista", ["Dashboard Principal", "Análisis Detallado", "Proyectos Portfolio"])
filtro_tiempo = st.sidebar.selectbox("📅 Período", ["Último Mes", "Últimos 3 Meses", "Último Año", "Todo el Tiempo"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔥 Acciones Rápidas")

# Métricas principales con animación
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric(
        label="🎯 Proyectos Completados",
        value="47",
        delta="3 este mes"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric(
        label="⏱️ Años de Experiencia",
        value="5+",
        delta="Creciendo"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric(
        label="😊 Clientes Satisfechos",
        value="128",
        delta="100% satisfacción"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric(
        label="🏆 Certificaciones",
        value="12",
        delta="2 nuevas"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Sección principal basada en la selección
if modo_vista == "Dashboard Principal":
    # Gráficos principales
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Rendimiento en el Tiempo")
        datos = generar_datos_rendimiento()
        
        fig = px.line(datos.tail(90), x='fecha', y='ventas', 
                     title='Ventas Últimos 90 Días',
                     color_discrete_sequence=['#667eea'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Distribución de Proyectos")
        proyectos_data = pd.DataFrame({
            'Tipo': ['Web Apps', 'APIs', 'Machine Learning', 'Mobile', 'Data Analysis'],
            'Cantidad': [15, 12, 8, 6, 6]
        })
        
        fig = px.pie(proyectos_data, values='Cantidad', names='Tipo',
                    title='Proyectos por Categoría',
                    color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#f5576c', '#ff9a9e'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(fig, use_container_width=True)

elif modo_vista == "Análisis Detallado":
    st.markdown("### 🔍 Análisis Técnico Detallado")
    
    # Habilidades técnicas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💻 Stack Tecnológico")
        tech_data = generar_datos_tecnologias()
        
        fig = px.bar(tech_data, x='Tecnología', y='Nivel',
                    title='Nivel de Competencia por Tecnología',
                    color='Nivel',
                    color_continuous_scale='Viridis')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Experiencia vs Proyectos")
        fig = px.scatter(tech_data, x='Experiencia (años)', y='Proyectos',
                        size='Nivel', color='Tecnología',
                        title='Relación Experiencia-Proyectos',
                        hover_name='Tecnología')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(fig, use_container_width=True)

else:  # Proyectos Portfolio
    st.markdown("### 🎨 Portfolio de Proyectos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
        <h4>🌐 E-commerce Platform</h4>
        <p><strong>Tech Stack:</strong> React, Node.js, MongoDB</p>
        <p><strong>Features:</strong> Payment integration, Real-time chat</p>
        <p><strong>Status:</strong> ✅ Completado</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>🤖 ML Prediction Model</h4>
        <p><strong>Tech Stack:</strong> Python, TensorFlow, FastAPI</p>
        <p><strong>Features:</strong> 95% accuracy, API deployment</p>
        <p><strong>Status:</strong> ✅ Completado</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
        <h4>📱 Mobile App</h4>
        <p><strong>Tech Stack:</strong> React Native, Firebase</p>
        <p><strong>Features:</strong> Cross-platform, Push notifications</p>
        <p><strong>Status:</strong> 🚧 En desarrollo</p>
        </div>
        """, unsafe_allow_html=True)

# Sección de habilidades
st.markdown("---")
st.markdown("### 🚀 Habilidades Técnicas")

skills = [
    "Python", "JavaScript", "React", "Node.js", "SQL", "MongoDB", 
    "Docker", "AWS", "Machine Learning", "Data Science", "API Development",
    "Git", "Agile/Scrum", "TensorFlow", "Pandas", "Streamlit"
]

skills_html = ""
for skill in skills:
    skills_html += f'<span class="skill-badge">{skill}</span>'

st.markdown(f'<div style="text-align: center; margin: 2rem 0;">{skills_html}</div>', unsafe_allow_html=True)

# Panel de estado del sistema
st.markdown("---")
st.markdown("### 🖥️ Estado del Sistema")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("🟢 Servidor Principal: ONLINE")
with col2:
    st.success("🟢 Base de Datos: ACTIVA")
with col3:
    st.warning("🟡 CDN: OPTIMIZANDO")
with col4:
    st.success("🟢 API Gateway: FUNCIONANDO")

# Botones de acción principal
st.markdown("---")
st.markdown("### 🎛️ Panel de Acciones")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📧 Contactar", key="contact"):
        st.balloons()
        st.success("✅ ¡Mensaje enviado! Te contactaré pronto.")

with col2:
    if st.button("💼 Ver CV", key="cv"):
        st.snow()
        st.success("✅ CV descargado correctamente.")

with col3:
    if st.button("🚀 Ver Proyectos", key="projects_btn"):
        st.balloons()
        st.success("✅ Redirigiendo a portfolio...")

with col4:
    if st.button("🤝 LinkedIn", key="linkedin"):
        st.success("✅ Perfil de LinkedIn abierto.")

# Footer con información de contacto
st.markdown("---")
st.markdown("""
<div class="animated-bg">
<h3 style="text-align: center; margin-bottom: 1rem;">💼 ¿Interesado en trabajar juntos?</h3>
<p style="text-align: center; font-size: 1.2rem;">
📧 Email: jahoperi@gmail.com 
</p>
<p style="text-align: center; font-style: italic;">
"Transformando ideas en soluciones digitales innovadoras"
</p>
</div>
""", unsafe_allow_html=True)

# Datos en tiempo real simulados
if st.sidebar.checkbox("🔴 Mostrar Datos en Tiempo Real"):
    placeholder = st.empty()
    
    for i in range(10):
        with placeholder.container():
            st.markdown("### 📊 Métricas en Tiempo Real")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Usuarios Online", f"{random.randint(150, 300)}")
            with col2:
                st.metric("CPU Usage", f"{random.randint(20, 80)}%")
            with col3:
                st.metric("Requests/min", f"{random.randint(500, 1500)}")
        
        time.sleep(2)